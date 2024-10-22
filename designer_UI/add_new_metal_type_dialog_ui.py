# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_metal_type_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_add_new_metal_type_dialog(object):
    def setupUi(self, add_new_metal_type_dialog):
        if not add_new_metal_type_dialog.objectName():
            add_new_metal_type_dialog.setObjectName(u"add_new_metal_type_dialog")
        add_new_metal_type_dialog.resize(580, 150)
        self.verticalLayout = QVBoxLayout(add_new_metal_type_dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.type_metall_label = QLabel(add_new_metal_type_dialog)
        self.type_metall_label.setObjectName(u"type_metall_label")
        self.type_metall_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.type_metall_label)

        self.label = QLabel(add_new_metal_type_dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 50)
        self.type_metall_combo_box = QComboBox(add_new_metal_type_dialog)
        self.type_metall_combo_box.setObjectName(u"type_metall_combo_box")
        self.type_metall_combo_box.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.type_metall_combo_box)

        self.lineEdit = QLineEdit(add_new_metal_type_dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.ok_button_2 = QPushButton(add_new_metal_type_dialog)
        self.ok_button_2.setObjectName(u"ok_button_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ok_button_2.sizePolicy().hasHeightForWidth())
        self.ok_button_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.ok_button_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(add_new_metal_type_dialog)

        QMetaObject.connectSlotsByName(add_new_metal_type_dialog)
    # setupUi

    def retranslateUi(self, add_new_metal_type_dialog):
        add_new_metal_type_dialog.setWindowTitle(QCoreApplication.translate("add_new_metal_type_dialog", u"Frame", None))
        self.type_metall_label.setText(QCoreApplication.translate("add_new_metal_type_dialog", u"\u0412\u0438\u0434 \u043c\u0435\u0442\u0430\u043b\u043b\u0430", None))
        self.label.setText(QCoreApplication.translate("add_new_metal_type_dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440, \u043c\u043c", None))
        self.ok_button_2.setText(QCoreApplication.translate("add_new_metal_type_dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

