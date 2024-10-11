import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from designer_UI.main_window_ui import Ui_main_window
from UI.products_frame import ProductsFrame
from UI.leads_frame import LeadsFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.leads_frame = LeadsFrame(self)
        self.products_frame = ProductsFrame(self)


        self.ui.centralwidget.layout().addWidget(self.products_frame)
        self.ui.centralwidget.layout().addWidget(self.leads_frame)

        self.products_frame.hide()
        self.leads_frame.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())