# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leads_frame.ui'
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

class Ui_leads_frame(object):
    def setupUi(self, leads_frame):
        if not leads_frame.objectName():
            leads_frame.setObjectName(u"leads_frame")
        leads_frame.resize(1360, 735)
        self.verticalLayout_2 = QVBoxLayout(leads_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_layout = QVBoxLayout()
        self.frame_layout.setSpacing(6)
        self.frame_layout.setObjectName(u"frame_layout")
        self.frame_layout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(leads_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 12)
        self.horizontalLayout.setStretch(2, 4)

        self.frame_layout.addLayout(self.horizontalLayout)

        self.labels_layout = QHBoxLayout()
        self.labels_layout.setObjectName(u"labels_layout")
        self.num_label = QLabel(leads_frame)
        self.num_label.setObjectName(u"num_label")
        self.num_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.num_label)

        self.date_label = QLabel(leads_frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.date_label)

        self.product_label = QLabel(leads_frame)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.product_label)

        self.count_label = QLabel(leads_frame)
        self.count_label.setObjectName(u"count_label")
        self.count_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.count_label)

        self.type_metal_label = QLabel(leads_frame)
        self.type_metal_label.setObjectName(u"type_metal_label")
        self.type_metal_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.type_metal_label)

        self.mark_steel_label = QLabel(leads_frame)
        self.mark_steel_label.setObjectName(u"mark_steel_label")
        self.mark_steel_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.mark_steel_label)

        self.diameter_label = QLabel(leads_frame)
        self.diameter_label.setObjectName(u"diameter_label")
        self.diameter_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.diameter_label)

        self.lenght_label = QLabel(leads_frame)
        self.lenght_label.setObjectName(u"lenght_label")
        self.lenght_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.lenght_label)

        self.total_weight_label = QLabel(leads_frame)
        self.total_weight_label.setObjectName(u"total_weight_label")
        self.total_weight_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.total_weight_label)

        self.draw_label = QLabel(leads_frame)
        self.draw_label.setObjectName(u"draw_label")
        self.draw_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.draw_label)

        self.metal_balance_label = QLabel(leads_frame)
        self.metal_balance_label.setObjectName(u"metal_balance_label")
        self.metal_balance_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.metal_balance_label)


        self.frame_layout.addLayout(self.labels_layout)

        self.leads_table = QTableView(leads_frame)
        self.leads_table.setObjectName(u"leads_table")

        self.frame_layout.addWidget(self.leads_table)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.storage_button = QPushButton(leads_frame)
        self.storage_button.setObjectName(u"storage_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storage_button.sizePolicy().hasHeightForWidth())
        self.storage_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.storage_button)

        self.products_button = QPushButton(leads_frame)
        self.products_button.setObjectName(u"products_button")
        sizePolicy.setHeightForWidth(self.products_button.sizePolicy().hasHeightForWidth())
        self.products_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.products_button)

        self.deal_button = QPushButton(leads_frame)
        self.deal_button.setObjectName(u"deal_button")
        sizePolicy.setHeightForWidth(self.deal_button.sizePolicy().hasHeightForWidth())
        self.deal_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.deal_button)


        self.frame_layout.addLayout(self.horizontalLayout_2)

        self.pdf_layout = QHBoxLayout()
        self.pdf_layout.setSpacing(0)
        self.pdf_layout.setObjectName(u"pdf_layout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.pdf_layout.addItem(self.horizontalSpacer_3)

        self.pdf_unload_button = QPushButton(leads_frame)
        self.pdf_unload_button.setObjectName(u"pdf_unload_button")
        sizePolicy.setHeightForWidth(self.pdf_unload_button.sizePolicy().hasHeightForWidth())
        self.pdf_unload_button.setSizePolicy(sizePolicy)
        self.pdf_unload_button.setMinimumSize(QSize(75, 0))
        self.pdf_unload_button.setMaximumSize(QSize(500, 100))
        self.pdf_unload_button.setIconSize(QSize(16, 16))

        self.pdf_layout.addWidget(self.pdf_unload_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.pdf_layout.addItem(self.horizontalSpacer_4)

        self.pdf_layout.setStretch(0, 2)
        self.pdf_layout.setStretch(1, 6)
        self.pdf_layout.setStretch(2, 2)

        self.frame_layout.addLayout(self.pdf_layout)

        self.frame_layout.setStretch(0, 1)
        self.frame_layout.setStretch(1, 1)
        self.frame_layout.setStretch(2, 14)
        self.frame_layout.setStretch(3, 3)
        self.frame_layout.setStretch(4, 1)

        self.verticalLayout_2.addLayout(self.frame_layout)


        self.retranslateUi(leads_frame)

        QMetaObject.connectSlotsByName(leads_frame)
    # setupUi

    def retranslateUi(self, leads_frame):
        leads_frame.setWindowTitle(QCoreApplication.translate("leads_frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("leads_frame", u"\u0417\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u0438\u0437\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.num_label.setText(QCoreApplication.translate("leads_frame", u"\u2116", None))
        self.date_label.setText(QCoreApplication.translate("leads_frame", u"\u0414\u0410\u0422\u0410", None))
        self.product_label.setText(QCoreApplication.translate("leads_frame", u"\u041f\u0420\u041e\u0414\u0423\u041a\u0426\u0418\u042f", None))
        self.count_label.setText(QCoreApplication.translate("leads_frame", u"\u041a\u041e\u041b-\u0412\u041e \u0418\u0417\u0414\u0415\u041b\u0418\u0419", None))
        self.type_metal_label.setText(QCoreApplication.translate("leads_frame", u"\u0422\u0418\u041f \u041c\u0415\u0422\u0410\u041b\u041b\u0410", None))
        self.mark_steel_label.setText(QCoreApplication.translate("leads_frame", u"\u041c\u0410\u0420\u041a\u0410 \u0421\u0422\u0410\u041b\u0418", None))
        self.diameter_label.setText(QCoreApplication.translate("leads_frame", u"\u0414\u0418\u0410\u041c\u0415\u0422\u0420, \u041c\u041c", None))
        self.lenght_label.setText(QCoreApplication.translate("leads_frame", u"\u0414\u041b\u0418\u041d\u0410, \u041c\u041c", None))
        self.total_weight_label.setText(QCoreApplication.translate("leads_frame", u"\u041e\u0411\u0429\u0418\u0419 \u0412\u0415\u0421(\u041a\u0413)", None))
        self.draw_label.setText(QCoreApplication.translate("leads_frame", u"\u0427\u0415\u0420\u0422\u0415\u0416", None))
        self.metal_balance_label.setText(QCoreApplication.translate("leads_frame", u"\u041d\u0410\u041b\u0418\u0427\u0418\u0415 \u041c\u0415\u0422\u0410\u041b\u041b\u0410", None))
        self.storage_button.setText(QCoreApplication.translate("leads_frame", u"\u0421\u043a\u043b\u0430\u0434", None))
        self.products_button.setText(QCoreApplication.translate("leads_frame", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f", None))
        self.deal_button.setText(QCoreApplication.translate("leads_frame", u"\u0421\u0447\u0435\u0442\u0430", None))
        self.pdf_unload_button.setText(QCoreApplication.translate("leads_frame", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0438 \u0432 PDF", None))
    # retranslateUi

