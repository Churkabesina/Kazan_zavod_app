import os.path
import sys

from backend.backend import load_cfg, create_draws_folder
from backend.db_backend import Database

from PySide6.QtWidgets import QApplication, QMainWindow

from designer_UI.main_window_ui import Ui_main_window
from UI.products_frame import ProductsFrame
from UI.leads_frame import LeadsFrame
from UI.storage_frame import StorageFrame
from UI.products_db_frame import ProductsDBFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.leads_frame = LeadsFrame(self)
        self.products_frame = ProductsFrame(self, DB)
        self.storage_frame = StorageFrame(self, DB)
        self.products_db_frame = ProductsDBFrame(self, DB, DRAWS_FOLDER)
        

        self.ui.centralwidget.layout().addWidget(self.storage_frame)
        self.ui.centralwidget.layout().addWidget(self.products_frame)
        self.ui.centralwidget.layout().addWidget(self.products_db_frame)
        self.ui.centralwidget.layout().addWidget(self.leads_frame)

        self.storage_frame.hide()
        self.products_frame.hide()
        self.products_db_frame.hide()
        self.leads_frame.show()


if __name__ == "__main__":
    cfg = load_cfg()
    DRAWS_FOLDER = create_draws_folder(cfg['DRAWS']['draws_folder'])
    app = QApplication(sys.argv)
    DB = Database(cfg['DB']['db_name'], cfg['DB']['db_path'])
    DB.create_db()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())