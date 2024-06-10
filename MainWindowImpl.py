# mainwindowimpl.py
import json
from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QListWidgetItem,
    QMessageBox,
    QTextEdit,
    QTreeWidgetItem,
    QWidget,
)
from mainwindow import MainWindow
import gradwidget, setwidget
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from util import OptionScoreImgPath, get_folder_contents_df

# from mainwindowimpl import MainWindowImpl
from ComboboxWithHover import ComboBoxWithHover, HoverLabel
import pandas as pd


user_data = {"1": "1"}


class MainWindowImpl(MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui_impl()

        # disable password
        self.islogin = True

    def init_ui_impl(self):
        # self._init_grad_set()
        self._init_gradwidge()
        self._init_setwidge()
        self._init_comboboxes()
        self._init_app()
        self._init_login_button()
        self._init_folder_button()

        # 放在最后, 因为需要连接其他控件
        self._init_menu()
        self.islogin = False

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
            setattr(self, comboBox.objectName(), hover_combobox)
            hover_combobox.setCurrentIndex(-1)
            self.grad.list_comboboxes.append(hover_combobox)

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
            self.popup_ask_to_login()

    def _init_folder_button(self):
        self.set.folder_button.clicked.connect(self.select_folder)
        self.set.folder_button.clicked.connect(self.get_df)
        self.set.folder_button.clicked.connect(self.show_patients_tree)
        self.set.treeWidget_patient.itemClicked.connect(self.on_item_clicked)

    def _init_login_button(self):
        self.set.pushButton_login.clicked.connect(self.login_user)

    def load_patient_list(self):
        self.set.treeWidget.addTopLevelItems(QTreeWidgetItem())

    def get_df(self):
        self.df = get_folder_contents_df(self.set.folder_path)

    def on_item_clicked(self, item, column):
        if item.childCount() == 0:  # 如果点击的是 visit_date 项目
            visit_date = item.data(0, 1)
            self.show_file_path(visit_date)

    def show_file_path(self, visit_date):
        self.set.listWidget_img_path.clear()
        filtered_df = self.df[self.df["visit_date"] == visit_date]

        for path in filtered_df.loc[:, "file_path"]:
            item = QListWidgetItem(Path(path).name)
            item.setToolTip(path)
            self.set.listWidget_img_path.addItem(item)

    def login_user(self):

        user = self.set.lineEdit_user.text()
        password = self.set.lineEdit_password.text()

        if user in user_data and user_data[user] == password:
            QMessageBox.information(self, "Success", "Login successful!")
            self.islogin = True

        else:
            QMessageBox.warning(self, "Error", "Invalid username or password!")

    def show_patients_tree(self):

        grouped = self.df.groupby("patient_id")
        for patient_id, group in grouped:
            # 创建顶级条目
            patient_item = QTreeWidgetItem([patient_id])
            self.set.treeWidget_patient.addTopLevelItem(patient_item)

            # 添加 visit_date 条目
            visit_dates = group["visit_date"].unique()

            for visit_date in visit_dates:
                visit_date_item = QTreeWidgetItem([visit_date])
                patient_item.addChild(visit_date_item)
                visit_date_item.setData(0, 1, visit_date)

    def popup_ask_to_login(self):
        QMessageBox.warning(self, "Error", "Please login!")

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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mwImpl = MainWindowImpl()
    mwImpl.show()

    sys.exit(app.exec())
