import os
from itertools import count

from PySide6.QtCore import Qt, Slot, QAbstractTableModel, QModelIndex, QSize
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QFrame, QComboBox, QStyledItemDelegate, QTableView
from UI.extended_UI import ExtendedUIDealsFrame
from backend.db_backend import Database

class DealsFrame(QFrame):
    def __init__(self, main_window, db):
        super().__init__()

        self.main_window = main_window
        self.db: Database = db
        self.ui = ExtendedUIDealsFrame()
        self.ui.setupUi(self)

        self.metal_balance_data = self.db.select_storage_table_metal_types_and_balance()
        print(self.metal_balance_data)
        self.table_data = self.db.select_deals_table_rows()
        for row in self.table_data:
            row.append(self.metal_balance_data[row[5]][row[7]])
        print(f'deals_frame_table_data = {self.table_data}')
        self.table_model = TableModel(self.table_data, self.db, self.ui.deals_table)
        self.ui.deals_table.setModel(self.table_model)
        self.ui.deals_table.horizontalHeader().hideSection(0)
        self.table_model.set_table_span()

        self.negative_delegate = NegativeNumberDelegate(self.ui.deals_table)
        self.ui.deals_table.setItemDelegateForColumn(11, self.negative_delegate)

        self.ui.back_button.clicked.connect(self.back_button_slot)


    @Slot()
    def back_button_slot(self):
        self.hide()
        self.main_window.leads_frame.show()

    def update_model_data(self):
        self.metal_balance_data = self.db.select_storage_table_metal_types_and_balance()
        self.table_data = self.db.select_deals_table_rows()
        for row in self.table_data:
            row.append(self.metal_balance_data[row[5]][row[7]])
        self.table_model.beginResetModel()
        self.table_model._data = self.table_data
        self.table_model.endResetModel()
        top_left = self.table_model.index(0, 0)
        bottom_right = self.table_model.index(self.table_model.rowCount() - 1, self.table_model.columnCount() - 1)
        self.table_model.dataChanged.emit(top_left, bottom_right),
        self.table_model.set_table_span()


class TableModel(QAbstractTableModel):
    def __init__(self, data: list[list], db: Database, table: QTableView):
        super().__init__()
        self._data = data
        self.db = db
        self.table = table

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return 12

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return
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

    def set_table_span(self):
        if self._data:
            start_index = 0
            end_index = 0
            num = self._data[0][1]
            while end_index < len(self._data):
                if self._data[end_index][1] == num:
                    end_index += 1
                else:
                    self.table.setSpan(start_index, 1, end_index - start_index, 1)
                    self.table.setSpan(start_index, 2, end_index - start_index, 1)
                    start_index = end_index
                    num = self._data[end_index][1]
            else:
                self.table.setSpan(start_index, 1, end_index - start_index, 1)
                self.table.setSpan(start_index, 2, end_index - start_index, 1)


# class TableModel(QAbstractTableModel):
#     def __init__(self, data: dict[str, dict], db: Database):
#         super().__init__()
#         self._data = data
#         self.db = db
#
#     def rowCount(self, parent=QModelIndex()):
#         return len(self._data)
#
#     def columnCount(self, parent=QModelIndex()):
#         return 12
#
#     def data(self, index, role=Qt.DisplayRole):
#         if not index.isValid():
#             return
#         row = index.row()
#         col = index.column()
#         if role == Qt.DisplayRole:
#             return str(self._data[row][col])
#         if role == Qt.UserRole:
#             return self._data[row][0]
#
#     def setData(self, index, value, role=Qt.EditRole):
#         if role == Qt.EditRole:
#             row = index.row()
#             col = index.column()
#             self._data[row][col] = value
#             self.dataChanged.emit(index, index, [Qt.EditRole])
#             return True
#         return False
#
#     def insertRows(self, row, count, parent=QModelIndex()):
#         last_id = self.db.select_last_id_temp_table()
#         self.beginInsertRows(parent, row, row + count - 1)
#         self._data.insert(row, [last_id,'','','','','','','',''])
#         self.endInsertRows()
#         return True
#
#     def removeRows(self, row, count, parent=QModelIndex()):
#         self.beginRemoveRows(parent, row, row + count - 1)
#         del self._data[row:row + count]
#         self.endRemoveRows()

class NegativeNumberDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        value = index.data()
        if float(value) < 0:
            painter.fillRect(option.rect, QBrush(QColor(178, 34, 34)))
        super().paint(painter, option, index)