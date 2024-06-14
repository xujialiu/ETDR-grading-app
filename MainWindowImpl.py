# MainWindowImpl.py
# TODO list
# [[chore]]: 添加license文件
# [[feat]]: 增加如果not gradable, 其他选项变为灰色
# [[feat]]: 重写calculate_total_score的逻辑


from functools import partial
import hashlib
import json
from typing import Literal
from PySide6.QtCore import QEvent, Qt, Slot
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QFileDialog,
    QMenu,
    QMessageBox,
    QTabWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
)
import numpy as np
from MainWindow import MainWindow
import GradWidget, SetWidget, ImgDock
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
from cryptography.fernet import Fernet
from RegisterResetDialogImpl import RegisterDialog


ICON_PATH = ".meta/icon.png"
ROOT_USERNAME = "root"
ROOT_PASSWORD = "root"
VERSION = "1.0.1"
TEST_MODE = True


class MainWindowImpl(MainWindow):

    def __init__(self, test_mode) -> None:
        super().__init__()
        self.test_mode = test_mode
        self.init_ui_impl()
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setWindowTitle("Diabetic Retinopathy Grading Application")

        if self.test_mode:
            # disable password
            self.islogin = True
        else:
            self.islogin = False

        self.isroot = False

    def init_ui_impl(self):
        self._init_right_dock()
        self._init_left_dock()
        self._init_gradwidge()
        self._init_setwidge()
        
        self._init_labels()
        self._init_comboboxes()
        self._init_combobox_gradable()
        self._init_combobox_is_dr()
        self._init_app()
        self._init_clear_button()
        self._init_login_button()
        self._init_folder_button()
        self._init_patients_tree()
        self._init_df_database()
        self._init_df_graded()
        self._init_save_button()
        self._init_next_and_previous_button()

        self.installEventFilter(self)
        self.setFocusPolicy(Qt.StrongFocus)  # 确保窗口可以接收键盘事件

        self._init_menu()  # 放在最后, 因为需要连接其他控件
        self._init_test_mode()

    def _init_test_mode(self):
        # if self.test_mode:
        #     self.set.lineEdit_user.setText("xujialiu")
        #     self.set.lineEdit_password.setText("3")
        #     self.set.pushButton_login.click()
            
        pass

    def closeEvent(self, event):
        if not self.df_database.empty:
            self.df_database.astype(str).to_hdf(
                ".data/database.hdf5", key="df_database", mode="w"
            )

            self.df_graded.to_hdf(".data/database.hdf5", key="df_graded", mode="a")

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Right:
                # 触发按钮的点击事件
                self.img.pushButton_next.click()
                return True  # 事件已处理
            if event.key() == Qt.Key_Left:
                self.img.pushButton_previous.click()
                return True  # 事件已处理
        return super().eventFilter(source, event)

    def _init_right_dock(self):
        # set right dock
        self.tabwidget = QTabWidget(self)
        self.right_dock.setWidget(self.tabwidget)

    def _init_left_dock(self):
        self._init_img_widget()
        self._init_imgdock()
        # set left dock
        self.left_dock.setWidget(self.img.centralwidget)
        img_layout = self.img.widget_img.parentWidget().layout()
        img_layout.replaceWidget(self.img.widget_img, self.img_widget)
        setattr(self.img, self.img.widget_img.objectName(), self.img_widget)
        self.img.widget_img = self.img_widget

    def _init_img_widget(self):
        # 创建一个GraphicsLayoutWidget
        self.img_widget = GraphicsLayoutWidget()

        # 添加一个PlotItem
        self.plot_item = self.img_widget.addPlot()

        # 禁用坐标轴
        self.plot_item.hideAxis("left")
        self.plot_item.hideAxis("bottom")

        # 添加一个ImageItem
        self.img_item = ImageItem()
        self.plot_item.addItem(self.img_item)

        # 加载图像
        self.display_img(ICON_PATH)

        # 设置放大缩小功能
        self.plot_item.getViewBox().setMouseEnabled(x=True, y=True)
        self.plot_item.getViewBox().setAspectLocked(True)

        # 设置放大缩小功能
        self.plot_item.getViewBox().setMouseEnabled(x=True, y=True)
        self.plot_item.getViewBox().setAspectLocked(True)

    def display_img(self, path):
        img = Image.open(path)
        img = np.array(img)
        img = np.rot90(img, -1)
        self.img_item.setImage(img)

    def on_display_img(self):
        self.img_path = self.list_img_path[self.img_index]
        self.display_img(self.img_path)

    def get_img_path_list(self):
        cond = (
            (self.df.patient_id == self.patient_id)
            & (self.df.visit_date == self.visit_date)
            & (self.df.eye == self.eye)
        )
        series_img_path = self.df.file_path[cond]
        self.list_img_path = list(series_img_path)

    def _init_setwidge(self):
        self.set = SetWidget.Ui_MainWindow()
        self.set.setupUi(self)
        self.tabwidget.addTab(self.set.centralwidget, "Settings")

    def _init_register_dialog(self):

        self.register = RegisterDialog.Ui_Dialog()
        self.register.setupUi(self)

    def _init_gradwidge(self):
        self.grad = GradWidget.Ui_MainWindow()
        self.grad.setupUi(self)
        self.tabwidget.addTab(self.grad.centralwidget, "Grading Area")

    def _init_imgdock(self):
        self.img = ImgDock.Ui_MainWindow()
        self.img.setupUi(self)

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
            hover_combobox.setCurrentIndex(-1)
            hover_combobox.currentTextChanged.connect(self.displace_total_score)

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

    def displace_total_score(self):
        self.calculate_total_score()
        self.grad.label_score.setText(f"Total score: {self.total_score}")

    def displace_photo_number(self):
        num_img = len(self.list_img_path)
        self.grad.label_num_photo.setText(
            f"NO. photo / Total photos: {self.img_index+1} / {num_img}"
        )

    def calculate_total_score(self):
        """计算总分数"""
        list_comboboxes = []
        list_options = []
        for _, (combobox, option) in self.dict_comboboxes.items():
            list_comboboxes.append(combobox)
            list_options.append(option)
        list_text = [combobox.currentText() for combobox in list_comboboxes]
        list_score = [
            option.get(text, OptionScoreImgPath(score=0, path="")).score
            for option, text in zip(list_options, list_text)
        ]
        self.total_score = sum(list_score)

    def _init_app(self):
        app = QApplication.instance()
        app.setStyle("fusion")

    def _init_next_and_previous_button(self):
        self.img.pushButton_next.clicked.connect(self.on_next_clicked)
        self.img.pushButton_next.clicked.connect(self.on_display_img)
        self.img.pushButton_next.clicked.connect(self.displace_photo_number)

        self.img.pushButton_previous.clicked.connect(self.on_previous_clicked)
        self.img.pushButton_previous.clicked.connect(self.on_display_img)
        self.img.pushButton_previous.clicked.connect(self.displace_photo_number)

    def on_next_clicked(self):
        if self.img_index < len(self.list_img_path) - 1:
            self.img_index += 1

    def on_previous_clicked(self):
        if self.img_index > 0:
            self.img_index -= 1

    def _init_menu(self):

        self.menu = self.menuBar()
        self.menu.file_menu = self.menu.addMenu("File")
        self.menu.user_menu = self.menu.addMenu("User")
        self.menu.help_menu = self.menu.addMenu("Help")

        self.menu.register = QAction("Register", self)
        self.menu.user_menu.addAction(self.menu.register)

        self.menu.reset = QAction("Reset", self)
        self.menu.user_menu.addAction(self.menu.reset)

        self.menu.open_folder = QAction("Open Folder", self)

        self.menu.file_menu.addAction(self.menu.open_folder)

        self.menu.export = QAction("Export", self)
        self.menu.export_menu = QMenu("Export", self)

        self.menu.export.setMenu(self.menu.export_menu)
        self.menu.file_menu.addAction(self.menu.export)

        self.menu.exit = QAction("Exit", self)
        self.menu.file_menu.addAction(self.menu.exit)

        self.menu.df = QAction("Patient ID / Visit Date list", self)
        self.menu.export_menu.addAction(self.menu.df)

        self.menu.df_database = QAction("Database table", self)
        self.menu.export_menu.addAction(self.menu.df_database)

        self.menu.df_graded = QAction("Graded list", self)
        self.menu.export_menu.addAction(self.menu.df_graded)

        self.menu.about = QAction("About", self)
        self.menu.help_menu.addAction(self.menu.about)

        self.menu.register.triggered.connect(self.on_menu_register_clicked)
        self.menu.reset.triggered.connect(self.on_menu_reset_clicked)

        self.menu.open_folder.triggered.connect(self.select_folder_clicked)

        if self.test_mode:
            self.menu.debug = QAction("Debug", self)
            self.menu.help_menu.addAction(self.menu.debug)
            self.menu.debug.triggered.connect(self.on_debug_clicked)

            self.menu.data_inject = QAction("Data inject", self)
            self.menu.help_menu.addAction(self.menu.data_inject)
            self.menu.data_inject.triggered.connect(self.on_data_inject_clicked)

        else:
            pass

        self.menu.exit.triggered.connect(self.on_exit_clicked)
        self.menu.about.triggered.connect(self.on_about_clicked)

        self.df = pd.DataFrame()
        self.menu.df.triggered.connect(partial(self.on_export_clicked, self.df))
        self.menu.df_database.triggered.connect(
            partial(self.on_export_clicked, self.df_database)
        )
        self.menu.df_graded.triggered.connect(
            partial(self.on_export_clicked, self.df_graded)
        )

        self.menu.register.setEnabled(False)
        self.menu.reset.setEnabled(False)

    def on_data_inject_clicked(self):
        self.grad.comboBox_HMA.setCurrentText("Quest")  ###############
        self.grad.comboBox_HE.setCurrentText("Quest")
        self.grad.comboBox_SE.setCurrentText("Quest")
        self.grad.comboBox_IRMA.setCurrentText("Quest")
        self.grad.comboBox_VB.setCurrentText("Quest")
        self.grad.comboBox_NVD.setCurrentText("Quest")
        self.grad.comboBox_NVE.setCurrentText("Quest")
        self.grad.comboBox_FP.setCurrentText("Quest")
        self.grad.comboBox_PRH_VH.setCurrentText("Quest")
        self.grad.comboBox_EDEMA.setCurrentText("Quest")
        self.grad.comboBox_CTR.setCurrentText("Quest")
        self.grad.comboBox_VEN.setCurrentText("Quest")
        self.grad.comboBox_LASER.setCurrentText("Quest/incomplete")
        self.grad.comboBox_RX.setCurrentText("Quest")
        self.grad.comboBox_gradable.setCurrentText("Yes")
        self.grad.comboBox_is_dr.setCurrentText("Yes")
        self.grad.comboBox_confident.setCurrentText("Yes")
        self.grad.textEdit_comment.setText("test comments")

    def on_menu_register_clicked(self):
        self.dialog = RegisterDialog(self)
        self.dialog.setWindowTitle("Register new user")
        self.dialog.pushButton_register_reset.setText("Register")
        self.dialog.pushButton_cancel.clicked.connect(self.on_cancel_clicked)
        self.dialog.pushButton_register_reset.clicked.connect(self.on_register_clicked)
        self.dialog.exec()

    def on_menu_reset_clicked(self):
        self.dialog = RegisterDialog(self)
        self.dialog.setWindowTitle("Reset password")
        self.dialog.lineEdit_user.hide()
        self.dialog.label_user.hide()
        self.dialog.pushButton_register_reset.setText("Reset")
        self.dialog.pushButton_cancel.clicked.connect(self.on_cancel_clicked)
        self.dialog.pushButton_register_reset.clicked.connect(self.on_reset_clicked)
        self.dialog.exec()

    def on_cancel_clicked(self):
        self.dialog.close()

    def on_reset_clicked(self):
        username = self.user
        password = self.dialog.lineEdit_password.text()
        confirm_password = self.dialog.lineEdit_confirm_password.text()
        if password != confirm_password:
            QMessageBox.warning(self, "Reset Failed", "Passwords do not match.")
            return
        if username == ROOT_USERNAME:
            QMessageBox.warning(self, "Reset Failed", "You cannot reset root password.")
            return
        if self.reset_user_password(username, password):
            QMessageBox.information(
                self,
                "Reset Successful",
                "Password resetted successfully.",
            )
            self.user = username
            self.set.lineEdit_user.setText(self.user)
            self.set.lineEdit_password.setText(password)
        else:
            QMessageBox.warning(self, "Registration Failed", "Username already exists.")

    def reset_user_password(self, username, password):
        with open(".meta/users.json", "r") as file:
            users = json.load(file)

        salt = Fernet.generate_key().decode()
        encrypted_password = hashlib.sha256((password + salt).encode()).hexdigest()
        users[username] = {"password": encrypted_password, "salt": salt}

        with open(".meta/users.json", "w") as file:
            json.dump(users, file)

        return True

    def on_register_clicked(self):
        username = self.dialog.lineEdit_user.text()
        password = self.dialog.lineEdit_password.text()
        confirm_password = self.dialog.lineEdit_confirm_password.text()
        if password != confirm_password:
            QMessageBox.warning(self, "Registration Failed", "Passwords do not match.")
            return
        if username == ROOT_USERNAME:
            QMessageBox.warning(
                self, "Registration Failed", "You cannot register as root."
            )
            return
        if self.add_user_password(username, password):
            QMessageBox.information(
                self,
                "Registration Successful",
                "User registered successfully.",
            )
            self.islogin = True
            self.isroot = False
            self.menu.reset.setEnabled(True)
            self.user = username
            self.set.lineEdit_user.setText(username)
            self.set.lineEdit_password.setText(password)
        else:
            QMessageBox.warning(self, "Registration Failed", "Username already exists.")

    def add_user_password(self, username, password):
        try:
            with open(".meta/users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if username in users:
            return False

        salt = Fernet.generate_key().decode()
        encrypted_password = hashlib.sha256((password + salt).encode()).hexdigest()
        users[username] = {"password": encrypted_password, "salt": salt}

        with open(".meta/users.json", "w") as file:
            json.dump(users, file)

        return True

    def on_export_clicked(self, df: pd.DataFrame):
        # 弹出文件选择窗口

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save DataFrame",
            "",
            "CSV Files (*.csv);;Excel Files (*.xlsx)",
            options=options,
        )
        if file_path:
            # 根据文件扩展名保存DataFrame
            if file_path.endswith(".csv"):
                df.to_csv(file_path, index=False)
            elif file_path.endswith(".xlsx"):
                df.to_excel(file_path, index=False)

    def on_about_clicked(self):
        # 创建关于对话框
        about_dialog = QMessageBox(self)
        about_dialog.setWindowTitle("About")
        about_dialog.setText(
            "This is a diabetic ETDR grading application.<br><br>"
            f"Version: {VERSION}<br><br>"
            "Author: Xujia Liu<br>"
            "Email: xujialiuphd@gmail.com<br><br>"
            'Website (building): <a href="https://github.com/xujialiu/ETDR-grading-app">https://github.com/xujialiu/ETDR-grading-app</a>'
        )
        about_dialog.setIcon(QMessageBox.Information)
        about_dialog.exec()

    def on_exit_clicked(self):
        app = QApplication.instance()
        app.quit()

    def on_debug_clicked(self):
        self.debug_window = DebugWindow()
        self.debug_window.code_submitted.connect(self.execute_code)
        self.debug_window.show()

    @Slot(str)
    def execute_code(self, code):
        try:
            exec(f"print({code})")
        except Exception as e:
            print(e)

    def select_folder_clicked(self):
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
        self.set.folder_button.clicked.connect(self.select_folder_clicked)
        self.set.folder_button.clicked.connect(self.get_df)
        self.set.folder_button.clicked.connect(self.show_patients_tree)
        self.set.folder_button.clicked.connect(self.find_first_tree_item)
        self.set.folder_button.clicked.connect(self.show_grad_labels)
        self.set.folder_button.clicked.connect(self.show_df_graded_df_database)
        self.set.folder_button.clicked.connect(self.get_first_img_index)
        self.set.folder_button.clicked.connect(self.get_img_path_list)
        self.set.folder_button.clicked.connect(self.on_display_img)
        self.set.folder_button.clicked.connect(self.displace_photo_number)

    def get_first_img_index(self):
        self.img_index = 0

    def _init_df_graded(self):
        """储存graded的患者信息, 包括patient_id, visit_date, eye"""
        self.df_graded = load_or_create_df_graded()

    def _init_patients_tree(self):
        self.set.treeWidget_patient.itemClicked.connect(self.on_visit_date_clicked)
        self.set.treeWidget_patient.itemClicked.connect(self.get_img_path_list)
        self.set.treeWidget_patient.itemClicked.connect(self.on_display_img)
        self.set.treeWidget_patient.itemClicked.connect(self.displace_photo_number)

    def _init_login_button(self):
        self.set.pushButton_login.clicked.connect(self.on_login_clicked)

    def _init_save_button(self):
        self.grad.pushButton_save.clicked.connect(self.on_save_clicked)
        self.grad.pushButton_save.clicked.connect(self.get_first_img_index)
        self.grad.pushButton_save.clicked.connect(self.get_img_path_list)
        self.grad.pushButton_save.clicked.connect(self.on_display_img)
        self.grad.pushButton_save.clicked.connect(self.displace_photo_number)

    def _init_df_database(self):
        self.df_database = load_or_create_df_database()

    def get_df(self):
        self.df = get_df_folder_contents(self.set.folder_path)
        self.df_remove_row_in_df_graded()

    def on_login_clicked(self):
        self.user = self.set.lineEdit_user.text()
        password = self.set.lineEdit_password.text()
        if self.validate_user(self.user, password):
            if self.user == ROOT_USERNAME:
                QMessageBox.information(
                    self, "Login Successful", "You are logged in as root."
                )
                self.islogin = True
                self.isroot = True
                self.menu.register.setEnabled(True)
            else:
                QMessageBox.information(self, "Login Successful", "You are logged in.")
                self.islogin = True
                self.isroot = False
                self.menu.reset.setEnabled(True)
                self.set.lineEdit_user.setEnabled(False)
                self.set.lineEdit_password.setEnabled(False)
                self.set.pushButton_login.setEnabled(False)

        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def validate_user(self, username, password):
        if username == ROOT_USERNAME and password == ROOT_PASSWORD:
            return True

        try:
            with open(".meta/users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if username in users:
            stored_password = users[username]["password"]
            salt = users[username]["salt"]
            return (
                stored_password
                == hashlib.sha256((password + salt).encode()).hexdigest()
            )
        return False

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
        self.grad.pushButton_clear.clicked.connect(self.on_clear_clicked)
        
        
    def _init_labels(self):
        pass

    def on_clear_clicked(self):
        comboboxes = (combobox for _, (combobox, _) in self.dict_comboboxes.items())
        for combobox in comboboxes:
            combobox.setCurrentIndex(-1)
        self.grad.comboBox_gradable.setCurrentIndex(-1)
        self.grad.comboBox_is_dr.setCurrentIndex(-1)
        self.grad.lineEdit_other_diagnosis.setText("")
        self.grad.comboBox_confident.setCurrentIndex(-1)
        self.grad.textEdit_comment.setText("")

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

    def _init_combobox_gradable(self):
        self.grad.comboBox_gradable.currentTextChanged.connect(
            self.on_gradable_text_changed
        )

    def on_gradable_text_changed(self):

        if self.grad.comboBox_gradable.currentText() == "Yes":
            for combobox, _ in self.dict_comboboxes.values():
                combobox.setEnabled(True)
            self.grad.comboBox_is_dr.setEnabled(True)
            self.grad.lineEdit_other_diagnosis.setEnabled(True)
            self.grad.comboBox_confident.setEnabled(True)

        if self.grad.comboBox_gradable.currentText() == "No":
            for combobox, _ in self.dict_comboboxes.values():
                combobox.setEnabled(False)
            self.grad.comboBox_is_dr.setEnabled(False)
            self.grad.lineEdit_other_diagnosis.setEnabled(False)
            self.grad.comboBox_confident.setEnabled(False)

    def is_all_filled(self):
        # 如果是gradable为No, 直接返回True
        if self.grad.comboBox_gradable.currentText() == "No":
            return True

        comboboxes_choices = [
            combobox.currentText() for (combobox, _) in self.dict_comboboxes.values()
        ]

        # 如果gradable为Yes, 需要进一步判断combobox_with_hover
        if all(comboboxes_choices) and self.grad.comboBox_confident.currentText():
            # 需要进一步判断is_dr

            # 如果is_dr=="Yes", 直接返回True
            if self.grad.comboBox_is_dr.currentText() == "Yes":
                return True

            # 如果is_dr=="No", 还需要other_diagnosis不为空
            elif (
                self.grad.comboBox_is_dr.currentText() == "No"
                and self.grad.lineEdit_other_diagnosis.text()
            ):
                return True

        # 其余情况, 返回false
        else:
            return False

    def _init_combobox_is_dr(self):
        self.grad.comboBox_is_dr.currentTextChanged.connect(self.on_is_dr_changed)

    def on_is_dr_changed(self):
        if self.grad.comboBox_is_dr.currentText() == "Yes":
            self.grad.lineEdit_other_diagnosis.setEnabled(False)
            # 如果不是空字符, 把lineEdit_other_diagnosis设为空字符
            self.grad.lineEdit_other_diagnosis.setText("")

        if self.grad.comboBox_is_dr.currentText() == "No":
            self.grad.lineEdit_other_diagnosis.setEnabled(True)

    def on_save_clicked(self):
        if not self.islogin:
            QMessageBox.warning(self, "Error", "Please login!")
        elif not self.is_all_filled():
            QMessageBox.warning(self, "Error", "Please fill all options!")

        elif self.is_all_filled():

            dict_results = self.update_dict_results()
            self.update_df_database(dict_results)

            self.update_df_graded()

            self.update_df()
            self.show_patients_tree()
            self.find_and_activate_tree_item()
            self.show_df_graded_df_database()
            self.on_clear_clicked()

            for combobox, _ in self.dict_comboboxes.values():
                combobox.setEnabled(True)

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

    def update_dict_results(self):
        dict_results = {
            label: combobox.currentText()
            for label, (combobox, _) in self.dict_comboboxes.items()
        }

        dict_scores = {}
        for key, label in dict_results.items():
            options = getattr(self, f"options_{key}")
            dict_scores[f"{key}_score"] = options[label].score
        dict_results.update(dict_scores)

        other_result = {
            "is_gradable": self.grad.comboBox_gradable.currentText(),
            "is_dr": self.grad.comboBox_is_dr.currentText(),
            "other_diagnosis": self.grad.lineEdit_other_diagnosis.text(),
            "confident": self.grad.comboBox_confident.currentText(),
            "comment": self.grad.textEdit_comment.toPlainText(),
        }

        dict_results.update(other_result)

        dict_results["user"] = self.user
        dict_results["patient_id"] = self.patient_id
        dict_results["visit_date"] = self.visit_date
        dict_results["eye"] = self.eye
        dict_results["total_score"] = self.total_score

        return dict_results

    def comboboxes_options(self):
        with open(".meta/combobox_options.json", "r", encoding="utf-8") as f:
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

    def _test_script(self):
        """This is test script and never expected to run on App"""
        self.df
        self.df_graded
        self.df_database
        self.patient_id, self.visit_date, self.eye
        self.df_database.to_csv("test.csv")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwimpl = MainWindowImpl(test_mode=TEST_MODE)
    mwimpl.show()
    sys.exit(app.exec())
