from datetime import datetime
from pathlib import Path
from PySide6.QtCore import QDate, Qt, QPoint, QEvent
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QFileDialog,
    QLabel,
    QComboBox,
    QMainWindow,
)
from dataclasses import dataclass
from MainWindow import Ui_MainWindow


@dataclass(frozen=True)
class OptionScoreImgPath:
    score: int
    path: str | Path


class MainWindowImpl(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.connect()
        self.before_quit()

    def init_ui(self):
        """init the application UI"""
        self.app = QApplication.instance()
        self._init_tip_button()
        self._init_window()
        self._init_option_button()
        self._init_menu()
        self._init_app()
        self._init_clear_button()
        self._init_visit_date()

        # g1 = QButtonGroup(self.ui.radioButton.parent())
        # g1.addButton(self.ui.radioButton)
        # g1.addButton(self.ui.radioButton_2)

        # g2 = QButtonGroup(self.ui.radioButton_3.parent())
        # g2.addButton(self.ui.radioButton_3)
        # g2.addButton(self.ui.radioButton_4)

    def connect(self):
        self.ui.folder_button.clicked.connect(self.click_folder_button)

    def before_quit(self):
        pass

    def click_folder_button(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, "Select the data folder", "./"
        )
        if folder_path:
            self.ui.folder_line.setText(folder_path)

    def click_clear_button(self):

        # clear comboboxes selection
        for combobox in self.ui.list_comboboxes:
            combobox.setCurrentIndex(-1)

        # clear comment box text
        self.ui.textEdit_comment.clear()

    def _init_comboboxes_options(self):
        self.options_HMA = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "<std 1": OptionScoreImgPath(2, "question.png"),
            "≥std 1": OptionScoreImgPath(3, "question.png"),
            "≥std 2A": OptionScoreImgPath(4, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }
        self.options_HE = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "<std 3": OptionScoreImgPath(2, "question.png"),
            "≥std 3 - <std 4": OptionScoreImgPath(2, "question.png"),
            "≥std 4": OptionScoreImgPath(4, "question.png"),
        }
        self.options_SE = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "Definite": OptionScoreImgPath(2, "question.png"),
        }
        self.options_IRMA = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "Definite": OptionScoreImgPath(2, "question.png"),
            "Definite (all fields)": OptionScoreImgPath(3, "question.png"),
            "≥std 8A": OptionScoreImgPath(4, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }
        self.options_VB = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "Definite": OptionScoreImgPath(2, "question.png"),
            "Definite (2+ fields)": OptionScoreImgPath(3, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }
        self.options_NVD = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "<std 10A": OptionScoreImgPath(2, "question.png"),
            "≥std 10A": OptionScoreImgPath(3, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }
        self.options_NVE = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "<1/2 Disc area": OptionScoreImgPath(2, "question.png"),
            "≥1/2 Disc area": OptionScoreImgPath(3, "question.png"),
        }
        self.options_FP = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "FPE only": OptionScoreImgPath(2, "question.png"),
            "FPD only": OptionScoreImgPath(3, "question.png"),
            "FPD + FPE": OptionScoreImgPath(4, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }
        self.options_PRH_VH = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "PRH only": OptionScoreImgPath(2, "question.png"),
            "VH only": OptionScoreImgPath(3, "question.png"),
            "PRH+VH": OptionScoreImgPath(4, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }
        self.options_EDEMA = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "Present, not CSME": OptionScoreImgPath(2, "question.png"),
            "Present, CSME": OptionScoreImgPath(3, "question.png"),
            "Non-Diab": OptionScoreImgPath(4, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }

        self.options_CTR = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "Present, not CSME": OptionScoreImgPath(2, "question.png"),
            "Present, CSME": OptionScoreImgPath(3, "question.png"),
            "Non-Diab": OptionScoreImgPath(4, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }

        self.options_VEN = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "Definite": OptionScoreImgPath(2, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }

        self.options_LASER = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest/incomplete": OptionScoreImgPath(1, "question.png"),
            "Focal": OptionScoreImgPath(2, "question.png"),
            "Scatter only": OptionScoreImgPath(3, "question.png"),
            "Scatter + Focal": OptionScoreImgPath(4, "question.png"),
            "Could grade": OptionScoreImgPath(8, "question.png"),
        }
        self.options_RX = {
            "None": OptionScoreImgPath(0, "question.png"),
            "Quest": OptionScoreImgPath(1, "question.png"),
            "Focal RX only": OptionScoreImgPath(2, "question.png"),
            "Grid RX only": OptionScoreImgPath(3, "question.png"),
            "Focal + Grid": OptionScoreImgPath(4, "question.png"),
            "CG": OptionScoreImgPath(8, "question.png"),
        }

    def _init_tip_button(self):
        # 提示demo
        self.ui.pushButton_HMA.setToolTip("introduction of HMA")

    def _init_window(self):
        self.setWindowTitle("Diabetic Retinopathy Grading App")
        self.setWindowIcon(QIcon("icon.png"))

    def _init_visit_date(self):
        date = datetime.now().date()
        year, month, day = date.year, date.month, date.day
        self.ui.dateEdit_Visit_data.setDate(QDate.currentDate())

    def _init_option_button(self):
        self._init_comboboxes_options()
        dict_comboboxes = {
            self.ui.comboBox_HMA: self.options_HMA,
            self.ui.comboBox_HE: self.options_HE,
            self.ui.comboBox_SE: self.options_SE,
            self.ui.comboBox_IRMA: self.options_IRMA,
            self.ui.comboBox_VB: self.options_VB,
            self.ui.comboBox_NVD: self.options_NVD,
            self.ui.comboBox_NVE: self.options_NVE,
            self.ui.comboBox_FP: self.options_FP,
            self.ui.comboBox_PRH_VH: self.options_PRH_VH,
            self.ui.comboBox_EDEMA: self.options_EDEMA,
            self.ui.comboBox_CTR: self.options_CTR,
            self.ui.comboBox_VEN: self.options_VEN,
            self.ui.comboBox_LASER: self.options_LASER,
            self.ui.comboBox_RX: self.options_RX,
        }

        self.hover_label = HoverLabel()

        self.ui.list_comboboxes = []
        for comboBox, options in dict_comboboxes.items():
            hover_combobox = ComboBoxWithHover(self.hover_label, options)
            hover_combobox.addItems(list(options.keys()))

            layout = comboBox.parentWidget().layout()
            layout.replaceWidget(comboBox, hover_combobox)
            comboBox.deleteLater()

            # Update reference to the new combobox
            setattr(self, comboBox.objectName(), hover_combobox)

            hover_combobox.setCurrentIndex(-1)
            self.ui.list_comboboxes.append(hover_combobox)

    def _init_menu(self):
        self.ui.menu = self.menuBar()
        self.ui.menu_file = self.ui.menu.addMenu("File")

        # 重构成使用addActions和QAction
        self.ui.menu_file_openfolder = self.ui.menu_file.addAction("Open Folder...")
        self.ui.menu_file_save = self.ui.menu_file.addAction("Save...")
        self.ui.menu_file_exit = self.ui.menu_file.addAction("Exit...")

        self.ui.menu_help = self.ui.menu.addMenu("help")
        self.ui.menu_help_about = self.ui.menu_help.addAction("About")
        self.ui.menu_file_openfolder.triggered.connect(self.click_folder_button)

    def _init_app(self):
        app = QApplication.instance()
        app.setStyle("fusion")

    def _init_clear_button(self):
        self.ui.pushButton_clear.clicked.connect(self.click_clear_button)
        self.ui.pushButton_clear


# class HoverLabel(QLabel):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowFlags(Qt.ToolTip)
#         self.setAlignment(Qt.AlignCenter)
#         self.setStyleSheet("background-color: white; border: 1px solid black;")
#         self.setVisible(False)

#     def show_image(self, image_path, pos):
#         pixmap = QPixmap(image_path)
#         self.setPixmap(pixmap)
#         self.adjustSize()
#         self.move(pos - QPoint(self.width() + 20, 0))
#         self.setVisible(True)

#     def hide_image(self):
#         self.setVisible(False)


# class ComboBoxWithHover(QComboBox):
#     def __init__(self, hover_label, options, parent=None):
#         super().__init__(parent)
#         self.hover_label = hover_label
#         self.options = options
#         self.view().setMouseTracking(True)
#         self.view().viewport().installEventFilter(self)
#         self.view().viewport().setAttribute(Qt.WA_Hover)

#     def eventFilter(self, source, event):
#         if event.type() == QEvent.MouseMove and source == self.view().viewport():
#             index = self.view().indexAt(event.pos()) 
#             if index.isValid():
#                 option_text = self.itemText(index.row())
#                 image_path = self.options[option_text].path
#                 self.hover_label.show_image(
#                     image_path, self.view().mapToGlobal(event.pos() + QPoint(20, 20))
#                 )
#             else:
#                 self.hover_label.hide_image()
#         elif event.type() in (QEvent.HoverLeave, QEvent.Leave):
#             self.hover_label.hide_image()
#         return super().eventFilter(source, event)


class HoverLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.ToolTip)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: white; border: 1px solid black;")
        self.setVisible(False)

    def show_image(self, image_path, item_rect_top_left):
        pixmap = QPixmap(image_path)
        self.setPixmap(pixmap)
        self.adjustSize()
        # Adjust position to show image on the left side of the item rectangle
        self.move(item_rect_top_left - QPoint(self.width() + 10, 0))
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
                item_rect = self.view().visualRect(index)
                item_rect_top_left = self.view().mapToGlobal(item_rect.topLeft())
                self.hover_label.show_image(image_path, item_rect_top_left)
            else:
                self.hover_label.hide_image()
        elif event.type() in (QEvent.HoverLeave, QEvent.Leave):
            self.hover_label.hide_image()
        return super().eventFilter(source, event)