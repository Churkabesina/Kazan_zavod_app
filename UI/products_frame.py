from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QStringListModel, Slot
from PySide6.QtWidgets import QFrame, QHeaderView, QComboBox, QCompleter, QStyledItemDelegate, QItemDelegate
from designer_UI.products_frame_ui import Ui_products_frame


class ProductsFrame(QFrame):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.ui = Ui_products_frame()
        self.ui.setupUi(self)

        self.table_data = [['','','','','','','','']]

        self.table_model = TableModel(self.table_data)
        self.ui.products_temp_table.setModel(self.table_model)

        # отключение названий строк и стобцов в TableView
        self.ui.products_temp_table.verticalHeader().setVisible(False)
        self.ui.products_temp_table.horizontalHeader().setVisible(False)
        # растяжение на все пространство по горизонту
        self.ui.products_temp_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Создаем делегат с элементами для QComboBox
        self.items = ["Вариант 1", "Вариант 2", "Вариант 3"]
        self.delegate = ComboBoxDelegate(self.items, self.ui.products_temp_table)

        # Устанавливаем делегат только для первого столбца
        self.ui.products_temp_table.setItemDelegateForColumn(0, self.delegate)

        self.ui.add_product_button.clicked.connect(self.add_button_click_slot)

    @Slot()
    def add_button_click_slot(self):
        self.table_model.insertRows(self.table_model.rowCount(), 1)

# переписать в "попроще" rowcount и т.тд
class TableModel(QAbstractTableModel):
    def __init__(self, data: list[list]):
        super().__init__()
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0]) if self._data else 0

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self._data[row][col])

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [Qt.EditRole])
            return True
        return False

    def flags(self, index):
        if index.column() == 0 or index.column() == 1:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def insertRows(self, row, count, parent=QModelIndex()):
        self.beginInsertRows(parent, row, row + count - 1)  # Уведомляем о начале добавления

        # Добавляем данные для новой строки в self._data
        self._data.insert(row, ['','','','','','','',''])

        self.endInsertRows()  # Уведомляем об окончании добавления
        self.layoutChanged.emit()  # Уведомляем об изменении структуры
        return True


class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.items = items

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setEditable(True)
        editor.addItems(self.items)
        editor.currentIndexChanged.connect(self.commitAndCloseEditor)
        return editor

    def setEditorData(self, editor, index):
        editor.setCurrentText('')
        # value = index.model().data(index, Qt.EditRole)
        # if value in self.items:
        #     editor.setCurrentIndex(self.items.index(value))
        # else:
        #     editor.setCurrentText(value)

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, value, Qt.EditRole)

    def commitAndCloseEditor(self):
        editor = self.sender()
        self.commitData.emit(editor)
        self.closeEditor.emit(editor)