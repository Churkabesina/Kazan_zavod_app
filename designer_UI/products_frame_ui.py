# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'products_frame.ui'
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

class Ui_products_frame(object):
    def setupUi(self, products_frame):
        if not products_frame.objectName():
            products_frame.setObjectName(u"products_frame")
        products_frame.resize(1354, 735)
        self.verticalLayout_2 = QVBoxLayout(products_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_layout = QVBoxLayout()
        self.frame_layout.setSpacing(0)
        self.frame_layout.setObjectName(u"frame_layout")
        self.frame_layout.setContentsMargins(-1, 0, -1, 0)
        self.back_and_name_layout = QHBoxLayout()
        self.back_and_name_layout.setSpacing(0)
        self.back_and_name_layout.setObjectName(u"back_and_name_layout")
        self.back_button = QPushButton(products_frame)
        self.back_button.setObjectName(u"back_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)

        self.back_and_name_layout.addWidget(self.back_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.back_and_name_layout.addItem(self.horizontalSpacer)

        self.frame_name_label = QLabel(products_frame)
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
        self.product_label = QLabel(products_frame)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.product_label)

        self.count_product_label = QLabel(products_frame)
        self.count_product_label.setObjectName(u"count_product_label")
        self.count_product_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.count_product_label)

        self.type_metall_label = QLabel(products_frame)
        self.type_metall_label.setObjectName(u"type_metall_label")
        self.type_metall_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.type_metall_label)

        self.steel_mark_label = QLabel(products_frame)
        self.steel_mark_label.setObjectName(u"steel_mark_label")
        self.steel_mark_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.steel_mark_label)

        self.diameter_label = QLabel(products_frame)
        self.diameter_label.setObjectName(u"diameter_label")
        self.diameter_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.diameter_label)

        self.lenght_label = QLabel(products_frame)
        self.lenght_label.setObjectName(u"lenght_label")
        self.lenght_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.lenght_label)

        self.weight_label = QLabel(products_frame)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.weight_label)

        self.draw_label = QLabel(products_frame)
        self.draw_label.setObjectName(u"draw_label")
        self.draw_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.draw_label)

        self.labels_layout.setStretch(0, 2)
        self.labels_layout.setStretch(1, 2)
        self.labels_layout.setStretch(2, 2)
        self.labels_layout.setStretch(3, 2)
        self.labels_layout.setStretch(4, 2)
        self.labels_layout.setStretch(5, 2)
        self.labels_layout.setStretch(6, 2)
        self.labels_layout.setStretch(7, 2)

        self.frame_layout.addLayout(self.labels_layout)

        self.scrollArea = QScrollArea(products_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1350, 511))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.frame_layout.addWidget(self.scrollArea)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(0)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.add_product_frame_button = QPushButton(products_frame)
        self.add_product_frame_button.setObjectName(u"add_product_frame_button")
        sizePolicy.setHeightForWidth(self.add_product_frame_button.sizePolicy().hasHeightForWidth())
        self.add_product_frame_button.setSizePolicy(sizePolicy)

        self.buttons_layout.addWidget(self.add_product_frame_button)

        self.clear_product_frames_button = QPushButton(products_frame)
        self.clear_product_frames_button.setObjectName(u"clear_product_frames_button")
        sizePolicy.setHeightForWidth(self.clear_product_frames_button.sizePolicy().hasHeightForWidth())
        self.clear_product_frames_button.setSizePolicy(sizePolicy)

        self.buttons_layout.addWidget(self.clear_product_frames_button)

        self.products_db_button = QPushButton(products_frame)
        self.products_db_button.setObjectName(u"products_db_button")
        sizePolicy.setHeightForWidth(self.products_db_button.sizePolicy().hasHeightForWidth())
        self.products_db_button.setSizePolicy(sizePolicy)

        self.buttons_layout.addWidget(self.products_db_button)

        self.buttons_layout.setStretch(0, 3)
        self.buttons_layout.setStretch(1, 3)
        self.buttons_layout.setStretch(2, 3)

        self.frame_layout.addLayout(self.buttons_layout)

        self.pdf_layout = QHBoxLayout()
        self.pdf_layout.setSpacing(0)
        self.pdf_layout.setObjectName(u"pdf_layout")
        self.pdf_products_button = QPushButton(products_frame)
        self.pdf_products_button.setObjectName(u"pdf_products_button")
        sizePolicy.setHeightForWidth(self.pdf_products_button.sizePolicy().hasHeightForWidth())
        self.pdf_products_button.setSizePolicy(sizePolicy)
        self.pdf_products_button.setMinimumSize(QSize(75, 0))
        self.pdf_products_button.setMaximumSize(QSize(16777215, 100))

        self.pdf_layout.addWidget(self.pdf_products_button)

        self.pdf_layout.setStretch(0, 6)

        self.frame_layout.addLayout(self.pdf_layout)

        self.frame_layout.setStretch(0, 1)
        self.frame_layout.setStretch(1, 1)
        self.frame_layout.setStretch(2, 14)
        self.frame_layout.setStretch(3, 2)
        self.frame_layout.setStretch(4, 2)

        self.verticalLayout_2.addLayout(self.frame_layout)


        self.retranslateUi(products_frame)

        QMetaObject.connectSlotsByName(products_frame)
    # setupUi

    def retranslateUi(self, products_frame):
        products_frame.setWindowTitle(QCoreApplication.translate("products_frame", u"Frame", None))
        self.back_button.setText(QCoreApplication.translate("products_frame", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.frame_name_label.setText(QCoreApplication.translate("products_frame", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f", None))
        self.product_label.setText(QCoreApplication.translate("products_frame", u"\u041f\u0420\u041e\u0414\u0423\u041a\u0426\u0418\u042f", None))
        self.count_product_label.setText(QCoreApplication.translate("products_frame", u"\u041a\u041e\u041b-\u0412\u041e \u0418\u0417\u0414\u0415\u041b\u0418\u0419", None))
        self.type_metall_label.setText(QCoreApplication.translate("products_frame", u"\u0422\u0418\u041f \u041c\u0415\u0422\u0410\u041b\u041b\u0410", None))
        self.steel_mark_label.setText(QCoreApplication.translate("products_frame", u"\u041c\u0410\u0420\u041a\u0410 \u0421\u0422\u0410\u041b\u0418", None))
        self.diameter_label.setText(QCoreApplication.translate("products_frame", u"\u0414\u0418\u0410\u041c\u0415\u0422\u0420, \u041c\u041c", None))
        self.lenght_label.setText(QCoreApplication.translate("products_frame", u"\u0414\u041b\u0418\u041d\u0410, \u041c\u041c", None))
        self.weight_label.setText(QCoreApplication.translate("products_frame", u"\u041e\u0411\u0429\u0418\u0419 \u0412\u0415\u0421(\u041a\u0413)", None))
        self.draw_label.setText(QCoreApplication.translate("products_frame", u"\u0427\u0415\u0420\u0422\u0415\u0416", None))
        self.add_product_frame_button.setText(QCoreApplication.translate("products_frame", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.clear_product_frames_button.setText(QCoreApplication.translate("products_frame", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u0441\u0435", None))
        self.products_db_button.setText(QCoreApplication.translate("products_frame", u"\u0411\u0430\u0437\u0430 \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438", None))
        self.pdf_products_button.setText(QCoreApplication.translate("products_frame", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044e \u0432 PDF", None))
    # retranslateUi

