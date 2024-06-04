# from pathlib import Path
# from signal import CTRL_BREAK_EVENT

# from PySide6.QtCore import QRect, QSize
# from PySide6.QtGui import QIcon
# from PySide6.QtWidgets import QPushButton
# from HoverButtonImpl import HoverButton
# import MainWindow
# from dataclasses import dataclass


# @dataclass(frozen=True)
# class OptionItem:
#     score: int
#     path: str | Path


# class MainWindowImpl(MainWindow.Ui_MainWindow):
#     def __init__(self, MainWindow):
#         super().__init__()

#         self.setupUi(MainWindow)
#         self.InitUI()
#         self.modify_ui()

#     def InitUI(self):
#         HMA_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "<std 1": OptionItem(2, "question.png"),
#             "≥std 1": OptionItem(3, "question.png"),
#             "≥std 2A": OptionItem(4, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }
#         HE_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "<std 3": OptionItem(2, "question.png"),
#             "≥std 3 - <std 4": OptionItem(2, "question.png"),
#             "≥std 4": OptionItem(4, "question.png"),
#         }
#         SE_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "Definite": OptionItem(2, "question.png"),
#         }
#         IRMA_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "Definite": OptionItem(2, "question.png"),
#             "Definite (all fields)": OptionItem(3, "question.png"),
#             "≥std 8A": OptionItem(4, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }
#         VB_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "Definite": OptionItem(2, "question.png"),
#             "Definite (2+ fields)": OptionItem(3, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }
#         NVD_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "<std 10A": OptionItem(2, "question.png"),
#             "≥std 10A": OptionItem(3, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }
#         NVE_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "<1/2 Disc area": OptionItem(2, "question.png"),
#             "≥1/2 Disc area": OptionItem(3, "question.png"),
#         }
#         FP_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "FPE only": OptionItem(2, "question.png"),
#             "FPD only": OptionItem(3, "question.png"),
#             "FPD + FPE": OptionItem(4, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }
#         PRH_VH_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "PRH only": OptionItem(2, "question.png"),
#             "VH only": OptionItem(3, "question.png"),
#             "PRH+VH": OptionItem(4, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }
#         EDEMA_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "Present, not CSME": OptionItem(2, "question.png"),
#             "Present, CSME": OptionItem(3, "question.png"),
#             "Non-Diab": OptionItem(4, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }

#         CTR_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "Present, not CSME": OptionItem(2, "question.png"),
#             "Present, CSME": OptionItem(3, "question.png"),
#             "Non-Diab": OptionItem(4, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }

#         VEN_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "Definite": OptionItem(2, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }

#         LASER_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest/incomplete": OptionItem(1, "question.png"),
#             "Focal": OptionItem(2, "question.png"),
#             "Scatter only": OptionItem(3, "question.png"),
#             "Scatter + Focal": OptionItem(4, "question.png"),
#             "Could grade": OptionItem(8, "question.png"),
#         }
#         RX_options = {
#             "None": OptionItem(0, "question.png"),
#             "Quest": OptionItem(1, "question.png"),
#             "Focal RX only": OptionItem(2, "question.png"),
#             "Grid RX only": OptionItem(3, "question.png"),
#             "Focal + Grid": OptionItem(4, "question.png"),
#             "CG": OptionItem(8, "question.png"),
#         }

#         dict_options = {
#             self.comboBox_HMA: HMA_options,
#             self.comboBox_HE: HE_options,
#             self.comboBox_HE: HE_options,
#             self.comboBox_SE: SE_options,
#             self.comboBox_IRMA: IRMA_options,
#             self.comboBox_VB: VB_options,
#             self.comboBox_NVD: NVD_options,
#             self.comboBox_NVE: NVE_options,
#             self.comboBox_FP: FP_options,
#             self.comboBox_PRH_VH: PRH_VH_options,
#             self.comboBox_EDEMA: EDEMA_options,
#             self.comboBox_CTR: CTR_options,
#             self.comboBox_VEN: VEN_options,
#             self.comboBox_LASER: LASER_options,
#             self.comboBox_RX: RX_options,
#         }

#         for comboBox, options in dict_options.items():
#             comboBox.addItems(list(options.keys()))

from pathlib import Path
from PySide6.QtCore import QRect, QSize, Qt, QPoint, QEvent
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    QComboBox,
    QWidget,
    QApplication,
    QMainWindow,
)
from dataclasses import dataclass
import sys

from MainWindow import Ui_MainWindow


class HoverLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.ToolTip)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: white; border: 1px solid black;")
        self.setVisible(False)

    def show_image(self, image_path, pos):
        pixmap = QPixmap(image_path)
        self.setPixmap(pixmap)
        self.adjustSize()
        self.move(pos)
        self.setVisible(True)

    def hide_image(self):
        self.setVisible(False)


class ComboBoxWithHover(QComboBox):
    def __init__(self, hover_label, options, parent=None):
        super().__init__(parent)
        self.hover_label = hover_label
        self.options = options
        self.view().setMouseTracking(True)
        self.view().viewport().installEventFilter(self)
        self.view().viewport().setAttribute(Qt.WA_Hover)

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseMove and source == self.view().viewport():
            index = self.view().indexAt(event.pos())
            if index.isValid():
                option_text = self.itemText(index.row())
                image_path = self.options[option_text].path
                self.hover_label.show_image(
                    image_path, self.view().mapToGlobal(event.pos() + QPoint(20, 20))
                )
            else:
                self.hover_label.hide_image()
        elif event.type() in (QEvent.HoverLeave, QEvent.Leave):
            self.hover_label.hide_image()
        return super().eventFilter(source, event)


@dataclass(frozen=True)
class OptionItem:
    score: int
    path: str | Path


class MainWindowImpl(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self):
        HMA_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "<std 1": OptionItem(2, "question.png"),
            "≥std 1": OptionItem(3, "question.png"),
            "≥std 2A": OptionItem(4, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }
        HE_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "<std 3": OptionItem(2, "question.png"),
            "≥std 3 - <std 4": OptionItem(2, "question.png"),
            "≥std 4": OptionItem(4, "question.png"),
        }
        SE_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "Definite": OptionItem(2, "question.png"),
        }
        IRMA_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "Definite": OptionItem(2, "question.png"),
            "Definite (all fields)": OptionItem(3, "question.png"),
            "≥std 8A": OptionItem(4, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }
        VB_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "Definite": OptionItem(2, "question.png"),
            "Definite (2+ fields)": OptionItem(3, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }
        NVD_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "<std 10A": OptionItem(2, "question.png"),
            "≥std 10A": OptionItem(3, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }
        NVE_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "<1/2 Disc area": OptionItem(2, "question.png"),
            "≥1/2 Disc area": OptionItem(3, "question.png"),
        }
        FP_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "FPE only": OptionItem(2, "question.png"),
            "FPD only": OptionItem(3, "question.png"),
            "FPD + FPE": OptionItem(4, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }
        PRH_VH_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "PRH only": OptionItem(2, "question.png"),
            "VH only": OptionItem(3, "question.png"),
            "PRH+VH": OptionItem(4, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }
        EDEMA_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "Present, not CSME": OptionItem(2, "question.png"),
            "Present, CSME": OptionItem(3, "question.png"),
            "Non-Diab": OptionItem(4, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }

        CTR_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "Present, not CSME": OptionItem(2, "question.png"),
            "Present, CSME": OptionItem(3, "question.png"),
            "Non-Diab": OptionItem(4, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }

        VEN_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "Definite": OptionItem(2, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }

        LASER_options = {
            "None": OptionItem(0, "question.png"),
            "Quest/incomplete": OptionItem(1, "question.png"),
            "Focal": OptionItem(2, "question.png"),
            "Scatter only": OptionItem(3, "question.png"),
            "Scatter + Focal": OptionItem(4, "question.png"),
            "Could grade": OptionItem(8, "question.png"),
        }
        RX_options = {
            "None": OptionItem(0, "question.png"),
            "Quest": OptionItem(1, "question.png"),
            "Focal RX only": OptionItem(2, "question.png"),
            "Grid RX only": OptionItem(3, "question.png"),
            "Focal + Grid": OptionItem(4, "question.png"),
            "CG": OptionItem(8, "question.png"),
        }

        dict_options = {
            self.ui.comboBox_HMA: HMA_options,
            self.ui.comboBox_HE: HE_options,
            self.ui.comboBox_SE: SE_options,
            self.ui.comboBox_IRMA: IRMA_options,
            self.ui.comboBox_VB: VB_options,
            self.ui.comboBox_NVD: NVD_options,
            self.ui.comboBox_NVE: NVE_options,
            self.ui.comboBox_FP: FP_options,
            self.ui.comboBox_PRH_VH: PRH_VH_options,
            self.ui.comboBox_EDEMA: EDEMA_options,
            self.ui.comboBox_CTR: CTR_options,
            self.ui.comboBox_VEN: VEN_options,
            self.ui.comboBox_LASER: LASER_options,
            self.ui.comboBox_RX: RX_options,
        }

        self.hover_label = HoverLabel()

        for comboBox, options in dict_options.items():
            hover_combo_box = ComboBoxWithHover(self.hover_label, options)
            hover_combo_box.addItems(list(options.keys()))

            layout = comboBox.parentWidget().layout()
            layout.replaceWidget(comboBox, hover_combo_box)
            comboBox.deleteLater()

            # Update reference to the new combo box
            setattr(self, comboBox.objectName(), hover_combo_box)
            
