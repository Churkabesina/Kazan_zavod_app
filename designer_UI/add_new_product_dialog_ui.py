# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_product_dialog.ui'
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

class Ui_add_new_product_dialog(object):
    def setupUi(self, add_new_product_dialog):
        if not add_new_product_dialog.objectName():
            add_new_product_dialog.setObjectName(u"add_new_product_dialog")
        add_new_product_dialog.resize(900, 156)
        self.verticalLayout = QVBoxLayout(add_new_product_dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(add_new_product_dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.type_metall_label = QLabel(add_new_product_dialog)
        self.type_metall_label.setObjectName(u"type_metall_label")
        self.type_metall_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.type_metall_label)

        self.label_4 = QLabel(add_new_product_dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label = QLabel(add_new_product_dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_5 = QLabel(add_new_product_dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(add_new_product_dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 50)
        self.product_name_line_edit = QLineEdit(add_new_product_dialog)
        self.product_name_line_edit.setObjectName(u"product_name_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_name_line_edit.sizePolicy().hasHeightForWidth())
        self.product_name_line_edit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.product_name_line_edit)

        self.type_metall_combo_box = QComboBox(add_new_product_dialog)
        self.type_metall_combo_box.setObjectName(u"type_metall_combo_box")
        sizePolicy.setHeightForWidth(self.type_metall_combo_box.sizePolicy().hasHeightForWidth())
        self.type_metall_combo_box.setSizePolicy(sizePolicy)
        self.type_metall_combo_box.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.type_metall_combo_box)

        self.mark_steel_line_edit = QLineEdit(add_new_product_dialog)
        self.mark_steel_line_edit.setObjectName(u"mark_steel_line_edit")
        sizePolicy.setHeightForWidth(self.mark_steel_line_edit.sizePolicy().hasHeightForWidth())
        self.mark_steel_line_edit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.mark_steel_line_edit)

        self.diamiter_combo_box = QComboBox(add_new_product_dialog)
        self.diamiter_combo_box.setObjectName(u"diamiter_combo_box")
        sizePolicy.setHeightForWidth(self.diamiter_combo_box.sizePolicy().hasHeightForWidth())
        self.diamiter_combo_box.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.diamiter_combo_box)

        self.lenght_line_edit = QLineEdit(add_new_product_dialog)
        self.lenght_line_edit.setObjectName(u"lenght_line_edit")
        sizePolicy.setHeightForWidth(self.lenght_line_edit.sizePolicy().hasHeightForWidth())
        self.lenght_line_edit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lenght_line_edit)

        self.choose_draw_button = QPushButton(add_new_product_dialog)
        self.choose_draw_button.setObjectName(u"choose_draw_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.choose_draw_button.sizePolicy().hasHeightForWidth())
        self.choose_draw_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.choose_draw_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.ok_button = QPushButton(add_new_product_dialog)
        self.ok_button.setObjectName(u"ok_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.ok_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(add_new_product_dialog)

        QMetaObject.connectSlotsByName(add_new_product_dialog)
    # setupUi

    def retranslateUi(self, add_new_product_dialog):
        add_new_product_dialog.setWindowTitle(QCoreApplication.translate("add_new_product_dialog", u"Frame", None))
        self.label_2.setText(QCoreApplication.translate("add_new_product_dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.type_metall_label.setText(QCoreApplication.translate("add_new_product_dialog", u"\u0422\u0438\u043f \u043c\u0435\u0442\u0430\u043b\u043b\u0430", None))
        self.label_4.setText(QCoreApplication.translate("add_new_product_dialog", u"\u043c\u0430\u0440\u043a\u0430 \u0441\u0442\u0430\u043b\u0438", None))
        self.label.setText(QCoreApplication.translate("add_new_product_dialog", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440, \u043c\u043c", None))
        self.label_5.setText(QCoreApplication.translate("add_new_product_dialog", u"\u0414\u043b\u0438\u043d\u0430, \u043c\u043c", None))
        self.label_6.setText(QCoreApplication.translate("add_new_product_dialog", u"\u0427\u0435\u0440\u0442\u0435\u0436", None))
        self.choose_draw_button.setText("")
        self.ok_button.setText(QCoreApplication.translate("add_new_product_dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

