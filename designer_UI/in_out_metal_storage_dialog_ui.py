# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'in_out_metal_storage_dialog.ui'
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

class Ui_in_out_metal_storage_dialog(object):
    def setupUi(self, in_out_metal_storage_dialog):
        if not in_out_metal_storage_dialog.objectName():
            in_out_metal_storage_dialog.setObjectName(u"in_out_metal_storage_dialog")
        in_out_metal_storage_dialog.resize(580, 150)
        self.verticalLayout = QVBoxLayout(in_out_metal_storage_dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.type_metall_label = QLabel(in_out_metal_storage_dialog)
        self.type_metall_label.setObjectName(u"type_metall_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_metall_label.sizePolicy().hasHeightForWidth())
        self.type_metall_label.setSizePolicy(sizePolicy)
        self.type_metall_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.type_metall_label)

        self.size_mm_label = QLabel(in_out_metal_storage_dialog)
        self.size_mm_label.setObjectName(u"size_mm_label")
        sizePolicy.setHeightForWidth(self.size_mm_label.sizePolicy().hasHeightForWidth())
        self.size_mm_label.setSizePolicy(sizePolicy)
        self.size_mm_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.size_mm_label)

        self.balance_kg_label = QLabel(in_out_metal_storage_dialog)
        self.balance_kg_label.setObjectName(u"balance_kg_label")
        sizePolicy.setHeightForWidth(self.balance_kg_label.sizePolicy().hasHeightForWidth())
        self.balance_kg_label.setSizePolicy(sizePolicy)
        self.balance_kg_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.balance_kg_label)

        self.horizontalSpacer_3 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 50)
        self.type_metall_combo_box = QComboBox(in_out_metal_storage_dialog)
        self.type_metall_combo_box.setObjectName(u"type_metall_combo_box")
        sizePolicy.setHeightForWidth(self.type_metall_combo_box.sizePolicy().hasHeightForWidth())
        self.type_metall_combo_box.setSizePolicy(sizePolicy)
        self.type_metall_combo_box.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.type_metall_combo_box)

        self.size_combo_box = QComboBox(in_out_metal_storage_dialog)
        self.size_combo_box.setObjectName(u"size_combo_box")
        sizePolicy.setHeightForWidth(self.size_combo_box.sizePolicy().hasHeightForWidth())
        self.size_combo_box.setSizePolicy(sizePolicy)
        self.size_combo_box.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.size_combo_box)

        self.balance_double_spin_box = QDoubleSpinBox(in_out_metal_storage_dialog)
        self.balance_double_spin_box.setObjectName(u"balance_double_spin_box")
        sizePolicy.setHeightForWidth(self.balance_double_spin_box.sizePolicy().hasHeightForWidth())
        self.balance_double_spin_box.setSizePolicy(sizePolicy)
        self.balance_double_spin_box.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.balance_double_spin_box)

        self.kg_sht_label = QLabel(in_out_metal_storage_dialog)
        self.kg_sht_label.setObjectName(u"kg_sht_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.kg_sht_label.sizePolicy().hasHeightForWidth())
        self.kg_sht_label.setSizePolicy(sizePolicy1)
        self.kg_sht_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.kg_sht_label)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ok_button = QPushButton(in_out_metal_storage_dialog)
        self.ok_button.setObjectName(u"ok_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.ok_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(in_out_metal_storage_dialog)

        QMetaObject.connectSlotsByName(in_out_metal_storage_dialog)
    # setupUi

    def retranslateUi(self, in_out_metal_storage_dialog):
        in_out_metal_storage_dialog.setWindowTitle("")
        self.type_metall_label.setText(QCoreApplication.translate("in_out_metal_storage_dialog", u"\u0412\u0438\u0434 \u043c\u0435\u0442\u0430\u043b\u043b\u0430", None))
        self.size_mm_label.setText(QCoreApplication.translate("in_out_metal_storage_dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440, \u043c\u043c", None))
        self.balance_kg_label.setText(QCoreApplication.translate("in_out_metal_storage_dialog", u"\u041f\u0440\u0438\u0445\u043e\u0434", None))
        self.kg_sht_label.setText(QCoreApplication.translate("in_out_metal_storage_dialog", u"\u041a\u0413", None))
        self.ok_button.setText(QCoreApplication.translate("in_out_metal_storage_dialog", u"\u041e\u041a", None))
    # retranslateUi

