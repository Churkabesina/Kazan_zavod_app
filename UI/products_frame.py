import sys

from PySide6.QtCore import Qt, Slot, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import QFrame, QComboBox, QStyledItemDelegate
from UI.extended_UI import ExtendedUIProductsFrame
from backend.db_backend import Database

class ProductsFrame(QFrame):
    def __init__(self, main_window, db):
        super().__init__()

        self.main_window = main_window
        self.db: Database = db
        self.ui = ExtendedUIProductsFrame()
        self.ui.setupUi(self)

        self.table_data = self.db.select_temp_table_rows()
        self.table_model = TableModel(self.table_data, self.db)
        self.ui.products_temp_table.setModel(self.table_model)
        self.ui.products_temp_table.horizontalHeader().hideSection(0)

        # Создаем делегат с элементами для QComboBox
        self.items = self.db.select_products()
        # print(f'QComboBox items = {self.items}')
        self.delegate = ComboBoxDelegate(self.items, self.ui.products_temp_table)

        # Устанавливаем делегат только для первого столбца
        self.ui.products_temp_table.setItemDelegateForColumn(1, self.delegate)

        self.ui.add_product_button.clicked.connect(self.add_button_click_slot)
        self.ui.del_product_button.clicked.connect(self.delete_selected_row_slot)
        self.ui.products_temp_table.customContextMenuRequested.connect(self.delete_by_right_click_slot)
        self.ui.products_temp_table.clicked.connect(self.choose_fist_cell_click_slot)
        self.ui.clear_product_button.clicked.connect(self.delete_all_rows_slot)
        self.ui.back_button.clicked.connect(self.back_button_slot)
        self.ui.products_db_button.clicked.connect(self.products_db_button_slot)

    @Slot()
    def add_button_click_slot(self):
        last_id = self.db.select_last_id_temp_table()
        print(f'last_id = {last_id}')
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
        selected_indexes = self.ui.products_temp_table.selectedIndexes()
        if selected_indexes:
            rows = sorted({index.row() for index in selected_indexes})
            print(f'selected rows = {rows}')
            for row in reversed(rows):
                cell_index = self.table_model.index(row, 1)
                id_from_cell = self.table_model.data(cell_index, role=Qt.UserRole)
                self.table_model.removeRows(row, 1)
                self.db.del_temp_table_row(id_from_cell)

    @Slot()
    def delete_by_right_click_slot(self, pos):
        index = self.ui.products_temp_table.indexAt(pos)
        row = index.row()
        print(f'какая строка в TableView: {row}')
        cell_index = self.table_model.index(row, 1)
        print(f'какой cell index в TableView: {cell_index}')
        id_from_cell = self.table_model.data(cell_index, role=Qt.UserRole)
        print(f'какой id_from_cell в TableView: {id_from_cell}')
        if index.isValid():
            self.table_model.removeRows(row, 1)
        self.db.del_temp_table_row(id_from_cell)


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
        # return len(self._data[0]) - 1 if self._data else 0

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            print('Ошибка метода data в table_model: невалидный индекс модели')
            sys.exit(1)
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return str(self._data[row][col])
        if role == Qt.UserRole:
            return self._data[row][0]

    def setData(self, index, value, role=Qt.EditRole):
        print(f'сработал setData: index = row:{index.row()} col:{index.column()}, value = {value}, role = {role}')
        print(f'_data = {self._data}')
        if role == Qt.EditRole:
            print(f'Значение: "{self._data[index.row()][index.column()]}" меняется на "{value}"')
            self._data[index.row()][index.column()] = value
            print(f'_data после изменений = {self._data}')
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
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.items = items

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setEditable(True)
        editor.addItems(self.items)
        editor.currentIndexChanged.connect(self.commit_and_close_editor)
        return editor

    def setEditorData(self, editor, index):
        editor.setCurrentText('')

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        print(f'value editor = {value}')
        model.setData(index, value, Qt.EditRole)

    def commit_and_close_editor(self):
        editor = self.sender()
        self.commitData.emit(editor)
        self.closeEditor.emit(editor)
