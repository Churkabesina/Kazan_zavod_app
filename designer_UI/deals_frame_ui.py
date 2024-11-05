# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deals_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_deals_frame(object):
    def setupUi(self, deals_frame):
        if not deals_frame.objectName():
            deals_frame.setObjectName(u"deals_frame")
        deals_frame.resize(1360, 735)
        self.verticalLayout = QVBoxLayout(deals_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_layout = QVBoxLayout()
        self.frame_layout.setSpacing(6)
        self.frame_layout.setObjectName(u"frame_layout")
        self.frame_layout.setContentsMargins(-1, 0, -1, 0)
        self.back_and_name_layout = QHBoxLayout()
        self.back_and_name_layout.setSpacing(0)
        self.back_and_name_layout.setObjectName(u"back_and_name_layout")
        self.back_button = QPushButton(deals_frame)
        self.back_button.setObjectName(u"back_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)

        self.back_and_name_layout.addWidget(self.back_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.back_and_name_layout.addItem(self.horizontalSpacer)

        self.frame_name_label = QLabel(deals_frame)
        self.frame_name_label.setObjectName(u"frame_name_label")
        self.frame_name_label.setAlignment(Qt.AlignCenter)

        self.back_and_name_layout.addWidget(self.frame_name_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.back_and_name_layout.addItem(self.horizontalSpacer_2)

        self.back_and_name_layout.setStretch(0, 1)
        self.back_and_name_layout.setStretch(1, 1)
        self.back_and_name_layout.setStretch(2, 6)
        self.back_and_name_layout.setStretch(3, 2)

        self.frame_layout.addLayout(self.back_and_name_layout)

        self.labels_layout = QHBoxLayout()
        self.labels_layout.setObjectName(u"labels_layout")
        self.num_label = QLabel(deals_frame)
        self.num_label.setObjectName(u"num_label")
        self.num_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.num_label)

        self.date_label = QLabel(deals_frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.date_label)

        self.product_label = QLabel(deals_frame)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.product_label)

        self.count_product_label = QLabel(deals_frame)
        self.count_product_label.setObjectName(u"count_product_label")
        self.count_product_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.count_product_label)

        self.type_metall_label = QLabel(deals_frame)
        self.type_metall_label.setObjectName(u"type_metall_label")
        self.type_metall_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.type_metall_label)

        self.steel_mark_label = QLabel(deals_frame)
        self.steel_mark_label.setObjectName(u"steel_mark_label")
        self.steel_mark_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.steel_mark_label)

        self.diameter_label = QLabel(deals_frame)
        self.diameter_label.setObjectName(u"diameter_label")
        self.diameter_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.diameter_label)

        self.lenght_label = QLabel(deals_frame)
        self.lenght_label.setObjectName(u"lenght_label")
        self.lenght_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.lenght_label)

        self.weight_label = QLabel(deals_frame)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.weight_label)

        self.draw_label = QLabel(deals_frame)
        self.draw_label.setObjectName(u"draw_label")
        self.draw_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.draw_label)

        self.balance_metal_label = QLabel(deals_frame)
        self.balance_metal_label.setObjectName(u"balance_metal_label")

        self.labels_layout.addWidget(self.balance_metal_label)


        self.frame_layout.addLayout(self.labels_layout)

        self.deals_table = QTableView(deals_frame)
        self.deals_table.setObjectName(u"deals_table")

        self.frame_layout.addWidget(self.deals_table)

        self.group_and_unload_layout = QHBoxLayout()
        self.group_and_unload_layout.setSpacing(0)
        self.group_and_unload_layout.setObjectName(u"group_and_unload_layout")
        self.group_deals_button = QPushButton(deals_frame)
        self.group_deals_button.setObjectName(u"group_deals_button")
        sizePolicy.setHeightForWidth(self.group_deals_button.sizePolicy().hasHeightForWidth())
        self.group_deals_button.setSizePolicy(sizePolicy)
        self.group_deals_button.setMinimumSize(QSize(75, 0))
        self.group_deals_button.setMaximumSize(QSize(16777215, 100))

        self.group_and_unload_layout.addWidget(self.group_deals_button)

        self.export_excel_deals_button = QPushButton(deals_frame)
        self.export_excel_deals_button.setObjectName(u"export_excel_deals_button")
        sizePolicy.setHeightForWidth(self.export_excel_deals_button.sizePolicy().hasHeightForWidth())
        self.export_excel_deals_button.setSizePolicy(sizePolicy)

        self.group_and_unload_layout.addWidget(self.export_excel_deals_button)

        self.group_and_unload_layout.setStretch(0, 5)
        self.group_and_unload_layout.setStretch(1, 5)

        self.frame_layout.addLayout(self.group_and_unload_layout)

        self.frame_layout.setStretch(0, 1)
        self.frame_layout.setStretch(1, 1)
        self.frame_layout.setStretch(2, 14)
        self.frame_layout.setStretch(3, 2)

        self.verticalLayout.addLayout(self.frame_layout)


        self.retranslateUi(deals_frame)

        QMetaObject.connectSlotsByName(deals_frame)
    # setupUi

    def retranslateUi(self, deals_frame):
        deals_frame.setWindowTitle(QCoreApplication.translate("deals_frame", u"Frame", None))
        self.back_button.setText(QCoreApplication.translate("deals_frame", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.frame_name_label.setText(QCoreApplication.translate("deals_frame", u"\u0421\u0447\u0435\u0442\u0430", None))
        self.num_label.setText(QCoreApplication.translate("deals_frame", u"\u2116", None))
        self.date_label.setText(QCoreApplication.translate("deals_frame", u"\u0414\u0410\u0422\u0410", None))
        self.product_label.setText(QCoreApplication.translate("deals_frame", u"\u041f\u0420\u041e\u0414\u0423\u041a\u0426\u0418\u042f", None))
        self.count_product_label.setText(QCoreApplication.translate("deals_frame", u"\u041a\u041e\u041b-\u0412\u041e \u0418\u0417\u0414\u0415\u041b\u0418\u0419", None))
        self.type_metall_label.setText(QCoreApplication.translate("deals_frame", u"\u0422\u0418\u041f \u041c\u0415\u0422\u0410\u041b\u041b\u0410", None))
        self.steel_mark_label.setText(QCoreApplication.translate("deals_frame", u"\u041c\u0410\u0420\u041a\u0410 \u0421\u0422\u0410\u041b\u0418", None))
        self.diameter_label.setText(QCoreApplication.translate("deals_frame", u"\u0414\u0418\u0410\u041c\u0415\u0422\u0420, \u041c\u041c", None))
        self.lenght_label.setText(QCoreApplication.translate("deals_frame", u"\u0414\u041b\u0418\u041d\u0410, \u041c\u041c", None))
        self.weight_label.setText(QCoreApplication.translate("deals_frame", u"\u041e\u0411\u0429\u0418\u0419 \u0412\u0415\u0421(\u041a\u0413)", None))
        self.draw_label.setText(QCoreApplication.translate("deals_frame", u"\u0427\u0415\u0420\u0422\u0415\u0416", None))
        self.balance_metal_label.setText(QCoreApplication.translate("deals_frame", u"\u041d\u0410\u041b\u0418\u0427\u0418\u0415 \u041c\u0415\u0422\u0410\u041b\u041b\u0410", None))
        self.group_deals_button.setText(QCoreApplication.translate("deals_frame", u"\u0421\u0433\u0440\u0443\u043f\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.export_excel_deals_button.setText(QCoreApplication.translate("deals_frame", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 EXCEL?", None))
    # retranslateUi

