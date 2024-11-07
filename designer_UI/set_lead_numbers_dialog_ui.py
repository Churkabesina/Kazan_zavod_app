# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_lead_numbers_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_set_lead_numbers_dialog(object):
    def setupUi(self, set_lead_numbers_dialog):
        if not set_lead_numbers_dialog.objectName():
            set_lead_numbers_dialog.setObjectName(u"set_lead_numbers_dialog")
        set_lead_numbers_dialog.resize(407, 300)
        self.verticalLayout = QVBoxLayout(set_lead_numbers_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(set_lead_numbers_dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.scrollArea = QScrollArea(set_lead_numbers_dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 385, 190))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.ok_button = QPushButton(set_lead_numbers_dialog)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout_2.addWidget(self.ok_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(set_lead_numbers_dialog)

        QMetaObject.connectSlotsByName(set_lead_numbers_dialog)
    # setupUi

    def retranslateUi(self, set_lead_numbers_dialog):
        set_lead_numbers_dialog.setWindowTitle(QCoreApplication.translate("set_lead_numbers_dialog", u"Frame", None))
        self.label.setText(QCoreApplication.translate("set_lead_numbers_dialog", u"\u043d\u043e\u043c\u0435\u0440\u0430 \u0437\u0430\u044f\u0432\u043e\u043a \u2116", None))
        self.ok_button.setText(QCoreApplication.translate("set_lead_numbers_dialog", u"\u041e\u041a", None))
    # retranslateUi

