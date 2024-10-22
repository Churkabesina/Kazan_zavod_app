import sys
from operator import index

from PySide6.QtCore import Qt, Slot, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QFrame, QComboBox, QStyledItemDelegate, QDialog
from select import select

from UI.extended_UI import ExtendedUIStorageFrame
from backend.db_backend import Database
from designer_UI.in_out_metal_storage_dialog_ui import Ui_in_out_metal_storage_dialog


class StorageFrame(QFrame):
    def __init__(self, main_window, db: Database):
        super().__init__()

        self.main_window = main_window
        self.db = db
        self.ui = ExtendedUIStorageFrame()
        self.ui.setupUi(self)

        self.table_data = self.db.select_storage_table_rows()
        self.table_model = TableModel(self.table_data, self.db)
        self.ui.storage_db_table.setModel(self.table_model)
        self.ui.storage_db_table.horizontalHeader().hideSection(0)

        self.in_out_dialog = InOutStorageDialog(self.table_model, self.db)

        self.negative_delegate = NegativeNumberDelegate(self.ui.storage_db_table)
        self.ui.storage_db_table.setItemDelegateForColumn(3, self.negative_delegate)


        self.ui.back_button.clicked.connect(self.back_button_slot)
        self.ui.in_storage_button.clicked.connect(self.in_storage_button_slot)
        self.ui.out_storage_button.clicked.connect(self.out_storage_button_slot)

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
            print('Ошибка метода data в table_model: невалидный индекс модели')
            sys.exit(1)
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return str(self._data[row][col])

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
        last_id = self.db.select_last_id_temp_table()
        self.beginInsertRows(parent, row, row + count - 1)
        self._data.insert(row, [last_id, '', '', '', '', '', '', '', ''])
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count - 1)
        del self._data[row:row + count]
        self.endRemoveRows()

    def find_row_by_id(self, _id):
        row_count = self.rowCount()
        for row in range(row_count):
            # _index = self.index(row, 0)
            if self._data[row][0] == _id:
                print(f'row = {row}')
                return row

class InOutStorageDialog(QDialog):
    def __init__(self, model: TableModel, db: Database):
        super().__init__()

        self.model = model
        self.db = db
        self.ui = Ui_in_out_metal_storage_dialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.ui.balance_double_spin_box.setMaximum(100000)

        ########            сделать _metal_data так: {труба: {30x30: 1, 50x50: 2})]}
        self._metal_data = self.db.select_type_metal_and_size()
        self.ui.type_metall_combo_box.addItems(list(self._metal_data.keys()))
        print(self._metal_data)
        self.is_input_dialog = True # флаг для понятия окно расхода или прихода

        self.ui.type_metall_combo_box.currentIndexChanged.connect(self.type_metal_combo_box_chosen)
        self.ui.ok_button.clicked.connect(self.ok_button_click)

        self.ui.type_metall_combo_box.setCurrentIndex(1)

    @Slot()
    def type_metal_combo_box_chosen(self):
        self.ui.size_combo_box.clear()
        type_metal = self.ui.type_metall_combo_box.currentText()
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
                self.model.setData(self.model.index(row, 2 + 1), new_balance_kg_sht)
                self.db.update_balance_kg_and_mm(type_metal, None, new_balance_kg_sht, None)
            else:
                current_balance_kg_sht = float(self.model.data(self.model.index(row, 3)))
                if self.is_input_dialog:
                    new_balance_kg_sht = current_balance_kg_sht + spin_box_value
                else:
                    new_balance_kg_sht = current_balance_kg_sht - spin_box_value
                new_balance_mm = self.balance_in_mm_formula(new_balance_kg_sht)
                self.model.setData(self.model.index(row, 3), new_balance_kg_sht)
                self.model.setData(self.model.index(row, 4), new_balance_mm)
                self.db.update_balance_kg_and_mm(type_metal, size, new_balance_kg_sht, new_balance_mm)
            print('Данные обновлены!')
            self.close()
        else:
            print('Невозможно добавить/убавить ноль')

    @staticmethod
    def balance_in_mm_formula(kg_balance) -> float:
        balance_mm = kg_balance * 3.14
        return balance_mm


class NegativeNumberDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        value = index.data()
        if float(value) < 0:
            painter.fillRect(option.rect, QBrush(QColor(178, 34, 34)))
        super().paint(painter, option, index)  # Вызов родительского метода для отрисовки остального содержимого ячейки