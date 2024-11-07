# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_deal_number_dialog.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_set_deal_number_dialog(object):
    def setupUi(self, set_deal_number_dialog):
        if not set_deal_number_dialog.objectName():
            set_deal_number_dialog.setObjectName(u"set_deal_number_dialog")
        set_deal_number_dialog.resize(407, 150)
        self.verticalLayout = QVBoxLayout(set_deal_number_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(set_deal_number_dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.num_lineedit = QLineEdit(set_deal_number_dialog)
        self.num_lineedit.setObjectName(u"num_lineedit")
        self.num_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.num_lineedit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.ok_button = QPushButton(set_deal_number_dialog)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout_2.addWidget(self.ok_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(set_deal_number_dialog)

        QMetaObject.connectSlotsByName(set_deal_number_dialog)
    # setupUi

    def retranslateUi(self, set_deal_number_dialog):
        set_deal_number_dialog.setWindowTitle(QCoreApplication.translate("set_deal_number_dialog", u"Frame", None))
        self.label.setText(QCoreApplication.translate("set_deal_number_dialog", u"\u043d\u043e\u043c\u0435\u0440 \u0441\u0447\u0435\u0442\u0430 \u2116", None))
        self.num_lineedit.setText("")
        self.ok_button.setText(QCoreApplication.translate("set_deal_number_dialog", u"\u041e\u041a", None))
    # retranslateUi

