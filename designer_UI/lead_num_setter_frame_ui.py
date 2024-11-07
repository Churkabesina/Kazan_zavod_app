# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lead_num_setter_frame.ui'
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
    QLineEdit, QSizePolicy, QWidget)

class Ui_lead_num_setter_frame(object):
    def setupUi(self, lead_num_setter_frame):
        if not lead_num_setter_frame.objectName():
            lead_num_setter_frame.setObjectName(u"lead_num_setter_frame")
        lead_num_setter_frame.resize(443, 89)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lead_num_setter_frame.sizePolicy().hasHeightForWidth())
        lead_num_setter_frame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(lead_num_setter_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.product_label = QLabel(lead_num_setter_frame)
        self.product_label.setObjectName(u"product_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.product_label.sizePolicy().hasHeightForWidth())
        self.product_label.setSizePolicy(sizePolicy1)
        self.product_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.product_label)

        self.line_edit = QLineEdit(lead_num_setter_frame)
        self.line_edit.setObjectName(u"line_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_edit.sizePolicy().hasHeightForWidth())
        self.line_edit.setSizePolicy(sizePolicy2)
        self.line_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.line_edit)

        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(lead_num_setter_frame)

        QMetaObject.connectSlotsByName(lead_num_setter_frame)
    # setupUi

    def retranslateUi(self, lead_num_setter_frame):
        lead_num_setter_frame.setWindowTitle(QCoreApplication.translate("lead_num_setter_frame", u"Frame", None))
        self.product_label.setText("")
        self.line_edit.setText("")
    # retranslateUi

