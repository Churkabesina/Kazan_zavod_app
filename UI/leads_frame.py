from PySide6.QtWidgets import QFrame
from designer_UI.leads_frame_ui import Ui_leads_frame


class LeadsFrame(QFrame):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.ui = Ui_leads_frame()
        self.ui.setupUi(self)

        self.ui.products_button.clicked.connect(self.open_products_frame_button_slot)
        self.ui.storage_button.clicked.connect(self.open_storage_frame_button_slot)
        self.ui.deal_button.clicked.connect(self.open_deals_frame_button_slot)

    def open_products_frame_button_slot(self):
        self.hide()
        self.main_window.products_frame.show()
    
    def open_storage_frame_button_slot(self):
        self.hide()
        self.main_window.storage_frame.show()

    def open_deals_frame_button_slot(self):
        self.hide()
        self.main_window.deals_frame.show()