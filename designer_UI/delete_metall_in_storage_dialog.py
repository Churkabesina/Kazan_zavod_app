# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_metall_in_storage_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(580, 150)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.type_metall_label = QLabel(Frame)
        self.type_metall_label.setObjectName(u"type_metall_label")
        self.type_metall_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.type_metall_label)

        self.balance_kg_label = QLabel(Frame)
        self.balance_kg_label.setObjectName(u"balance_kg_label")
        self.balance_kg_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.balance_kg_label)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 50)
        self.type_metall_combo_box = QComboBox(Frame)
        self.type_metall_combo_box.setObjectName(u"type_metall_combo_box")

        self.horizontalLayout.addWidget(self.type_metall_combo_box)

        self.balance_double_spin_box = QDoubleSpinBox(Frame)
        self.balance_double_spin_box.setObjectName(u"balance_double_spin_box")

        self.horizontalLayout.addWidget(self.balance_double_spin_box)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ok_button = QPushButton(Frame)
        self.ok_button.setObjectName(u"ok_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.ok_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.type_metall_label.setText(QCoreApplication.translate("Frame", u"\u0412\u0438\u0434 \u043c\u0435\u0442\u0430\u043b\u043b\u0430", None))
        self.balance_kg_label.setText(QCoreApplication.translate("Frame", u"\u0420\u0430\u0441\u0445\u043e\u0434, \u043a\u0433 | \u0448\u0442", None))
        self.ok_button.setText(QCoreApplication.translate("Frame", u"\u041e\u041a", None))
    # retranslateUi

