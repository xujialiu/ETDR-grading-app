# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1234, 881)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 9, 221, 23))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 70, 601, 491))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 38, 528, 25))
        self.horizontalLayout_19 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_ID = QLineEdit(self.layoutWidget)
        self.lineEdit_ID.setObjectName(u"lineEdit_ID")

        self.horizontalLayout.addWidget(self.lineEdit_ID)


        self.horizontalLayout_19.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_Grader = QLineEdit(self.layoutWidget)
        self.lineEdit_Grader.setObjectName(u"lineEdit_Grader")

        self.horizontalLayout_2.addWidget(self.lineEdit_Grader)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_18.addWidget(self.label_19)

        self.dateEdit_Visit_data = QDateEdit(self.layoutWidget)
        self.dateEdit_Visit_data.setObjectName(u"dateEdit_Visit_data")
        self.dateEdit_Visit_data.setEnabled(True)
        self.dateEdit_Visit_data.setMinimumSize(QSize(120, 0))
        self.dateEdit_Visit_data.setFrame(True)

        self.horizontalLayout_18.addWidget(self.dateEdit_Visit_data)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(750, 54, 471, 444))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_21.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer)

        self.comboBox_HMA = QComboBox(self.layoutWidget1)
        self.comboBox_HMA.setObjectName(u"comboBox_HMA")

        self.horizontalLayout_21.addWidget(self.comboBox_HMA)

        self.pushButton_17 = QPushButton(self.layoutWidget1)
        self.pushButton_17.setObjectName(u"pushButton_17")
        icon = QIcon()
        icon.addFile(u"question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon)

        self.horizontalLayout_21.addWidget(self.pushButton_17)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_SE = QHBoxLayout()
        self.horizontalLayout_SE.setObjectName(u"horizontalLayout_SE")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_SE.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_SE.addItem(self.horizontalSpacer_2)

        self.comboBox_HE = QComboBox(self.layoutWidget1)
        self.comboBox_HE.setObjectName(u"comboBox_HE")

        self.horizontalLayout_SE.addWidget(self.comboBox_HE)

        self.pushButton_16 = QPushButton(self.layoutWidget1)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setIcon(icon)

        self.horizontalLayout_SE.addWidget(self.pushButton_16)


        self.verticalLayout_2.addLayout(self.horizontalLayout_SE)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.comboBox_SE = QComboBox(self.layoutWidget1)
        self.comboBox_SE.setObjectName(u"comboBox_SE")

        self.horizontalLayout_6.addWidget(self.comboBox_SE)

        self.pushButton_15 = QPushButton(self.layoutWidget1)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.pushButton_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.comboBox_IRMA = QComboBox(self.layoutWidget1)
        self.comboBox_IRMA.setObjectName(u"comboBox_IRMA")

        self.horizontalLayout_7.addWidget(self.comboBox_IRMA)

        self.pushButton_4 = QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.comboBox_VB = QComboBox(self.layoutWidget1)
        self.comboBox_VB.setObjectName(u"comboBox_VB")

        self.horizontalLayout_8.addWidget(self.comboBox_VB)

        self.pushButton_5 = QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.pushButton_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.comboBox_NVD = QComboBox(self.layoutWidget1)
        self.comboBox_NVD.setObjectName(u"comboBox_NVD")

        self.horizontalLayout_9.addWidget(self.comboBox_NVD)

        self.pushButton_6 = QPushButton(self.layoutWidget1)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.pushButton_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.comboBox_NVE = QComboBox(self.layoutWidget1)
        self.comboBox_NVE.setObjectName(u"comboBox_NVE")

        self.horizontalLayout_10.addWidget(self.comboBox_NVE)

        self.pushButton_7 = QPushButton(self.layoutWidget1)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon)

        self.horizontalLayout_10.addWidget(self.pushButton_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.comboBox_FP = QComboBox(self.layoutWidget1)
        self.comboBox_FP.setObjectName(u"comboBox_FP")

        self.horizontalLayout_11.addWidget(self.comboBox_FP)

        self.pushButton_8 = QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.pushButton_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.comboBox_PRH_VH = QComboBox(self.layoutWidget1)
        self.comboBox_PRH_VH.setObjectName(u"comboBox_PRH_VH")

        self.horizontalLayout_12.addWidget(self.comboBox_PRH_VH)

        self.pushButton_9 = QPushButton(self.layoutWidget1)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon)

        self.horizontalLayout_12.addWidget(self.pushButton_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(131, 0))

        self.horizontalLayout_13.addWidget(self.label_13)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.comboBox_EDEMA = QComboBox(self.layoutWidget1)
        self.comboBox_EDEMA.setObjectName(u"comboBox_EDEMA")

        self.horizontalLayout_13.addWidget(self.comboBox_EDEMA)

        self.pushButton_10 = QPushButton(self.layoutWidget1)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.pushButton_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.comboBox_CTR = QComboBox(self.layoutWidget1)
        self.comboBox_CTR.setObjectName(u"comboBox_CTR")

        self.horizontalLayout_14.addWidget(self.comboBox_CTR)

        self.pushButton_11 = QPushButton(self.layoutWidget1)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setIcon(icon)

        self.horizontalLayout_14.addWidget(self.pushButton_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_12)

        self.comboBox_VEN = QComboBox(self.layoutWidget1)
        self.comboBox_VEN.setObjectName(u"comboBox_VEN")

        self.horizontalLayout_15.addWidget(self.comboBox_VEN)

        self.pushButton_12 = QPushButton(self.layoutWidget1)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.pushButton_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)

        self.comboBox_LASER = QComboBox(self.layoutWidget1)
        self.comboBox_LASER.setObjectName(u"comboBox_LASER")

        self.horizontalLayout_16.addWidget(self.comboBox_LASER)

        self.pushButton_13 = QPushButton(self.layoutWidget1)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setIcon(icon)

        self.horizontalLayout_16.addWidget(self.pushButton_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.horizontalSpacer_14 = QSpacerItem(40, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)

        self.comboBox_RX = QComboBox(self.layoutWidget1)
        self.comboBox_RX.setObjectName(u"comboBox_RX")

        self.horizontalLayout_17.addWidget(self.comboBox_RX)

        self.pushButton_14 = QPushButton(self.layoutWidget1)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setIcon(icon)

        self.horizontalLayout_17.addWidget(self.pushButton_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(750, 510, 461, 194))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_18 = QLabel(self.layoutWidget2)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.textEdit_comment = QTextEdit(self.layoutWidget2)
        self.textEdit_comment.setObjectName(u"textEdit_comment")

        self.horizontalLayout_3.addWidget(self.textEdit_comment)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(750, 770, 331, 26))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_20.addWidget(self.pushButton)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.pushButton_2 = QPushButton(self.layoutWidget3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_20.addWidget(self.pushButton_2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_16)

        self.pushButton_3 = QPushButton(self.layoutWidget3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_20.addWidget(self.pushButton_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 760, 391, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.folder_line = QLineEdit(self.widget)
        self.folder_line.setObjectName(u"folder_line")

        self.horizontalLayout_4.addWidget(self.folder_line)

        self.folder_button = QPushButton(self.widget)
        self.folder_button.setObjectName(u"folder_button")

        self.horizontalLayout_4.addWidget(self.folder_button)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Diabetic Retinopathy Grading", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Grader:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Visit date:", None))
        self.dateEdit_Visit_data.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Haemorrhage/Microaneurysms (HMA):", None))
        self.pushButton_17.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hard Exudates (HE):", None))
        self.pushButton_16.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Soft Exudates (SE):", None))
        self.pushButton_15.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Intraretinal Microvascular Abnormalities (IRMA):", None))
        self.pushButton_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Venous Beeding (VB):", None))
        self.pushButton_5.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"New Vessels on the Disc (NVD):", None))
        self.pushButton_6.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"New vessels Elsewhere (NVE):", None))
        self.pushButton_7.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Fibrous Proliferation (FP):", None))
        self.pushButton_8.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pre-retinal Haemorrhage-Vitreous Haemorrhage (PRH-VH):", None))
        self.pushButton_9.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"MAC-EDEMA:", None))
        self.pushButton_10.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"MAC CTR:", None))
        self.pushButton_11.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"VEN LOOPS", None))
        self.pushButton_12.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"LASER SCARS", None))
        self.pushButton_13.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"FOCAL/GRID RX", None))
        self.pushButton_14.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Comments:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.folder_button.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
    # retranslateUi

