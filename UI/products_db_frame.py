import os.path
import sys

from PySide6.QtCore import Qt, Slot, QAbstractTableModel, QModelIndex, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QFrame, QDialog, QFileDialog
from UI.extended_UI import ExtendedUIProductsDBFrame
from backend.db_backend import Database
from backend.backend import copy_pdf_to_draws_folder
from designer_UI.add_new_product_dialog_ui import Ui_add_new_product_dialog


class ProductsDBFrame(QFrame):
    def __init__(self, main_window, db, draws_folder):
        super().__init__()

        self.main_window = main_window
        self.db: Database = db
        self.draws_folder = draws_folder
        self.ui = ExtendedUIProductsDBFrame()
        self.ui.setupUi(self)

        self.table_data = self.db.select_products_db_rows()
        self.table_model = TableModel(self.table_data, self.db)
        self.ui.storage_db_table.setModel(self.table_model)
        self.ui.storage_db_table.horizontalHeader().hideSection(0)

        self.add_new_product_dialog = AddNewProductDialog(self.main_window, self.db, self.table_model, self.draws_folder)

        self.ui.back_button.clicked.connect(self.back_button_slot)
        self.ui.add_product_db_button.clicked.connect(self.add_product_db_button_slot)
        self.ui.del_product_db_button.clicked.connect(self.del_product_db_button_slot)

    @Slot()
    def back_button_slot(self):
        self.hide()
        self.main_window.products_frame.show()

    @Slot()
    def add_product_db_button_slot(self):
        self.add_new_product_dialog.exec()

    @Slot()
    def del_product_db_button_slot(self):
        print('del')

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
        last_data = self.db.select_last_row_products_db()
        self.beginInsertRows(parent, row, row + count - 1)
        self._data.insert(row, last_data)
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count - 1)
        del self._data[row:row + count]
        self.endRemoveRows()

class AddNewProductDialog(QDialog):
    def __init__(self, main_window, db: Database, model: TableModel, draws_folder):
        super().__init__()

        self.main_window = main_window
        self.db = db
        self.model = model
        self.draws_folder = draws_folder
        self.chosen_draw_path = None
        self.ui = Ui_add_new_product_dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Добавить продукцию')

        self._metal_data = self.db.select_storage_table_type_metal_and_size()
        self.ui.type_metall_combo_box.addItems(list(self._metal_data.keys()))

        self.line_edit_lenght_regex = QRegularExpression(r"^\d+\.\d+$")
        self.line_edit_lenght_validator = QRegularExpressionValidator(self.line_edit_lenght_regex)
        self.ui.lenght_line_edit.setValidator(self.line_edit_lenght_validator)

        self.ui.ok_button.clicked.connect(self.ok_button_slot)
        self.ui.type_metall_combo_box.currentIndexChanged.connect(self.type_metal_combo_box_chosen)
        self.ui.choose_draw_button.clicked.connect(self.choose_draw_button_slot)

        self.ui.type_metall_combo_box.setCurrentIndex(1)

    @Slot()
    def ok_button_slot(self):
        product_name = self.ui.product_name_line_edit.text()
        type_metal = self.ui.type_metall_combo_box.currentText()
        mark_steel = self.ui.mark_steel_line_edit.text()
        if mark_steel == '':
            mark_steel = None
        diameter = self.ui.diamiter_combo_box.currentText()
        lenght = self.ui.lenght_line_edit.text()
        if lenght == '':
            lenght = None
        draw = self.ui.choose_draw_button.text()
        if draw == '':
            draw = None
        if product_name != '':
            if not self.db.check_product_exists_products_db(product_name):
                if 'гайка' not in type_metal.lower():
                    if lenght:
                        weight = self.calculate_product_weight(type_metal, diameter, float(lenght))
                        self.db.insert_product_products_db(product_name, type_metal, mark_steel, diameter, float(lenght), weight, draw)
                    else:
                        print('Для этого типа металла нужно ввести длину')
                else:
                    weight = None
                    self.db.insert_product_products_db(product_name, type_metal, mark_steel, diameter, lenght, weight, draw)
                self.model.insertRows(self.model.rowCount(), 1)
                self.main_window.products_frame.delegate.items.append(product_name)
                if draw:
                    copy_pdf_to_draws_folder(self.chosen_draw_path, os.path.abspath(self.draws_folder))
                    self.ui.choose_draw_button.setText('')
                    self.chosen_draw_path = None
                self.close()
                print('Запись добавлена!')
            else:
                print('Такой продукт уже существует')
        else:
            print('Нужно ввести название продукта')

    @Slot()
    def type_metal_combo_box_chosen(self):
        self.ui.diamiter_combo_box.clear()
        type_metal = self.ui.type_metall_combo_box.currentText()
        if 'гайка' in type_metal.lower():
            self.ui.diamiter_combo_box.setEnabled(False)
            self.ui.lenght_line_edit.setEnabled(False)
        else:
            self.ui.diamiter_combo_box.setEnabled(True)
            self.ui.lenght_line_edit.setEnabled(True)
            self.ui.diamiter_combo_box.addItems(self._metal_data[type_metal])

    @Slot()
    def choose_draw_button_slot(self):
        draws_folder = os.path.abspath(self.draws_folder)
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать чертеж", draws_folder,'*.pdf')
        self.chosen_draw_path = file_path
        if file_path:
            print(f"Выбран файл: {file_path}")
            file_name = file_path.split('/')[-1]
            print(f'file_name: {file_name}')
            self.ui.choose_draw_button.setText(file_name)
        else:
            print('Путь не выбран или какая-то ошибка')

    @staticmethod
    def calculate_product_weight(type_metal: str, diameter: str, lenght: float) -> float:
        if type_metal.lower() == 'труба':
            split_diameter = diameter.split('x')
            d = float(split_diameter[0])
            s = float(split_diameter[1])
            l = lenght
            m = round((6.16225*(d**2-(d-2*s)**2)*l/10**9) * 1000, 2)
            return m
        else:
            d = float(diameter)
            l = lenght
            m = round(6.169315*d**2*l/10**6, 2)
            return m
