# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gradwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 964)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_25)

        self.label_visit_date = QLabel(self.centralwidget)
        self.label_visit_date.setObjectName(u"label_visit_date")

        self.horizontalLayout_2.addWidget(self.label_visit_date)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_20)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_21)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_22)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_23)

        self.radioButton_eye_r = QRadioButton(self.centralwidget)
        self.radioButton_eye_r.setObjectName(u"radioButton_eye_r")
        self.radioButton_eye_r.setCheckable(False)

        self.horizontalLayout.addWidget(self.radioButton_eye_r)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_18)

        self.radioButton_eye_l = QRadioButton(self.centralwidget)
        self.radioButton_eye_l.setObjectName(u"radioButton_eye_l")
        self.radioButton_eye_l.setCheckable(False)

        self.horizontalLayout.addWidget(self.radioButton_eye_l)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_24)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_21.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer)

        self.comboBox_HMA = QComboBox(self.centralwidget)
        self.comboBox_HMA.setObjectName(u"comboBox_HMA")
        self.comboBox_HMA.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_HMA.sizePolicy().hasHeightForWidth())
        self.comboBox_HMA.setSizePolicy(sizePolicy)
        self.comboBox_HMA.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_21.addWidget(self.comboBox_HMA)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_SE = QHBoxLayout()
        self.horizontalLayout_SE.setObjectName(u"horizontalLayout_SE")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_SE.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_SE.addItem(self.horizontalSpacer_2)

        self.comboBox_HE = QComboBox(self.centralwidget)
        self.comboBox_HE.setObjectName(u"comboBox_HE")

        self.horizontalLayout_SE.addWidget(self.comboBox_HE)


        self.verticalLayout_2.addLayout(self.horizontalLayout_SE)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.comboBox_SE = QComboBox(self.centralwidget)
        self.comboBox_SE.setObjectName(u"comboBox_SE")

        self.horizontalLayout_6.addWidget(self.comboBox_SE)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.comboBox_IRMA = QComboBox(self.centralwidget)
        self.comboBox_IRMA.setObjectName(u"comboBox_IRMA")

        self.horizontalLayout_7.addWidget(self.comboBox_IRMA)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.comboBox_VB = QComboBox(self.centralwidget)
        self.comboBox_VB.setObjectName(u"comboBox_VB")

        self.horizontalLayout_8.addWidget(self.comboBox_VB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.comboBox_NVD = QComboBox(self.centralwidget)
        self.comboBox_NVD.setObjectName(u"comboBox_NVD")

        self.horizontalLayout_9.addWidget(self.comboBox_NVD)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.comboBox_NVE = QComboBox(self.centralwidget)
        self.comboBox_NVE.setObjectName(u"comboBox_NVE")

        self.horizontalLayout_10.addWidget(self.comboBox_NVE)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.comboBox_FP = QComboBox(self.centralwidget)
        self.comboBox_FP.setObjectName(u"comboBox_FP")

        self.horizontalLayout_11.addWidget(self.comboBox_FP)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.comboBox_PRH_VH = QComboBox(self.centralwidget)
        self.comboBox_PRH_VH.setObjectName(u"comboBox_PRH_VH")

        self.horizontalLayout_12.addWidget(self.comboBox_PRH_VH)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(131, 0))

        self.horizontalLayout_13.addWidget(self.label_13)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.comboBox_EDEMA = QComboBox(self.centralwidget)
        self.comboBox_EDEMA.setObjectName(u"comboBox_EDEMA")

        self.horizontalLayout_13.addWidget(self.comboBox_EDEMA)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.comboBox_CTR = QComboBox(self.centralwidget)
        self.comboBox_CTR.setObjectName(u"comboBox_CTR")

        self.horizontalLayout_14.addWidget(self.comboBox_CTR)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_12)

        self.comboBox_VEN = QComboBox(self.centralwidget)
        self.comboBox_VEN.setObjectName(u"comboBox_VEN")

        self.horizontalLayout_15.addWidget(self.comboBox_VEN)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)

        self.comboBox_LASER = QComboBox(self.centralwidget)
        self.comboBox_LASER.setObjectName(u"comboBox_LASER")

        self.horizontalLayout_16.addWidget(self.comboBox_LASER)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.horizontalSpacer_14 = QSpacerItem(40, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)

        self.comboBox_RX = QComboBox(self.centralwidget)
        self.comboBox_RX.setObjectName(u"comboBox_RX")

        self.horizontalLayout_17.addWidget(self.comboBox_RX)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.textEdit_comment = QTextEdit(self.centralwidget)
        self.textEdit_comment.setObjectName(u"textEdit_comment")

        self.verticalLayout.addWidget(self.textEdit_comment)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_17)

        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setAutoDefault(False)
        self.pushButton_clear.setFlat(False)

        self.horizontalLayout_20.addWidget(self.pushButton_clear)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout_20.addWidget(self.pushButton_save)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_19)

        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.horizontalLayout_20.addWidget(self.pushButton_next)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_16)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 849, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_clear.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_visit_date.setText(QCoreApplication.translate("MainWindow", u"Visit date:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Patient ID: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NO. photo / Total photos:", None))
        self.radioButton_eye_r.setText(QCoreApplication.translate("MainWindow", u"Right eye (OD)", None))
        self.radioButton_eye_l.setText(QCoreApplication.translate("MainWindow", u"Left eye (OS)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Haemorrhage/Microaneurysms (HMA):", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hard Exudates (HE):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Soft Exudates (SE):", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Intraretinal Microvascular Abnormalities (IRMA):", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Venous Beeding (VB):", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"New Vessels on the Disc (NVD):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"New vessels Elsewhere (NVE):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Fibrous Proliferation (FP):", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pre-retinal Haemorrhage-Vitreous Haemorrhage (PRH-VH):", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"MAC-EDEMA:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"MAC CTR:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"VEN LOOPS", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"LASER SCARS", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"FOCAL/GRID RX", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Comments:", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

