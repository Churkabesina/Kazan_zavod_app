import sys

from PySide6.QtCore import QFile

from backend.backend import load_cfg, create_draws_folder, create_storage_excel_folder, create_temp_products_pdf_folder
from backend.db_backend import Database

from PySide6.QtWidgets import QApplication, QMainWindow

from designer_UI.main_window_ui import Ui_main_window
from UI.products_frame import ProductsFrame
from UI.leads_frame import LeadsFrame
from UI.storage_frame import StorageFrame
from UI.products_db_frame import ProductsDBFrame
from UI.deals_frame import DealsFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.leads_frame = LeadsFrame(self, DB)
        self.products_frame = ProductsFrame(self, DB, TEMP_PRODUCTS_PDF_FOLDER, DRAWS_FOLDER)
        self.storage_frame = StorageFrame(self, DB, STORAGE_EXCEL_FOLDER)
        self.products_db_frame = ProductsDBFrame(self, DB, DRAWS_FOLDER)
        self.deals_frame = DealsFrame(self, DB)

        self.ui.centralwidget.layout().addWidget(self.storage_frame)
        self.ui.centralwidget.layout().addWidget(self.products_frame)
        self.ui.centralwidget.layout().addWidget(self.products_db_frame)
        self.ui.centralwidget.layout().addWidget(self.deals_frame)
        self.ui.centralwidget.layout().addWidget(self.leads_frame)

        self.storage_frame.hide()
        self.products_frame.hide()
        self.products_db_frame.hide()
        self.deals_frame.hide()
        self.leads_frame.show()


if __name__ == "__main__":
    cfg = load_cfg()
    DRAWS_FOLDER = create_draws_folder(cfg['PATHS']['draws_folder'])
    STORAGE_EXCEL_FOLDER = create_storage_excel_folder(cfg['PATHS']['storage_excel_export_path'])
    TEMP_PRODUCTS_PDF_FOLDER = create_temp_products_pdf_folder(cfg['PATHS']['export_pdf_folder'])
    app = QApplication(sys.argv)

    # unreal_stylesheet.setup()
    qss_file = QFile("style.qss")
    qss_file.open(QFile.OpenMode.ReadOnly | QFile.OpenMode.Text)
    app.setStyleSheet(qss_file.readAll().data().decode())
    qss_file.close()
    # app.setStyleSheet('''QFrame {background-color: gray;} QTableView {background-color: white;} QPushButton {background-color: white;} QListView {background-color: white;} QMessageBox {background-color: white;}''')

    DB = Database(cfg['DB']['db_name'], cfg['DB']['db_folder'])
    DB.create_db()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())