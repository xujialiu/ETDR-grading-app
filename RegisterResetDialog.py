# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterResetDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(322, 129)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(322, 129))
        Dialog.setMaximumSize(QSize(322, 129))
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_user = QLabel(Dialog)
        self.label_user.setObjectName(u"label_user")

        self.verticalLayout_2.addWidget(self.label_user)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_user = QLineEdit(Dialog)
        self.lineEdit_user.setObjectName(u"lineEdit_user")

        self.verticalLayout.addWidget(self.lineEdit_user)

        self.lineEdit_password = QLineEdit(Dialog)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.lineEdit_password)

        self.lineEdit_confirm_password = QLineEdit(Dialog)
        self.lineEdit_confirm_password.setObjectName(u"lineEdit_confirm_password")
        self.lineEdit_confirm_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.lineEdit_confirm_password)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_register_reset = QPushButton(Dialog)
        self.pushButton_register_reset.setObjectName(u"pushButton_register_reset")

        self.horizontalLayout_4.addWidget(self.pushButton_register_reset)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_4.addWidget(self.pushButton_cancel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_user.setText(QCoreApplication.translate("Dialog", u"User name:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Password: ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Confirm Password:", None))
        self.pushButton_register_reset.setText(QCoreApplication.translate("Dialog", u"Register / Reset password", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

