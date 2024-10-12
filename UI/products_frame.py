from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QStringListModel
from PySide6.QtWidgets import QFrame, QHeaderView, QComboBox, QCompleter
from designer_UI.products_frame_ui import Ui_products_frame


class ProductsFrame(QFrame):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.ui = Ui_products_frame()
        self.ui.setupUi(self)

        self.table_data = [['ASDDDDDDDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS',2,3,4,5,6,7,8]]

        self.table_model = TableModel(self.table_data)
        self.ui.products_temp_table.setModel(self.table_model)

        # отключение названий строк и стобцов в TableView
        self.ui.products_temp_table.verticalHeader().setVisible(False)
        self.ui.products_temp_table.horizontalHeader().setVisible(False)

        self.ui.products_temp_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.items = ['', '321', 'AAAAAA', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC']
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(self.items)
        self.ui.products_temp_table.setIndexWidget(self.table_model.index(0, 0), self.my_combo_box)

        # Способ 2: Динамическая ширина
        width = self.my_combo_box.view().sizeHintForColumn(0) + self.my_combo_box.view().verticalScrollBar().sizeHint().width()
        self.my_combo_box.view().setMinimumWidth(width)

        # Создаем модель для QCompleter
        self.completer_model = QStringListModel(self.items)

        # Создаем QCompleter и связываем его с моделью
        self.completer = QCompleter(self.completer_model, self)

        # Настраиваем чувствительность к регистру (опционально)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        # Устанавливаем completer для combobox
        self.my_combo_box.setCompleter(self.completer)

        self.my_combo_box.setEditable(True)

        self.my_combo_box.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.my_combo_box.completer().setCompletionMode(QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        self.my_combo_box.completer().setFilterMode(QtCore.Qt.MatchFlag.MatchContains)


class TableModel(QAbstractTableModel):
    def __init__(self, data):
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
