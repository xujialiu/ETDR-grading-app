# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GradWidget.ui'
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 964)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_25)

        self.label_visit_date = QLabel(self.centralwidget)
        self.label_visit_date.setObjectName(u"label_visit_date")

        self.horizontalLayout_2.addWidget(self.label_visit_date)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_20)

        self.label_patient_id = QLabel(self.centralwidget)
        self.label_patient_id.setObjectName(u"label_patient_id")

        self.horizontalLayout_2.addWidget(self.label_patient_id)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_21)

        self.label_num_photo = QLabel(self.centralwidget)
        self.label_num_photo.setObjectName(u"label_num_photo")

        self.horizontalLayout_2.addWidget(self.label_num_photo)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_22)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_23)

        self.label_user = QLabel(self.centralwidget)
        self.label_user.setObjectName(u"label_user")

        self.horizontalLayout.addWidget(self.label_user)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_18)

        self.label_eye = QLabel(self.centralwidget)
        self.label_eye.setObjectName(u"label_eye")

        self.horizontalLayout.addWidget(self.label_eye)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_26)

        self.label_score = QLabel(self.centralwidget)
        self.label_score.setObjectName(u"label_score")

        self.horizontalLayout.addWidget(self.label_score)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_24)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_28)

        self.comboBox_gradable = QComboBox(self.centralwidget)
        self.comboBox_gradable.addItem("")
        self.comboBox_gradable.addItem("")
        self.comboBox_gradable.setObjectName(u"comboBox_gradable")

        self.horizontalLayout_4.addWidget(self.comboBox_gradable)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_19.addWidget(self.label_20)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_31)

        self.comboBox_clarity = QComboBox(self.centralwidget)
        self.comboBox_clarity.addItem("")
        self.comboBox_clarity.addItem("")
        self.comboBox_clarity.setObjectName(u"comboBox_clarity")

        self.horizontalLayout_19.addWidget(self.comboBox_clarity)


        self.verticalLayout_2.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_18.addWidget(self.label_19)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_30)

        self.comboBox_is_dr = QComboBox(self.centralwidget)
        self.comboBox_is_dr.addItem("")
        self.comboBox_is_dr.addItem("")
        self.comboBox_is_dr.setObjectName(u"comboBox_is_dr")

        self.horizontalLayout_18.addWidget(self.comboBox_is_dr)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_27)

        self.lineEdit_other_diagnosis = QLineEdit(self.centralwidget)
        self.lineEdit_other_diagnosis.setObjectName(u"lineEdit_other_diagnosis")

        self.horizontalLayout_3.addWidget(self.lineEdit_other_diagnosis)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_HMA = QLabel(self.centralwidget)
        self.label_HMA.setObjectName(u"label_HMA")

        self.horizontalLayout_21.addWidget(self.label_HMA)

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

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_29)

        self.comboBox_confident = QComboBox(self.centralwidget)
        self.comboBox_confident.addItem("")
        self.comboBox_confident.addItem("")
        self.comboBox_confident.setObjectName(u"comboBox_confident")

        self.horizontalLayout_5.addWidget(self.comboBox_confident)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.textEdit_comment = QTextEdit(self.centralwidget)
        self.textEdit_comment.setObjectName(u"textEdit_comment")

        self.verticalLayout.addWidget(self.textEdit_comment)


        self.verticalLayout_2.addLayout(self.verticalLayout)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 849, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox_gradable.setCurrentIndex(-1)
        self.comboBox_clarity.setCurrentIndex(-1)
        self.comboBox_is_dr.setCurrentIndex(-1)
        self.comboBox_confident.setCurrentIndex(-1)
        self.pushButton_clear.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_visit_date.setText(QCoreApplication.translate("MainWindow", u"Visit date:", None))
        self.label_patient_id.setText(QCoreApplication.translate("MainWindow", u"Patient ID: ", None))
        self.label_num_photo.setText(QCoreApplication.translate("MainWindow", u"NO. photo / Total photos:", None))
        self.label_user.setText(QCoreApplication.translate("MainWindow", u"Grader: ", None))
        self.label_eye.setText(QCoreApplication.translate("MainWindow", u"Eye: ", None))
        self.label_score.setText(QCoreApplication.translate("MainWindow", u"Total score: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Is fundus photos gradable?", None))
        self.comboBox_gradable.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_gradable.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Clarity", None))
        self.comboBox_clarity.setItemText(0, QCoreApplication.translate("MainWindow", u"Blur", None))
        self.comboBox_clarity.setItemText(1, QCoreApplication.translate("MainWindow", u"Clear", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Whether it is DR?", None))
        self.comboBox_is_dr.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_is_dr.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"    Other diagnosis (if not DR)", None))
        self.label_HMA.setText(QCoreApplication.translate("MainWindow", u"Haemorrhage/Microaneurysms (HMA):", None))
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Are you confident in this grading?", None))
        self.comboBox_confident.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_confident.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Comments:", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

