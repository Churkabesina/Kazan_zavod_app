import sys

from PySide6.QtCore import Qt, Slot, QAbstractTableModel, QModelIndex, QRegularExpression
from PySide6.QtGui import QBrush, QColor, QRegularExpressionValidator
from PySide6.QtWidgets import QFrame, QStyledItemDelegate, QDialog, QMessageBox

from UI.extended_UI import ExtendedUIStorageFrame
from backend.db_backend import Database
from backend.backend import unload_storage_to_excel
from designer_UI.in_out_metal_storage_dialog_ui import Ui_in_out_metal_storage_dialog
from designer_UI.add_new_metal_type_dialog_ui import Ui_add_new_metal_type_dialog


class StorageFrame(QFrame):
    def __init__(self, main_window, db: Database, storage_excel_folder):
        super().__init__()

        self.main_window = main_window
        self.db = db
        self.storage_excel_folder = storage_excel_folder
        self.ui = ExtendedUIStorageFrame()
        self.ui.setupUi(self)

        self.table_data = self.db.select_storage_table_rows()[::-1]
        self.table_model = TableModel(self.table_data, self.db)
        self.ui.storage_db_table.setModel(self.table_model)
        self.ui.storage_db_table.horizontalHeader().hideSection(0)

        self.in_out_dialog = InOutStorageDialog(self.main_window, self.table_model, self.db)
        self.add_metal_type_dialog = AddNewMetalTypeDialog(self.table_model, self.db, main_window, self.in_out_dialog)

        self.negative_delegate = NegativeNumberDelegate(self.ui.storage_db_table)
        self.ui.storage_db_table.setItemDelegateForColumn(3, self.negative_delegate)

        self.ui.back_button.clicked.connect(self.back_button_slot)
        self.ui.in_storage_button.clicked.connect(self.in_storage_button_slot)
        self.ui.out_storage_button.clicked.connect(self.out_storage_button_slot)
        self.ui.add_type_metal_button.clicked.connect(self.add_metal_type_dialog_button)
        self.ui.unload_storage_excel_button.clicked.connect(self.unload_storage_to_excel_button_slot)
        self.ui.del_type_metal_button.clicked.connect(self.del_selected_metal_type_button)

    @Slot()
    def back_button_slot(self):
        self.hide()
        self.main_window.leads_frame.show()

    @Slot()
    def in_storage_button_slot(self):
        self.in_out_dialog.ui.balance_kg_label.setText('Приход')
        self.in_out_dialog.setWindowTitle('Приход металла')
        self.in_out_dialog.is_input_dialog = True
        self.in_out_dialog.exec()

    @Slot()
    def out_storage_button_slot(self):
        self.in_out_dialog.ui.balance_kg_label.setText('Расход')
        self.in_out_dialog.setWindowTitle('Расход металла')
        self.in_out_dialog.is_input_dialog = False
        self.in_out_dialog.exec()

    @Slot()
    def add_metal_type_dialog_button(self):
        self.add_metal_type_dialog.exec()

    @Slot()
    def del_selected_metal_type_button(self):
        selected_indexes = self.ui.storage_db_table.selectedIndexes()
        if selected_indexes:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Icon.Question)
            msg_box.setWindowTitle("Подтверждение")
            msg_box.setText("Вы уверены, что хотите выполнить это действие?")
            button_yes = msg_box.addButton("Да", QMessageBox.ButtonRole.YesRole)
            button_no = msg_box.addButton("Нет", QMessageBox.ButtonRole.NoRole)
            msg_box.setDefaultButton(button_no)
            msg_box.exec()
            if msg_box.clickedButton() == button_yes:
                print("Действие подтверждено!")
                rows = sorted({index.row() for index in selected_indexes})
                for row in reversed(rows):
                    cell_index = self.table_model.index(row, 0)
                    id_from_cell = self.table_model.data(cell_index, role=Qt.UserRole)
                    self.table_model.removeRows(row, 1)
                    self.db.del_metal_type_storage_table_by_id(id_from_cell)
                self.main_window.products_db_frame.add_new_product_dialog.update_type_metal_combobox()
                print('Записи удалены!')
            else:
                print("Действие отменено")

    @Slot()
    def unload_storage_to_excel_button_slot(self):
        data = [[self.ui.type_metall_label_2.text(),
                 self.ui.size_mm_label.text(),
                 self.ui.balance_kg_label.text(),
                 self.ui.balance_mm_label.text()]]
        data.extend([x[1:] for x in self.table_model._data])
        unload_storage_to_excel(self.storage_excel_folder, data)
        print('Склад выгружен!')

class TableModel(QAbstractTableModel):
    def __init__(self, data: list[list], db: Database):
        super().__init__()
        self._data = data
        self.db = db

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return 5

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            print('Ошибка метода data в storage frame в table_model: невалидный индекс модели')
            sys.exit(1)
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return str(self._data[row][col])
        if role == Qt.UserRole:
            return self._data[row][0]

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [Qt.EditRole])
            return True
        return False

    # def flags(self, index):
    #     if index.column() == 0 or index.column() == 1:
    #         return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
    #     return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def insertRows(self, row, count, parent=QModelIndex()):
        last_row = self.db.select_last_row_storage_table()
        self.beginInsertRows(parent, row, row + count - 1)
        self._data.insert(row, last_row)
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count - 1)
        del self._data[row:row + count]
        self.endRemoveRows()

    def find_row_by_id(self, _id):
        row_count = self.rowCount()
        for row in range(row_count):
            if self._data[row][0] == _id:
                return row

class InOutStorageDialog(QDialog):
    def __init__(self, main_window, model: TableModel, db: Database):
        super().__init__()

        self.main_window = main_window
        self.model = model
        self.db = db
        self.ui = Ui_in_out_metal_storage_dialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.ui.balance_double_spin_box.setMaximum(100000)

        self._metal_data = self.db.select_storage_table_type_metal_and_size()
        self.ui.type_metall_combo_box.addItems(list(self._metal_data.keys()))
        self.is_input_dialog = True # флаг для понятия окно расхода или прихода

        self.ui.type_metall_combo_box.currentIndexChanged.connect(self.type_metal_combo_box_chosen)
        self.ui.ok_button.clicked.connect(self.ok_button_click)

        self.ui.type_metall_combo_box.setCurrentIndex(1)

    @Slot()
    def type_metal_combo_box_chosen(self):
        self.ui.size_combo_box.clear()
        type_metal = self.ui.type_metall_combo_box.currentText()
        if type_metal == '':
            return
        if 'гайка' in type_metal.lower():
            self.ui.size_combo_box.setEnabled(False)
            self.ui.kg_sht_label.setText('ШТ')
        else:
            self.ui.size_combo_box.setEnabled(True)
            self.ui.kg_sht_label.setText('КГ')
            self.ui.size_combo_box.addItems(self._metal_data[type_metal])

    @Slot()
    def ok_button_click(self):
        type_metal = self.ui.type_metall_combo_box.currentText()
        size = self.ui.size_combo_box.currentText()
        spin_box_value = float(self.ui.balance_double_spin_box.value())
        _id = self._metal_data[type_metal][size]
        if spin_box_value != 0:
            row = self.model.find_row_by_id(_id)
            if 'гайка' in type_metal.lower():
                current_balance_kg_sht = float(self.model.data(self.model.index(row, 3)))
                if self.is_input_dialog:
                    new_balance_kg_sht = current_balance_kg_sht + spin_box_value
                else:
                    new_balance_kg_sht = current_balance_kg_sht - spin_box_value
                self.model.setData(self.model.index(row, 3), new_balance_kg_sht)
                self.db.update_storage_table_balance_kg_and_mm(type_metal, None, new_balance_kg_sht, None)
            else:
                current_balance_kg_sht = float(self.model.data(self.model.index(row, 3)))
                if self.is_input_dialog:
                    new_balance_kg_sht = current_balance_kg_sht + spin_box_value
                else:
                    new_balance_kg_sht = current_balance_kg_sht - spin_box_value
                new_balance_mm = self.balance_in_mm_formula(type_metal, size, new_balance_kg_sht)
                self.model.setData(self.model.index(row, 3), new_balance_kg_sht)
                self.model.setData(self.model.index(row, 4), new_balance_mm)
                self.db.update_storage_table_balance_kg_and_mm(type_metal, size, new_balance_kg_sht, new_balance_mm)
            print('Данные обновлены!')
            self.close()
            self.main_window.deals_frame.update_model_data()
        else:
            print('Невозможно добавить/убавить ноль')

    def out_metal_from_other_frame(self, type_metal, size, out_balance):
        type_metal = type_metal
        size = size
        spin_box_value = float(out_balance)
        _id = self._metal_data[type_metal][size]
        row = self.model.find_row_by_id(_id)
        if 'гайка' in type_metal.lower():
            current_balance_kg_sht = float(self.model.data(self.model.index(row, 3)))
            new_balance_kg_sht = current_balance_kg_sht - spin_box_value
            self.model.setData(self.model.index(row, 3), new_balance_kg_sht)
            self.db.update_storage_table_balance_kg_and_mm(type_metal, None, new_balance_kg_sht, None)
        else:
            current_balance_kg_sht = float(self.model.data(self.model.index(row, 3)))
            new_balance_kg_sht = current_balance_kg_sht - spin_box_value
            new_balance_mm = self.balance_in_mm_formula(type_metal, size, new_balance_kg_sht)
            self.model.setData(self.model.index(row, 3), new_balance_kg_sht)
            self.model.setData(self.model.index(row, 4), new_balance_mm)
            self.db.update_storage_table_balance_kg_and_mm(type_metal, size, new_balance_kg_sht, new_balance_mm)

    @staticmethod
    def balance_in_mm_formula(type_metal: str, size: str, kg_balance) -> float:
        m = float(kg_balance)
        if type_metal.lower() == 'труба':
            size_split = size.split('x')
            print(size_split)
            d_external = float(size_split[0])
            print(d_external)
            d_internal = d_external - (2*float(size_split[1]))
            print(d_internal)
        else:
            d_external = float(size)
            d_internal = 0
        s = 3.14 * ((d_external / 2)**2 - (d_internal / 2)**2)
        l = round(m/(7850*s) * 1000, 3)
        return l

class AddNewMetalTypeDialog(QDialog):
    def __init__(self, model: TableModel, db: Database, main_window, in_out_dialog: InOutStorageDialog):
        super().__init__()

        self.main_window = main_window
        self.model = model
        self.db = db
        self.in_out_dialog = in_out_dialog
        self.ui = Ui_add_new_metal_type_dialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle('Добавить вид металла')

        self.ui.type_metall_combo_box.addItems(['Труба', 'Круг', 'Гайка'])

        self.regex_krug = QRegularExpression(r"^[1-9]\d*$")
        self.regex_truba = QRegularExpression(r"^[1-9]\d*[xXхХ][1-9]\d*$")
        self.regex_all = QRegularExpression()
        self.lineedit_validator = QRegularExpressionValidator(self.regex_truba)
        self.ui.lineEdit.setValidator(self.lineedit_validator)

        self.ui.ok_button_2.clicked.connect(self.add_button_slot)
        self.ui.type_metall_combo_box.currentIndexChanged.connect(self.type_metal_combo_box_chosen)

        self.ui.type_metall_combo_box.setCurrentIndex(1)

    @Slot()
    def add_button_slot(self):
        type_metal = self.ui.type_metall_combo_box.currentText()
        size = self.ui.lineEdit.text()
        if size != '':
            if self.ui.type_metall_combo_box.currentIndex() == 2:
                type_metal = type_metal + ' ' + size
                size = None
            if not self.db.check_metal_exists_storage_table(type_metal, size):
                # русская х в англ. x
                if self.ui.type_metall_combo_box.currentIndex() != 2:
                    size = size.lower().replace('х', 'x')
                self.db.insert_row_storage_table(type_metal, size)
                self.model.insertRows(self.model.rowCount(), 1)
                self.in_out_dialog._metal_data = self.db.select_storage_table_type_metal_and_size()
                self.in_out_dialog.ui.type_metall_combo_box.clear()
                self.in_out_dialog.ui.type_metall_combo_box.addItems(list(self.in_out_dialog._metal_data.keys()))
                self.main_window.products_db_frame.add_new_product_dialog.update_type_metal_combobox()
                self.ui.lineEdit.setText('')
                print('Запись добавлена!')
                self.close()
            else:
                print('Такой металл уже существует')
        else:
            print('Нужно ввести размер или название гайки')

    @Slot()
    def type_metal_combo_box_chosen(self):
        self.ui.lineEdit.setText('')
        current_text = self.ui.type_metall_combo_box.currentText()
        if current_text == 'Труба':
            self.ui.label.setText('Размер, мм')
            self.lineedit_validator.setRegularExpression(self.regex_truba)
        elif current_text == 'Круг':
            self.ui.label.setText('Размер, мм')
            self.lineedit_validator.setRegularExpression(self.regex_krug)
        else:
            self.ui.label.setText('Вид гайки')
            self.lineedit_validator.setRegularExpression(self.regex_all)


class NegativeNumberDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        value = index.data()
        if float(value) < 0:
            painter.fillRect(option.rect, QBrush(QColor(178, 34, 34)))
        super().paint(painter, option, index)  # Вызов родительского метода для отрисовки остального содержимого ячейки