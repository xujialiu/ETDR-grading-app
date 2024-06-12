# mainwindowimpl.py
# [[feat]]: 增加export 按键

import json
from pathlib import Path
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QFileDialog,
    QListWidgetItem,
    QMessageBox,
    QTabWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
)
import numpy as np
from MainWindow import MainWindow
import GradWidget, SetWidget
import sys
from PySide6.QtWidgets import QApplication
from util import (
    OptionScoreImgPath,
    get_df_folder_contents,
    load_or_create_df_database,
    load_or_create_df_graded,
)
from ComboboxWithHover import ComboBoxWithHover, HoverLabel
import pandas as pd
from DebugWindow import DebugWindow
from pyqtgraph import ImageItem, GraphicsLayoutWidget
from PIL import Image

user_data = {"1": "1"}


class MainWindowImpl(MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui_impl()
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("Diabetic Retinopathy Grading System")

        # disable password
        self.islogin = True  # testing...发行版删除该行
        self.user = "xujialiu"  # testing...发行版删除该行

        # 数据注入
        # self.df_database = pd.read_pickle(".data/test_data.pkl")

    def init_ui_impl(self):
        self._init_tabs()
        self._init_gradwidge()
        self._init_setwidge()
        self._init_comboboxes()
        self._init_app()
        self._init_clear_button()
        self._init_login_button()
        self._init_folder_button()
        self._init_patients_tree()
        self._init_df_database()
        self._init_df_graded()
        self._init_save_button()

        # 放在最后, 因为需要连接其他控件
        self._init_menu()
        self.islogin = False

    def closeEvent(self, event):
        if not self.df_database.empty:
            self.df_database.astype(str).to_hdf(
                ".data/database.hdf5", key="df_database", mode="w"
            )

            self.df_graded.to_hdf(".data/database.hdf5", key="df_graded", mode="a")

    def _init_tabs(self):

        # set right dock
        self.tabwidget = QTabWidget(self)
        self.right_dock.setWidget(self.tabwidget)

        self._init_img_widget()
        # set left dock
        self.left_dock.setWidget(self.img_widget)

    def _init_img_widget(self):
        # 创建一个GraphicsLayoutWidget
        self.img_widget = GraphicsLayoutWidget()
        self.setCentralWidget(self.img_widget)

        # 添加一个PlotItem
        self.plot_item = self.img_widget.addPlot()

        # 禁用坐标轴
        self.plot_item.hideAxis("left")
        self.plot_item.hideAxis("bottom")

        # 添加一个ImageItem
        self.img_item = ImageItem()
        self.plot_item.addItem(self.img_item)

        # 加载图像
        img = Image.open("icon.png")
        img = np.array(img)
        img = np.rot90(img, -1)
        self.img_item.setImage(img)

        # 设置放大缩小功能
        self.plot_item.getViewBox().setMouseEnabled(x=True, y=True)
        self.plot_item.getViewBox().setAspectLocked(True)

        # 设置放大缩小功能
        self.plot_item.getViewBox().setMouseEnabled(x=True, y=True)
        self.plot_item.getViewBox().setAspectLocked(True)

    def _init_setwidge(self):
        self.set = SetWidget.Ui_MainWindow()
        self.set.setupUi(self)
        self.tabwidget.addTab(self.set.centralwidget, "Settings")

    def _init_gradwidge(self):
        self.grad = GradWidget.Ui_MainWindow()
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

            setattr(
                self.grad, comboBox.objectName(), hover_combobox
            )  # 绑定到新的变量上
            hover_combobox.setCurrentIndex(1)  # testing...发行版改为-1
            hover_combobox.currentTextChanged.connect(self.displace_total_score)

            self.grad.list_comboboxes.append(hover_combobox)

            # [[feat]]: 增加text改变时, 计算总分并显示总分的功能

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

    def displace_total_score(self):
        # print(self.options_HMA)
        self.calculate_total_score()
        self.grad.label_score.setText(f"Total score: {self.total_score}")

    def calculate_total_score(self):
        # list_combobox = [for _,(com)]
        list_comboboxes = []
        list_options = []
        for _, (combobox, option) in self.dict_comboboxes.items():
            list_comboboxes.append(combobox)
            list_options.append(option)
            # self.grad.comboBox_PRH_VH.currentText()
        list_text = [combobox.currentText() for combobox in list_comboboxes]
        list_score = [
            option.get(text, OptionScoreImgPath(score=0, path="")).score
            for option, text in zip(list_options, list_text)
        ]
        self.total_score = sum(list_score)

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
        self.menu_help_about = self.menu_help.addAction("Debug")

        self.menu_file_openfolder.triggered.connect(self.select_folder)
        self.menu_help_about.triggered.connect(self.on_debug_click)
        # [[feat]]: 做About页面
        # [[feat]]: Exit

    def on_debug_click(self):
        self.debug_window = DebugWindow()
        self.debug_window.code_submitted.connect(self.execute_code)
        self.debug_window.show()

    @Slot(str)
    def execute_code(self, code):
        try:
            exec(f"print({code})")
        except Exception as e:
            print(e)

    def select_folder(self):
        if not self.islogin:
            QMessageBox.warning(self, "Error", "Please login!")
        else:
            self.set.folder_path = QFileDialog.getExistingDirectory(
                self, "Select the data folder", "./"
            )
            if self.set.folder_path:
                self.set.label_folder.setText(self.set.folder_path)

    def show_grad_labels(self):
        self.grad.label_eye.setText(f"Eye: {self.eye}")
        self.grad.label_patient_id.setText(f"Patient ID: {self.patient_id}")
        self.grad.label_user.setText(f"Grader: {self.user}")
        self.grad.label_visit_date.setText(f"Visit date: {self.visit_date}")

    def _init_folder_button(self):
        self.set.folder_button.clicked.connect(self.select_folder)
        self.set.folder_button.clicked.connect(self.get_df)
        self.set.folder_button.clicked.connect(self.show_patients_tree)
        self.set.folder_button.clicked.connect(self.find_first_tree_item)
        self.set.folder_button.clicked.connect(self.show_grad_labels)
        self.set.folder_button.clicked.connect(self.show_df_graded_df_database)

    def _init_df_graded(self):
        """储存graded的患者信息, 包括patient_id, visit_date, eye"""
        self.df_graded = load_or_create_df_graded()

    def _init_patients_tree(self):
        self.set.treeWidget_patient.itemClicked.connect(self.on_visit_date_clicked)

    def _init_login_button(self):
        self.set.pushButton_login.clicked.connect(self.login_user)

    def _init_save_button(self):
        self.grad.pushButton_save.clicked.connect(self.on_save_click)
        # self.grad.pushButton_save.clicked.connect(self.on_clear_click)    # testing...发行版中取消注释

    def _init_df_database(self):
        self.df_database = load_or_create_df_database()

    def get_df(self):
        self.df = get_df_folder_contents(self.set.folder_path)
        self.df_remove_row_in_df_graded()

    def login_user(self):
        self.user = self.set.lineEdit_user.text()
        password = self.set.lineEdit_password.text()

        if self.user in user_data and user_data[self.user] == password:
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

            self.set.treeWidget_patient.sortItems(0, Qt.AscendingOrder)

    def on_visit_date_clicked(self, item, column):
        if item.childCount() == 0:  # 如果点击的是 visit_date (eye) item

            # 获取点击的visit_date, eye和patient_id
            self.visit_date, self.eye = item.text(0).split()
            self.patient_id = item.parent().text(0)

    def _init_clear_button(self):
        self.grad.pushButton_clear.clicked.connect(self.on_clear_click)

    def on_clear_click(self):
        comboboxes = (combobox for _, (combobox, _) in self.dict_comboboxes.items())
        for combobox in comboboxes:
            combobox.setCurrentIndex(-1)

    def show_df_graded_df_database(self):
        self.show_df_database()
        self.show_df_graded()

    def show_df_graded(self):
        self.add_df_to_qtable(self.df_graded, self.set.tableWidget_graded)

    def show_df_database(self):
        self.add_df_to_qtable(self.df_database, self.set.tableWidget_database)

    @staticmethod
    def add_df_to_qtable(df: pd.DataFrame, table: QTreeWidget):

        df.reset_index(drop=True, inplace=True)
        table.setRowCount(len(df))
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(df.columns)

        for row_index, row in df.iterrows():
            for col_index, value in enumerate(row):
                table.setItem(row_index, col_index, QTableWidgetItem(str(value)))

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

        self.update_df_graded()

        self.update_df()
        self.show_patients_tree()
        self.find_and_activate_tree_item()
        self.show_df_graded_df_database()

    def find_and_activate_tree_item(self):
        """
        定位到新的行:
        1. 如果self.patient_id还在self.df, 转到第一个visit_date
        2. 如果self.patient_id已经不在self.df里, 转到第一个visit_date的第一个值
        """
        # 列表为空时, 提前返回
        if len(self.df) == 0:
            QMessageBox.information(
                self, "Success", "Congratulations! You finish all patients grading!"
            )
            return

        if self.patient_id in self.df.patient_id.to_numpy():

            # 遍历顶层项目
            for i in range(self.set.treeWidget_patient.topLevelItemCount()):
                top_level_item = self.set.treeWidget_patient.topLevelItem(i)
                if top_level_item.text(0) == self.patient_id:
                    # 直接返回第一个
                    self.item = top_level_item.child(0)
                    self.visit_date, self.eye = self.item.text(0).split()
                    self.set.treeWidget_patient.setCurrentItem(self.item)
                    self.set.treeWidget_patient.scrollToItem(
                        self.item, QTreeWidget.PositionAtCenter
                    )
        else:
            self.find_first_tree_item()

    def find_first_tree_item(self):
        try:
            self.patient_id = self.df.patient_id.iloc[0]
            self.item = self.set.treeWidget_patient.topLevelItem(0).child(0)
            self.set.treeWidget_patient.setCurrentItem(self.item)
            self.set.treeWidget_patient.scrollToItem(
                self.item, QTreeWidget.PositionAtCenter
            )
            self.visit_date, self.eye = self.item.text(0).split()
        except IndexError as e:
            QMessageBox.information(self, "Warning", "Do not find ungraded patient.")

    def update_df(self):
        df_mask = self.get_df_mask()
        self.df = self.df[~df_mask]

    def get_df_mask(self):
        """返回一个根据patient_id, visit_date, eye的全是布尔值的dataframe"""
        return (
            (self.df.patient_id == self.patient_id)
            & (self.df.visit_date == self.visit_date)
            & (self.df.eye == self.eye)
        )

    def df_remove_row_in_df_graded(self):
        """去除df中, 已包含在df_graded中的行"""
        # 合并两个DataFrame，并标记出第二个DataFrame中的行
        merged_df = self.df.merge(
            self.df_graded,
            on=["patient_id", "visit_date", "eye"],
            how="left",
            indicator=True,
        )

        # 过滤掉存在于第二个DataFrame中的行
        result_df = merged_df[merged_df["_merge"] == "left_only"]

        # 去掉标记列
        self.df = result_df.drop(columns=["_merge"])

    def update_df_graded(self):
        self.df_graded.loc[len(self.df_graded)] = (
            self.patient_id,
            self.visit_date,
            self.eye,
        )

    def update_df_database(self, dict_results):
        df_data = pd.DataFrame([dict_results])
        self.df_database = pd.concat([self.df_database, df_data])

    def update_dict_results(self, dict_results):
        dict_scores = {}
        for key, label in dict_results.items():
            options = getattr(self, f"options_{key}")
            dict_scores[f"{key}_score"] = options[label].score
        dict_results.update(dict_scores)

        dict_results["comment"] = self.grad.textEdit_comment.toPlainText()
        dict_results["user"] = self.user
        dict_results["patient_id"] = self.patient_id
        dict_results["visit_date"] = self.visit_date
        dict_results["eye"] = self.eye

        # total_score = 0
        # for key, value in dict_results.items():
        #     if key.endswith("_score"):
        #         total_score += value
        dict_results["total_score"] = self.total_score

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

    def _test_script(self):
        self.df
        self.df_graded
        self.df_database
        self.patient_id, self.visit_date, self.eye
        self.df_database.to_csv("test.csv")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mwimpl = MainWindowImpl()
    mwimpl.show()
    sys.exit(app.exec())
