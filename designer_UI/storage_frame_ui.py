# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'storage_frame.ui'
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

class Ui_storage_frame(object):
    def setupUi(self, storage_frame):
        if not storage_frame.objectName():
            storage_frame.setObjectName(u"storage_frame")
        storage_frame.resize(1360, 735)
        self.verticalLayout = QVBoxLayout(storage_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_layout = QVBoxLayout()
        self.frame_layout.setSpacing(0)
        self.frame_layout.setObjectName(u"frame_layout")
        self.frame_layout.setContentsMargins(-1, 0, -1, 0)
        self.back_and_name_layout = QHBoxLayout()
        self.back_and_name_layout.setSpacing(0)
        self.back_and_name_layout.setObjectName(u"back_and_name_layout")
        self.back_button = QPushButton(storage_frame)
        self.back_button.setObjectName(u"back_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)

        self.back_and_name_layout.addWidget(self.back_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.back_and_name_layout.addItem(self.horizontalSpacer)

        self.frame_name_label = QLabel(storage_frame)
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
        self.labels_layout.setSpacing(0)
        self.labels_layout.setObjectName(u"labels_layout")
        self.type_metall_label_2 = QLabel(storage_frame)
        self.type_metall_label_2.setObjectName(u"type_metall_label_2")
        self.type_metall_label_2.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.type_metall_label_2)

        self.size_mm_label = QLabel(storage_frame)
        self.size_mm_label.setObjectName(u"size_mm_label")
        self.size_mm_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.size_mm_label)

        self.balance_kg_label = QLabel(storage_frame)
        self.balance_kg_label.setObjectName(u"balance_kg_label")
        self.balance_kg_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.balance_kg_label)

        self.balance_mm_label = QLabel(storage_frame)
        self.balance_mm_label.setObjectName(u"balance_mm_label")
        self.balance_mm_label.setAlignment(Qt.AlignCenter)

        self.labels_layout.addWidget(self.balance_mm_label)

        self.labels_layout.setStretch(0, 2)
        self.labels_layout.setStretch(1, 2)
        self.labels_layout.setStretch(2, 2)
        self.labels_layout.setStretch(3, 2)

        self.frame_layout.addLayout(self.labels_layout)

        self.storage_db_table = QTableView(storage_frame)
        self.storage_db_table.setObjectName(u"storage_db_table")

        self.frame_layout.addWidget(self.storage_db_table)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(0)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.in_storage_button = QPushButton(storage_frame)
        self.in_storage_button.setObjectName(u"in_storage_button")
        sizePolicy.setHeightForWidth(self.in_storage_button.sizePolicy().hasHeightForWidth())
        self.in_storage_button.setSizePolicy(sizePolicy)

        self.buttons_layout.addWidget(self.in_storage_button)

        self.out_storage_button = QPushButton(storage_frame)
        self.out_storage_button.setObjectName(u"out_storage_button")
        sizePolicy.setHeightForWidth(self.out_storage_button.sizePolicy().hasHeightForWidth())
        self.out_storage_button.setSizePolicy(sizePolicy)

        self.buttons_layout.addWidget(self.out_storage_button)

        self.buttons_layout.setStretch(0, 1)
        self.buttons_layout.setStretch(1, 1)

        self.frame_layout.addLayout(self.buttons_layout)

        self.pdf_layout = QHBoxLayout()
        self.pdf_layout.setSpacing(0)
        self.pdf_layout.setObjectName(u"pdf_layout")
        self.unload_storage_excel_button = QPushButton(storage_frame)
        self.unload_storage_excel_button.setObjectName(u"unload_storage_excel_button")
        sizePolicy.setHeightForWidth(self.unload_storage_excel_button.sizePolicy().hasHeightForWidth())
        self.unload_storage_excel_button.setSizePolicy(sizePolicy)
        self.unload_storage_excel_button.setMinimumSize(QSize(75, 0))
        self.unload_storage_excel_button.setMaximumSize(QSize(16777215, 100))

        self.pdf_layout.addWidget(self.unload_storage_excel_button)

        self.add_type_metal_button = QPushButton(storage_frame)
        self.add_type_metal_button.setObjectName(u"add_type_metal_button")
        sizePolicy.setHeightForWidth(self.add_type_metal_button.sizePolicy().hasHeightForWidth())
        self.add_type_metal_button.setSizePolicy(sizePolicy)

        self.pdf_layout.addWidget(self.add_type_metal_button)

        self.pdf_layout.setStretch(0, 5)
        self.pdf_layout.setStretch(1, 5)

        self.frame_layout.addLayout(self.pdf_layout)

        self.frame_layout.setStretch(0, 1)
        self.frame_layout.setStretch(1, 1)
        self.frame_layout.setStretch(2, 14)
        self.frame_layout.setStretch(3, 2)
        self.frame_layout.setStretch(4, 2)

        self.verticalLayout.addLayout(self.frame_layout)


        self.retranslateUi(storage_frame)

        QMetaObject.connectSlotsByName(storage_frame)
    # setupUi

    def retranslateUi(self, storage_frame):
        storage_frame.setWindowTitle(QCoreApplication.translate("storage_frame", u"Frame", None))
        self.back_button.setText(QCoreApplication.translate("storage_frame", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.frame_name_label.setText(QCoreApplication.translate("storage_frame", u"\u0421\u043a\u043b\u0430\u0434", None))
        self.type_metall_label_2.setText(QCoreApplication.translate("storage_frame", u"\u0412\u0438\u0434 \u043c\u0435\u0442\u0430\u043b\u043b\u0430", None))
        self.size_mm_label.setText(QCoreApplication.translate("storage_frame", u"\u0420\u0430\u0437\u043c\u0435\u0440, \u043c\u043c", None))
        self.balance_kg_label.setText(QCoreApplication.translate("storage_frame", u"\u041e\u0441\u0442\u0430\u0442\u043e\u043a, \u043a\u0433 | \u0448\u0442", None))
        self.balance_mm_label.setText(QCoreApplication.translate("storage_frame", u"\u041e\u0441\u0442\u0430\u0442\u043e\u043a, \u043c\u043c", None))
        self.in_storage_button.setText(QCoreApplication.translate("storage_frame", u"+", None))
        self.out_storage_button.setText(QCoreApplication.translate("storage_frame", u"-", None))
        self.unload_storage_excel_button.setText(QCoreApplication.translate("storage_frame", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 EXCEL", None))
        self.add_type_metal_button.setText(QCoreApplication.translate("storage_frame", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u0438\u0434 \u043c\u0435\u0442\u0430\u043b\u043b\u0430", None))
    # retranslateUi

