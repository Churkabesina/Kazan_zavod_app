from PySide6.QtWidgets import QFrame
from designer_UI.products_frame_ui import Ui_products_frame


class ProductsFrame(QFrame):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.ui = Ui_products_frame()
        self.ui.setupUi(self)