import os

from PySide6.QtCore import Qt, Slot, QAbstractTableModel, QModelIndex, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QFrame, QComboBox, QStyledItemDelegate, QDialog
from win32ctypes.pywin32.pywintypes import datetime

from UI.extended_UI import ExtendedUIProductsFrame
from designer_UI.set_deal_number_dialog_ui import Ui_set_deal_number_dialog
from backend.backend import unload_products_temp_table_to_pdf
from backend.db_backend import Database

class ProductsFrame(QFrame):
    def __init__(self, main_window, db, products_pdf_folder, draws_folder):
        super().__init__()

        self.main_window = main_window
        self.db: Database = db
        self.draws_folder = draws_folder
        self.products_pdf_folder = products_pdf_folder
        self.ui = ExtendedUIProductsFrame()
        self.ui.setupUi(self)

        self.table_data = self.db.select_temp_table_rows()
        self.table_model = TableModel(self.table_data, self.db)
        self.ui.products_temp_table.setModel(self.table_model)
        self.ui.products_temp_table.horizontalHeader().hideSection(0)

        self.set_deal_number_dialog = SetDealNumberDialog(self.db)

        # Создаем делегат с элементами для QComboBox
        self.items = self.db.select_all_products_products_db()
        self.delegate = ComboBoxDelegate(self.items, self.db, self.ui.products_temp_table)
        self.ui.products_temp_table.setItemDelegateForColumn(1, self.delegate)

        self.ui.add_product_button.clicked.connect(self.add_button_click_slot)
        self.ui.del_product_button.clicked.connect(self.delete_selected_row_slot)
        self.ui.products_temp_table.customContextMenuRequested.connect(self.delete_by_right_click_slot)
        self.ui.products_temp_table.clicked.connect(self.choose_fist_cell_click_slot)
        self.ui.clear_product_button.clicked.connect(self.delete_all_rows_slot)
        self.ui.back_button.clicked.connect(self.back_button_slot)
        self.ui.products_db_button.clicked.connect(self.products_db_button_slot)
        self.table_model.dataChanged.connect(self.products_count_changed)
        self.ui.pdf_products_button.clicked.connect(self.pdf_button_slot)
        self.ui.send_to_deals_button.clicked.connect(self.send_to_deals_button_slot)

    @Slot()
    def send_to_deals_button_slot(self):
        if self.table_model.rowCount() != 0:
            rows = [row for row in self.table_model._data if row[1] != '' and row[2] != '']
            if rows:
                if self.set_deal_number_dialog.exec() == QDialog.DialogCode.Accepted:
                    for row in rows:
                        valid_row = [int(self.set_deal_number_dialog.deal_num), self.set_deal_number_dialog.date]
                        valid_row.extend(row[1:])
                        if 'гайка' in valid_row[-6].lower():
                            self.main_window.storage_frame.in_out_dialog.out_metal_from_other_frame(valid_row[-6], valid_row[-4], valid_row[-7])
                        else:
                            self.main_window.storage_frame.in_out_dialog.out_metal_from_other_frame(valid_row[-6], valid_row[-4], valid_row[-2])
                        self.db.insert_row_deals_table(valid_row)
                    self.main_window.deals_frame.update_model_data()
                    # self.main_window.leads_frame.update_model_data()
                    self.table_model.removeRows(0, self.table_model.rowCount())
                    self.db.del_temp_table_all_rows()
                else:
                    print('Диалоговое окно было закрыто без подтверждения')
            else:
                print('Нельзя отправить в изготовление только пустые продукции')
        else:
            print('Нельзя отправить ноль продукций в изготовление')

    @Slot()
    def products_count_changed(self, topLeft, bottomRight, roles):
        if topLeft.column() == 2:
            row = topLeft.row()
            _id = int(self.table_model.data(self.table_model.index(row, 0)))
            product_name = self.table_model.data(self.table_model.index(row, 1))
            type_metal = self.table_model.data(self.table_model.index(row, 3))
            count = self.table_model.data(self.table_model.index(row, 2))
            if 'гайка' not in type_metal.lower():
                weight = self.db.select_product_weight_by_product_product_db(product_name)
                total_weight = int(count)*weight
                self.table_model.setData(self.table_model.index(row, 7), total_weight)
                self.db.update_temp_table_count_and_total_weight_by_id(_id, count, total_weight)
            else:
                self.db.update_temp_table_count_and_total_weight_by_id(_id, count, None)


    @Slot()
    def add_button_click_slot(self):
        last_id = self.db.select_last_id_temp_table()
        row_count = self.table_model.rowCount()
        if last_id is None:
            self.db.add_temp_table_row(0)
        else:
            self.db.add_temp_table_row(last_id + 1)
        self.table_model.insertRows(row_count, 1)

    @Slot()
    def delete_all_rows_slot(self):
        self.table_model.removeRows(0, self.table_model.rowCount())
        self.db.del_temp_table_all_rows()

    # возможно лишнее - удаление выделенных строк через кнопку
    @Slot()
    def delete_selected_row_slot(self):
        print('заглушка')
        # selected_indexes = self.ui.products_temp_table.selectedIndexes()
        # if selected_indexes:
        #     rows = sorted({index.row() for index in selected_indexes})
        #     for row in reversed(rows):
        #         cell_index = self.table_model.index(row, 1)
        #         id_from_cell = self.table_model.data(cell_index, role=Qt.UserRole)
        #         self.table_model.removeRows(row, 1)
        #         self.db.del_temp_table_row(id_from_cell)

    @Slot()
    def delete_by_right_click_slot(self, pos):
        index = self.ui.products_temp_table.indexAt(pos)
        row = index.row()
        cell_index = self.table_model.index(row, 1)
        id_from_cell = self.table_model.data(cell_index, role=Qt.UserRole)
        if index.isValid():
            self.table_model.removeRows(row, 1)
            self.db.del_temp_table_row(id_from_cell)

    @Slot()
    def pdf_button_slot(self):
        draws_paths = []
        for row in self.table_model._data:
            draw = row[-1]
            if draw != '':
                draw_path = os.path.abspath(self.draws_folder + r'/' + draw)
                if os.path.exists(draw_path):
                    draws_paths.append(draw_path)
                else:
                    print(f'Такого чертежа: {draw} нет в папке, отмена выгрузки')
                    return
        if draws_paths:
            unload_products_temp_table_to_pdf(draws_paths, self.products_pdf_folder)
        else:
            print('Нет ни одного чертежа для выгрузки')

    @Slot()
    def choose_fist_cell_click_slot(self, index):
        if index.column() == 1:
            self.ui.products_temp_table.edit(index)

    @Slot()
    def products_db_button_slot(self):
        self.hide()
        self.main_window.products_db_frame.show()

    @Slot()
    def back_button_slot(self):
        self.hide()
        self.main_window.leads_frame.show()

class TableModel(QAbstractTableModel):
    def __init__(self, data: list[list], db: Database):
        super().__init__()
        self._data = data
        self.db = db

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return 9

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return
            # print('Ошибка метода data в products frame в table_model: невалидный индекс модели')
            # sys.exit(1)
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return str(self._data[row][col])
        if role == Qt.UserRole:
            return self._data[row][0]

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            col = index.column()
            self._data[row][col] = value
            self.dataChanged.emit(index, index, [Qt.EditRole])
            return True
        return False

    def flags(self, index):
        if index.column() == 1 or index.column() == 2:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def insertRows(self, row, count, parent=QModelIndex()):
        last_id = self.db.select_last_id_temp_table()
        self.beginInsertRows(parent, row, row + count - 1)
        self._data.insert(row, [last_id,'','','','','','','',''])
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count - 1)
        del self._data[row:row + count]
        self.endRemoveRows()


class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, items, db: Database, parent=None):
        super().__init__(parent)
        self.items = items
        self.db = db

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setEditable(True)
        editor.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        editor.completer().setCompletionMode(editor.completer().CompletionMode.PopupCompletion)
        editor.completer().setFilterMode(Qt.MatchFlag.MatchContains)
        editor.addItems(self.items)
        editor.setCurrentIndex(-1)
        editor.currentIndexChanged.connect(self.commit_and_close_editor)
        return editor

    def setEditorData(self, editor, index):
        editor.setCurrentText('')

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        if value == '' or value not in self.items:
            return
        model.setData(index, value, Qt.EditRole)
        row = index.row()
        _id = model.data(model.index(row, 0))
        update_data = self.db.select_products_db_row_by_product(value)
        model.setData(model.index(row, 1), update_data['product'])
        model.setData(model.index(row, 2), 1)
        model.setData(model.index(row, 3), update_data['type_metal'])
        model.setData(model.index(row, 4), update_data['mark_steel'])
        model.setData(model.index(row, 5), update_data['diameter'])
        model.setData(model.index(row, 6), update_data['lenght'])
        model.setData(model.index(row, 7), update_data['weight'])
        model.setData(model.index(row, 8), update_data['draw'])
        self.db.update_temp_table_row_by_id(_id, update_data)

    def commit_and_close_editor(self):
        editor = self.sender()
        self.commitData.emit(editor)
        self.closeEditor.emit(editor)


class SetDealNumberDialog(QDialog):
    def __init__(self, db: Database):
        super().__init__()

        self.db = db
        self.deal_num = None
        self.date = datetime.today().strftime('%d.%m.%Y')
        self.ui = Ui_set_deal_number_dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Выставить номер счета')

        self.line_edit_regex = QRegularExpression(r"\d+")
        self.line_edit_validator = QRegularExpressionValidator(self.line_edit_regex)
        self.ui.num_lineedit.setValidator(self.line_edit_validator)

        self.ui.ok_button.clicked.connect(self.ok_button_slot)

    @Slot()
    def ok_button_slot(self):
        num = self.ui.num_lineedit.text()
        if num != '' and not self.db.check_deal_num_exists_deals_table(int(num)):
            self.deal_num = num
            self.date = datetime.today().strftime('%d.%m.%Y')
            self.ui.num_lineedit.clear()
            self.accept()
        else:
            print('такой номер счета уже существует или введено пустое поле')
