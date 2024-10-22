import sys

from PySide6.QtCore import Qt, Slot, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import QFrame
from UI.extended_UI import ExtendedUIProductsDBFrame
from backend.db_backend import Database


class ProductsDBFrame(QFrame):
    def __init__(self, main_window, db):
        super().__init__()

        self.main_window = main_window
        self.db: Database = db
        self.ui = ExtendedUIProductsDBFrame()
        self.ui.setupUi(self)

        self.table_data = self.db.select_products_db_rows()
        self.table_model = TableModel(self.table_data, self.db)
        self.ui.storage_db_table.setModel(self.table_model)
        self.ui.storage_db_table.horizontalHeader().hideSection(0)


        self.ui.back_button.clicked.connect(self.back_button_slot)

    @Slot()
    def back_button_slot(self):
        self.hide()
        self.main_window.products_frame.show()

class TableModel(QAbstractTableModel):
    def __init__(self, data: list[list], db: Database):
        super().__init__()
        self._data = data
        self.db = db

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return 8

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
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [Qt.EditRole])
            return True
        return False

    # def flags(self, index):
    #     if index.column() == 1 or index.column() == 2:
    #         return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
    #     return Qt.ItemIsEnabled | Qt.ItemIsSelectable

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