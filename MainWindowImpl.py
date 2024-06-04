from pathlib import Path
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QComboBox,
    QMainWindow,
)
from dataclasses import dataclass
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
class OptionScoreImgPath:
    score: int
    path: str | Path
    

# @dataclass(frozen=True)
# class ComboBoxOptionsItem:
#     labels: str
#     score_img_path: OptionScoreImgPath

# @dataclass(frozen=True)
# class ComboBoxOptions:
#     labels: 



class MainWindowImpl(QMainWindow):
    HMA_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "<std 1": OptionScoreImgPath(2, "question.png"),
        "≥std 1": OptionScoreImgPath(3, "question.png"),
        "≥std 2A": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    HE_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "<std 3": OptionScoreImgPath(2, "question.png"),
        "≥std 3 - <std 4": OptionScoreImgPath(2, "question.png"),
        "≥std 4": OptionScoreImgPath(4, "question.png"),
    }
    SE_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Definite": OptionScoreImgPath(2, "question.png"),
    }
    IRMA_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Definite": OptionScoreImgPath(2, "question.png"),
        "Definite (all fields)": OptionScoreImgPath(3, "question.png"),
        "≥std 8A": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    VB_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Definite": OptionScoreImgPath(2, "question.png"),
        "Definite (2+ fields)": OptionScoreImgPath(3, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    NVD_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "<std 10A": OptionScoreImgPath(2, "question.png"),
        "≥std 10A": OptionScoreImgPath(3, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    NVE_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "<1/2 Disc area": OptionScoreImgPath(2, "question.png"),
        "≥1/2 Disc area": OptionScoreImgPath(3, "question.png"),
    }
    FP_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "FPE only": OptionScoreImgPath(2, "question.png"),
        "FPD only": OptionScoreImgPath(3, "question.png"),
        "FPD + FPE": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    PRH_VH_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "PRH only": OptionScoreImgPath(2, "question.png"),
        "VH only": OptionScoreImgPath(3, "question.png"),
        "PRH+VH": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    EDEMA_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Present, not CSME": OptionScoreImgPath(2, "question.png"),
        "Present, CSME": OptionScoreImgPath(3, "question.png"),
        "Non-Diab": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }

    CTR_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Present, not CSME": OptionScoreImgPath(2, "question.png"),
        "Present, CSME": OptionScoreImgPath(3, "question.png"),
        "Non-Diab": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }

    VEN_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Definite": OptionScoreImgPath(2, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }

    LASER_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest/incomplete": OptionScoreImgPath(1, "question.png"),
        "Focal": OptionScoreImgPath(2, "question.png"),
        "Scatter only": OptionScoreImgPath(3, "question.png"),
        "Scatter + Focal": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    RX_OPTIONS = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Focal RX only": OptionScoreImgPath(2, "question.png"),
        "Grid RX only": OptionScoreImgPath(3, "question.png"),
        "Focal + Grid": OptionScoreImgPath(4, "question.png"),
        "CG": OptionScoreImgPath(8, "question.png"),
    }

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.InitUI()

        self.ui.folder_button.clicked.connect(self.select_folder)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            self.ui.folder_line.setText(folder_path)

    def InitUI(self):
        dict_options = {
            self.ui.comboBox_HMA: self.HMA_OPTIONS,
            self.ui.comboBox_HE: self.HE_OPTIONS,
            self.ui.comboBox_SE: self.SE_OPTIONS,
            self.ui.comboBox_IRMA: self.IRMA_OPTIONS,
            self.ui.comboBox_VB: self.VB_OPTIONS,
            self.ui.comboBox_NVD: self.NVD_OPTIONS,
            self.ui.comboBox_NVE: self.NVE_OPTIONS,
            self.ui.comboBox_FP: self.FP_OPTIONS,
            self.ui.comboBox_PRH_VH: self.PRH_VH_OPTIONS,
            self.ui.comboBox_EDEMA: self.EDEMA_OPTIONS,
            self.ui.comboBox_CTR: self.CTR_OPTIONS,
            self.ui.comboBox_VEN: self.VEN_OPTIONS,
            self.ui.comboBox_LASER: self.LASER_OPTIONS,
            self.ui.comboBox_RX: self.RX_OPTIONS,
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
