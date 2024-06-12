# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1234, 881)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_user = QLineEdit(self.centralwidget)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_user.sizePolicy().hasHeightForWidth())
        self.lineEdit_user.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_user, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.lineEdit_password, 1, 1, 1, 1)

        self.pushButton_login = QPushButton(self.centralwidget)
        self.pushButton_login.setObjectName(u"pushButton_login")
        sizePolicy.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_login, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.treeWidget_patient = QTreeWidget(self.centralwidget)
        self.treeWidget_patient.setObjectName(u"treeWidget_patient")
        self.treeWidget_patient.setSortingEnabled(True)

        self.horizontalLayout_3.addWidget(self.treeWidget_patient)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tableWidget_graded = QTableWidget(self.centralwidget)
        if (self.tableWidget_graded.columnCount() < 3):
            self.tableWidget_graded.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_graded.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_graded.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_graded.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_graded.setObjectName(u"tableWidget_graded")

        self.verticalLayout.addWidget(self.tableWidget_graded)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.tableWidget_database = QTableWidget(self.centralwidget)
        if (self.tableWidget_database.columnCount() < 1):
            self.tableWidget_database.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_database.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        self.tableWidget_database.setObjectName(u"tableWidget_database")

        self.verticalLayout.addWidget(self.tableWidget_database)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.folder_button = QPushButton(self.centralwidget)
        self.folder_button.setObjectName(u"folder_button")
        self.folder_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.folder_button.sizePolicy().hasHeightForWidth())
        self.folder_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.folder_button)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.label_folder = QLabel(self.frame)
        self.label_folder.setObjectName(u"label_folder")
        self.label_folder.setGeometry(QRect(10, 0, 331, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_folder.sizePolicy().hasHeightForWidth())
        self.label_folder.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.frame)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1234, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password::", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        ___qtreewidgetitem = self.treeWidget_patient.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Patient ID / Visit Date", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Graded list:", None))
        ___qtablewidgetitem = self.tableWidget_graded.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Patient ID", None));
        ___qtablewidgetitem1 = self.tableWidget_graded.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Visit Date", None));
        ___qtablewidgetitem2 = self.tableWidget_graded.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Eye", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Database: ", None))
        ___qtablewidgetitem3 = self.tableWidget_database.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Patient ID", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total score:", None))
        self.folder_button.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.label_folder.setText("")
    # retranslateUi

