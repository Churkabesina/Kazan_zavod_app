from PySide6.QtWidgets import QFrame
from designer_UI.leads_frame_ui import Ui_leads_frame


class LeadsFrame(QFrame):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.ui = Ui_leads_frame()
        self.ui.setupUi(self)

        self.ui.products_button.clicked.connect(self.blabla)


    def blabla(self):
        self.main_window.leads_frame.hide()
        self.main_window.products_frame.show()