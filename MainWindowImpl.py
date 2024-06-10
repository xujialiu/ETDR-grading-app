# mainwindowimpl.py
from copy import copy
from doctest import debug
import json
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QListWidgetItem,
    QMessageBox,
    QTextEdit,
    QTreeWidgetItem,
    QWidget,
)
from networkx import dfs_edges
from mainwindow import MainWindow
import gradwidget, setwidget
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from util import OptionScoreImgPath, get_df_folder_contents, load_or_create_df_dataset

# from mainwindowimpl import MainWindowImpl
from ComboboxWithHover import ComboBoxWithHover, HoverLabel
import pandas as pd


user_data = {"1": "1"}


class MainWindowImpl(MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui_impl()
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("Diabetic Retinopathy Grading System")
        # disable password
        self.islogin = True

    def init_ui_impl(self):
        self._init_gradwidge()
        self._init_setwidge()
        self._init_comboboxes()
        self._init_app()
        self._init_login_button()
        self._init_folder_button()
        self._init_patients_tree()
        self.get_df_dataset()
        self._init_save_button()

        # 放在最后, 因为需要连接其他控件
        self._init_menu()
        self.islogin = False
        self.debug_button(hide=False)

    def _init_setwidge(self):
        self.set = setwidget.Ui_MainWindow()
        self.set.setupUi(self)
        self.tabwidget.addTab(self.set.centralwidget, "Settings")

    def _init_gradwidge(self):
        self.grad = gradwidget.Ui_MainWindow()
        self.grad.setupUi(self)
        self.tabwidget.addTab(self.grad.centralwidget, "Grading Area")

    def _init_comboboxes(self):
        self.comboboxes_options()

        dict_comboboxes = {
            self.grad.comboBox_HMA: self.options_HMA,
            self.grad.comboBox_HE: self.options_HE,
            self.grad.comboBox_SE: self.options_SE,
            self.grad.comboBox_IRMA: self.options_IRMA,
            self.grad.comboBox_VB: self.options_VB,
            self.grad.comboBox_NVD: self.options_NVD,
            self.grad.comboBox_NVE: self.options_NVE,
            self.grad.comboBox_FP: self.options_FP,
            self.grad.comboBox_PRH_VH: self.options_PRH_VH,
            self.grad.comboBox_EDEMA: self.options_EDEMA,
            self.grad.comboBox_CTR: self.options_CTR,
            self.grad.comboBox_VEN: self.options_VEN,
            self.grad.comboBox_LASER: self.options_LASER,
            self.grad.comboBox_RX: self.options_RX,
        }
        self.hover_label = HoverLabel()

        self.grad.list_comboboxes = []
        for comboBox, options in dict_comboboxes.items():
            hover_combobox = ComboBoxWithHover(self.hover_label, options)
            hover_combobox.addItems(list(options.keys()))

            layout = comboBox.parentWidget().layout()
            layout.replaceWidget(comboBox, hover_combobox)
            comboBox.deleteLater()

            # Update reference to the new combobox
            setattr(
                self.grad, comboBox.objectName(), hover_combobox
            )  # 绑定到新的变量上
            hover_combobox.setCurrentIndex(-1)
            self.grad.list_comboboxes.append(hover_combobox)

        self.dict_comboboxes = {
            "HMA": [self.grad.comboBox_HMA, self.options_HMA],
            "HE": [self.grad.comboBox_HE, self.options_HE],
            "SE": [self.grad.comboBox_SE, self.options_SE],
            "IRMA": [self.grad.comboBox_IRMA, self.options_IRMA],
            "VB": [self.grad.comboBox_VB, self.options_VB],
            "NVD": [self.grad.comboBox_NVD, self.options_NVD],
            "NVE": [self.grad.comboBox_NVE, self.options_NVE],
            "FP": [self.grad.comboBox_FP, self.options_FP],
            "PRH_VH": [self.grad.comboBox_PRH_VH, self.options_PRH_VH],
            "EDEMA": [self.grad.comboBox_EDEMA, self.options_EDEMA],
            "CTR": [self.grad.comboBox_CTR, self.options_CTR],
            "VEN": [self.grad.comboBox_VEN, self.options_VEN],
            "LASER": [self.grad.comboBox_LASER, self.options_LASER],
            "RX": [self.grad.comboBox_RX, self.options_RX],
        }

    def _init_app(self):
        app = QApplication.instance()
        app.setStyle("fusion")

    def _init_menu(self):
        self.menu = self.menuBar()
        self.menu_file = self.menu.addMenu("File")

        # 重构成使用addActions和QAction
        self.menu_file_openfolder = self.menu_file.addAction("Open Folder...")
        self.menu_file_save = self.menu_file.addAction("Save...")
        self.menu_file_exit = self.menu_file.addAction("Exit...")

        self.menu_help = self.menu.addMenu("help")
        self.menu_help_about = self.menu_help.addAction("About")
        self.menu_file_openfolder.triggered.connect(self.select_folder)

    def select_folder(self):
        if self.islogin:
            self.set.folder_path = QFileDialog.getExistingDirectory(
                self, "Select the data folder", "./"
            )
            if self.set.folder_path:
                self.set.label_folder.setText(self.set.folder_path)

        else:
            QMessageBox.warning(self, "Error", "Please login!")

    def _init_folder_button(self):
        self.set.folder_button.clicked.connect(self.select_folder)
        self.set.folder_button.clicked.connect(self.get_df)
        self.set.folder_button.clicked.connect(self.show_patients_tree)

    def _init_patients_tree(self):
        self.set.treeWidget_patient.itemClicked.connect(self.on_visit_date_clicked)

    def _init_login_button(self):
        self.set.pushButton_login.clicked.connect(self.login_user)

    def get_df_dataset(self):
        self.df_dataset = load_or_create_df_dataset()

    def get_df(self):
        self.df = get_df_folder_contents(self.set.folder_path)

    def login_user(self):

        user = self.set.lineEdit_user.text()
        password = self.set.lineEdit_password.text()

        if user in user_data and user_data[user] == password:
            QMessageBox.information(self, "Success", "Login successful!")
            self.islogin = True

        else:
            QMessageBox.warning(self, "Error", "Invalid username or password!")

    def show_patients_tree(self):
        self.set.treeWidget_patient.clear()
        grouped = self.df.groupby("patient_id")
        for patient_id, group in grouped:
            # 创建顶级条目
            patient_item = QTreeWidgetItem([patient_id])
            self.set.treeWidget_patient.addTopLevelItem(patient_item)

            # 获取 unique 的 visit_date 和 eye 组合
            visit_date_eye_combinations = (
                group[["visit_date", "eye"]].drop_duplicates().values
            )

            for visit_date, eye in visit_date_eye_combinations:
                visit_date_eye_item = QTreeWidgetItem([f"{visit_date} {eye}"])
                patient_item.addChild(visit_date_eye_item)
                visit_date_eye_item.setData(0, 1, visit_date)

    def on_visit_date_clicked(self, item, column):
        if item.childCount() == 0:  # 如果点击的是 visit_date (eye) item

            # 获取点击的visit_date, eye和patient_id
            self.visit_date, self.eye = item.text(0).split()
            self.patien_id = item.parent().text(0)

            self.show_file_path(self.visit_date, self.eye)

    def show_file_path(self, visit_date, eye):
        self.set.listWidget_img_path.clear()
        filtered_df = self.df[
            (self.df["visit_date"] == visit_date) & (self.df["eye"] == eye)
        ]

        for path in filtered_df.loc[:, "file_path"]:
            item = QListWidgetItem(Path(path).name)
            item.setToolTip(path)
            self.set.listWidget_img_path.addItem(item)

    def _init_save_button(self):
        self.grad.pushButton_save.clicked.connect(self.on_save_click)



    def on_save_click(self):

        comboboxs_choices = [
            list_combobox[0].currentText()
            for list_combobox in self.dict_comboboxes.values()
        ]
        if not self.islogin:
            QMessageBox.warning(self, "Error", "Please login!")
        elif not all(comboboxs_choices):
            QMessageBox.warning(self, "Error", "Please fill all options!")

        dict_results = {
            label: list_combobox[0].currentText()
            for label, list_combobox in self.dict_comboboxes.items()
        }
        self.update_dict_results(dict_results)

        self.update_df_database(dict_results)
        print(self.df_dataset)  # 写到这里

    def update_df_database(self, dict_results):
        df_data = pd.DataFrame([dict_results])
        self.df_dataset = pd.concat([self.df_dataset, df_data])

    def update_dict_results(self, dict_results):
        dict_scores = {}
        for key, label in dict_results.items():
            options = getattr(self, f"options_{key}")
            dict_scores[f"{key}_score"] = options[label].score
        dict_results.update(dict_scores)

        dict_results["comment"] = self.grad.textEdit_comment.toPlainText()
        dict_results["patient_id"] = self.patien_id
        dict_results["visit_date"] = self.visit_date
        dict_results["eye"] = self.eye

    def comboboxes_options(self):
        with open("combobox_options.json", "r", encoding="utf-8") as f:
            options_data = json.load(f)

        self.options_HMA = self._parse_options(options_data["HMA"])
        self.options_HE = self._parse_options(options_data["HE"])
        self.options_SE = self._parse_options(options_data["SE"])
        self.options_IRMA = self._parse_options(options_data["IRMA"])
        self.options_VB = self._parse_options(options_data["VB"])
        self.options_NVD = self._parse_options(options_data["NVD"])
        self.options_NVE = self._parse_options(options_data["NVE"])
        self.options_FP = self._parse_options(options_data["FP"])
        self.options_PRH_VH = self._parse_options(options_data["PRH_VH"])
        self.options_EDEMA = self._parse_options(options_data["EDEMA"])
        self.options_CTR = self._parse_options(options_data["CTR"])
        self.options_VEN = self._parse_options(options_data["VEN"])
        self.options_LASER = self._parse_options(options_data["LASER"])
        self.options_RX = self._parse_options(options_data["RX"])

    def _parse_options(self, options_dict):
        return {
            key: OptionScoreImgPath(value["score"], value["image"])
            for key, value in options_dict.items()
        }

    # debug button
    def debug_button(self, hide=True):
        self.set.pushButton_debug.clicked.connect(self.debug_func)
        if hide:
            self.set.pushButton_debug.hide()

    def debug_func(self):
        a = self.set.treeWidget_patient.currentItem()
        print(self.options_HE)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    mwImpl = MainWindowImpl()
    mwImpl.show()

    sys.exit(app.exec())
