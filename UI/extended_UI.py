from designer_UI.products_db_frame_ui import Ui_products_db_frame
from designer_UI.products_frame_ui import Ui_products_frame
from designer_UI.storage_frame_ui import Ui_storage_frame
from PySide6.QtWidgets import QHeaderView
from PySide6.QtCore import Qt

class ExtendedUIProductsFrame(Ui_products_frame):
    def setupUi(self, products_frame):
        super().setupUi(products_frame)
        # отключение названий строк и стобцов в TableView
        self.products_temp_table.verticalHeader().setVisible(False)
        self.products_temp_table.horizontalHeader().setVisible(False)
        # растяжение на все пространство по горизонту
        self.products_temp_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # политика кастомного меню, нужно для удаления по нажатию на пкм
        self.products_temp_table.setContextMenuPolicy(Qt.CustomContextMenu)


class ExtendedUIStorageFrame(Ui_storage_frame):
    def setupUi(self, storage_frame):
        super().setupUi(storage_frame)
        # отключение названий строк и стобцов в TableView
        self.storage_db_table.verticalHeader().setVisible(False)
        self.storage_db_table.horizontalHeader().setVisible(False)
        # растяжение на все пространство по горизонту
        self.storage_db_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

class ExtendedUIProductsDBFrame(Ui_products_db_frame):
    def setupUi(self, storage_frame):
        super().setupUi(storage_frame)
        # отключение названий строк и стобцов в TableView
        self.products_db_table.verticalHeader().setVisible(False)
        self.products_db_table.horizontalHeader().setVisible(False)
        # растяжение на все пространство по горизонту
        self.products_db_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)