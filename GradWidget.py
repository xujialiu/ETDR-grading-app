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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1090, 1273)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_14 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
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


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

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


        self.verticalLayout_10.addLayout(self.horizontalLayout)


        self.verticalLayout_13.addLayout(self.verticalLayout_10)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)

        self.horizontalLayout_25.addWidget(self.label_23)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)

        self.horizontalLayout_25.addWidget(self.frame)


        self.verticalLayout_13.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)

        self.horizontalLayout_33.addWidget(self.label_30)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)

        self.horizontalLayout_30.addWidget(self.label_29)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_gradable.sizePolicy().hasHeightForWidth())
        self.comboBox_gradable.setSizePolicy(sizePolicy1)
        self.comboBox_gradable.setMinimumSize(QSize(150, 0))
        self.comboBox_gradable.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.comboBox_gradable)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

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
        sizePolicy1.setHeightForWidth(self.comboBox_clarity.sizePolicy().hasHeightForWidth())
        self.comboBox_clarity.setSizePolicy(sizePolicy1)
        self.comboBox_clarity.setMinimumSize(QSize(150, 0))
        self.comboBox_clarity.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_19.addWidget(self.comboBox_clarity)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

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
        sizePolicy1.setHeightForWidth(self.comboBox_is_dr.sizePolicy().hasHeightForWidth())
        self.comboBox_is_dr.setSizePolicy(sizePolicy1)
        self.comboBox_is_dr.setMinimumSize(QSize(150, 0))
        self.comboBox_is_dr.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_18.addWidget(self.comboBox_is_dr)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)

        self.horizontalLayout_28.addWidget(self.label_26)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_27)

        self.comboBox_diagnoses = QComboBox(self.centralwidget)
        self.comboBox_diagnoses.setObjectName(u"comboBox_diagnoses")

        self.horizontalLayout_3.addWidget(self.comboBox_diagnoses)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_23.addWidget(self.label_4)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_33)

        self.lineEdit_other_diagnoses = QLineEdit(self.centralwidget)
        self.lineEdit_other_diagnoses.setObjectName(u"lineEdit_other_diagnoses")
        sizePolicy1.setHeightForWidth(self.lineEdit_other_diagnoses.sizePolicy().hasHeightForWidth())
        self.lineEdit_other_diagnoses.setSizePolicy(sizePolicy1)
        self.lineEdit_other_diagnoses.setMinimumSize(QSize(150, 0))
        self.lineEdit_other_diagnoses.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_23.addWidget(self.lineEdit_other_diagnoses)


        self.verticalLayout_2.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_28.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_24.addWidget(self.label_22)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_34)

        self.comboBox_ICDR = QComboBox(self.centralwidget)
        self.comboBox_ICDR.setObjectName(u"comboBox_ICDR")

        self.horizontalLayout_24.addWidget(self.comboBox_ICDR)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_30.addLayout(self.verticalLayout_3)


        self.horizontalLayout_33.addLayout(self.horizontalLayout_30)


        self.verticalLayout_13.addLayout(self.horizontalLayout_33)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)

        self.horizontalLayout_26.addWidget(self.label_24)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.HLine)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(1)

        self.horizontalLayout_26.addWidget(self.frame_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_HMA_3 = QLabel(self.centralwidget)
        self.label_HMA_3.setObjectName(u"label_HMA_3")

        self.horizontalLayout_32.addWidget(self.label_HMA_3)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_35)

        self.comboBox_MA = QComboBox(self.centralwidget)
        self.comboBox_MA.setObjectName(u"comboBox_MA")
        self.comboBox_MA.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_MA.sizePolicy().hasHeightForWidth())
        self.comboBox_MA.setSizePolicy(sizePolicy2)
        self.comboBox_MA.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_32.addWidget(self.comboBox_MA)


        self.verticalLayout_12.addLayout(self.horizontalLayout_32)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_HMA = QLabel(self.centralwidget)
        self.label_HMA.setObjectName(u"label_HMA")

        self.horizontalLayout_21.addWidget(self.label_HMA)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer)

        self.comboBox_RH = QComboBox(self.centralwidget)
        self.comboBox_RH.setObjectName(u"comboBox_RH")
        self.comboBox_RH.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.comboBox_RH.sizePolicy().hasHeightForWidth())
        self.comboBox_RH.setSizePolicy(sizePolicy2)
        self.comboBox_RH.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_21.addWidget(self.comboBox_RH)


        self.verticalLayout_5.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.label_31)

        self.label_HMA_2 = QLabel(self.centralwidget)
        self.label_HMA_2.setObjectName(u"label_HMA_2")

        self.horizontalLayout_13.addWidget(self.label_HMA_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.spinBox_RH_quadrants = QSpinBox(self.centralwidget)
        self.spinBox_RH_quadrants.setObjectName(u"spinBox_RH_quadrants")
        self.spinBox_RH_quadrants.setMaximum(4)

        self.horizontalLayout_13.addWidget(self.spinBox_RH_quadrants)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)


        self.verticalLayout_12.addLayout(self.verticalLayout_5)

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


        self.verticalLayout_12.addLayout(self.horizontalLayout_SE)

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


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
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


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.label_32)

        self.label_HMA_4 = QLabel(self.centralwidget)
        self.label_HMA_4.setObjectName(u"label_HMA_4")

        self.horizontalLayout_14.addWidget(self.label_HMA_4)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.spinBox_IRMA_quadrants = QSpinBox(self.centralwidget)
        self.spinBox_IRMA_quadrants.setObjectName(u"spinBox_IRMA_quadrants")
        self.spinBox_IRMA_quadrants.setMaximum(4)

        self.horizontalLayout_14.addWidget(self.spinBox_IRMA_quadrants)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.label_33)

        self.label_HMA_5 = QLabel(self.centralwidget)
        self.label_HMA_5.setObjectName(u"label_HMA_5")

        self.horizontalLayout_17.addWidget(self.label_HMA_5)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)

        self.spinBox_VB_quadrants = QSpinBox(self.centralwidget)
        self.spinBox_VB_quadrants.setObjectName(u"spinBox_VB_quadrants")
        self.spinBox_VB_quadrants.setMaximum(4)

        self.horizontalLayout_17.addWidget(self.spinBox_VB_quadrants)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)


        self.verticalLayout_12.addLayout(self.verticalLayout_6)

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


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
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


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)

        self.horizontalLayout_29.addWidget(self.label_34)

        self.label_HMA_6 = QLabel(self.centralwidget)
        self.label_HMA_6.setObjectName(u"label_HMA_6")

        self.horizontalLayout_29.addWidget(self.label_HMA_6)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_16)

        self.spinBox_NVE_quadrants = QSpinBox(self.centralwidget)
        self.spinBox_NVE_quadrants.setObjectName(u"spinBox_NVE_quadrants")
        self.spinBox_NVE_quadrants.setMaximum(4)

        self.horizontalLayout_29.addWidget(self.spinBox_NVE_quadrants)


        self.verticalLayout_8.addLayout(self.horizontalLayout_29)


        self.verticalLayout_12.addLayout(self.verticalLayout_8)

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


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
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


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)

        self.horizontalLayout_34.addWidget(self.label_35)

        self.label_HMA_7 = QLabel(self.centralwidget)
        self.label_HMA_7.setObjectName(u"label_HMA_7")

        self.horizontalLayout_34.addWidget(self.label_HMA_7)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_37)

        self.comboBox_VH_extent = QComboBox(self.centralwidget)
        self.comboBox_VH_extent.addItem("")
        self.comboBox_VH_extent.addItem("")
        self.comboBox_VH_extent.addItem("")
        self.comboBox_VH_extent.setObjectName(u"comboBox_VH_extent")
        sizePolicy1.setHeightForWidth(self.comboBox_VH_extent.sizePolicy().hasHeightForWidth())
        self.comboBox_VH_extent.setSizePolicy(sizePolicy1)
        self.comboBox_VH_extent.setMinimumSize(QSize(150, 0))
        self.comboBox_VH_extent.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_34.addWidget(self.comboBox_VH_extent)


        self.verticalLayout_9.addLayout(self.horizontalLayout_34)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)

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


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

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


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_22.addWidget(self.label_21)

        self.horizontalSpacer_32 = QSpacerItem(40, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_32)

        self.comboBox_RD = QComboBox(self.centralwidget)
        self.comboBox_RD.setObjectName(u"comboBox_RD")

        self.horizontalLayout_22.addWidget(self.comboBox_RD)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)

        self.horizontalLayout_27.addWidget(self.label_25)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.HLine)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(1)

        self.horizontalLayout_27.addWidget(self.frame_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)

        self.horizontalLayout_31.addWidget(self.label_28)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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
        sizePolicy1.setHeightForWidth(self.comboBox_confident.sizePolicy().hasHeightForWidth())
        self.comboBox_confident.setSizePolicy(sizePolicy1)
        self.comboBox_confident.setMinimumSize(QSize(150, 0))
        self.comboBox_confident.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox_confident)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.textEdit_comment = QTextEdit(self.centralwidget)
        self.textEdit_comment.setObjectName(u"textEdit_comment")

        self.verticalLayout.addWidget(self.textEdit_comment)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout_31.addLayout(self.verticalLayout_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_31)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

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


        self.verticalLayout_13.addLayout(self.horizontalLayout_20)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1090, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox_gradable.setCurrentIndex(0)
        self.comboBox_clarity.setCurrentIndex(-1)
        self.comboBox_is_dr.setCurrentIndex(-1)
        self.comboBox_VH_extent.setCurrentIndex(-1)
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
        self.label_score.setText(QCoreApplication.translate("MainWindow", u"Levels: ", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"General:", None))
        self.label_30.setText("")
        self.label_29.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Is fundus photos gradable?", None))
        self.comboBox_gradable.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_gradable.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Clarity:", None))
        self.comboBox_clarity.setItemText(0, QCoreApplication.translate("MainWindow", u"Blur", None))
        self.comboBox_clarity.setItemText(1, QCoreApplication.translate("MainWindow", u"Clear", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Whether it is DR?", None))
        self.comboBox_is_dr.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_is_dr.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_26.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Other diagnoses:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"If not listed above:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"ICDR:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"ETDR:", None))
        self.label_HMA_3.setText(QCoreApplication.translate("MainWindow", u"Microaneurysms:", None))
        self.label_HMA.setText(QCoreApplication.translate("MainWindow", u"Retinal Haemorrhage:", None))
        self.label_31.setText("")
        self.label_HMA_2.setText(QCoreApplication.translate("MainWindow", u"Haemorrhage Quadrants:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hard Exudates (HE):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Soft Exudates (SE):", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Intraretinal Microvascular Abnormalities (IRMA):", None))
        self.label_32.setText("")
        self.label_HMA_4.setText(QCoreApplication.translate("MainWindow", u"IRMA Quadrants:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Venous Beeding (VB):", None))
        self.label_33.setText("")
        self.label_HMA_5.setText(QCoreApplication.translate("MainWindow", u"VB Quadrants:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"New Vessels on the Disc (NVD):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"New vessels Elsewhere (NVE):", None))
        self.label_34.setText("")
        self.label_HMA_6.setText(QCoreApplication.translate("MainWindow", u"NVE Quadrants:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Fibrous Proliferation (FP):", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pre-retinal Haemorrhage-Vitreous Haemorrhage (PRH-VH):", None))
        self.label_35.setText("")
        self.label_HMA_7.setText(QCoreApplication.translate("MainWindow", u"Extent of VH", None))
        self.comboBox_VH_extent.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_VH_extent.setItemText(1, QCoreApplication.translate("MainWindow", u"VH Obsure < 1/2 fundus", None))
        self.comboBox_VH_extent.setItemText(2, QCoreApplication.translate("MainWindow", u"VH Obsure \u2265 1/2 fundus", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Venous Loops", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Laser Scars", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Retinal Detachment (RD):", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Others:", None))
        self.label_28.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Are you confident in this grading?", None))
        self.comboBox_confident.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_confident.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Comments:", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

