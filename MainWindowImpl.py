# MainWindowImpl.py
# TODO list
# [[feat, priority low]]: 读取时使用多线程加速
# [[feat, priority low]]: 增加eval mode, 当为eval mode时, 只有df_database和df_graded的交集, 界面出现列表, 点击患者, 显示各项评分
# [[feat, priority high]]: 修改update_dict_results, update_df_database, update_df_graded, update_df的逻辑
# [[feat, priority high]]: 增加qlabel, 显示macula和disc, 增加一个内部计数器
# [[feat, priority high]]: 由于增加了项目, 需要需要修改util

# 增加levels对应的DR严重程度


from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
from ComboBoxWithToolTips import ComboBoxWithToolTips
from functools import partial
import hashlib
import json
from PySide6.QtCore import QEvent, QObject, QSettings, QSize, Qt, Signal, Slot
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QFileDialog,
    QMenu,
    QMessageBox,
    QScrollArea,
    QTabWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)
import numpy as np
from CheckableComboBox import CheckableComboBox
from MainWindow import MainWindow
import GradWidget, SetWidget, ImgDock
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
from pynput import keyboard
from VERSION import VERSION


ICON_PATH = ".meta/icon.png"
ROOT_USERNAME = "root"
ROOT_PASSWORD = "root"
TEST_MODE = True
DATA_BASE_PATH = Path.home() / "ETDR-grading-app"
DF_DATABASE_PATH = DATA_BASE_PATH / "df_database.parquet"
DF_GRADED_PATH = DATA_BASE_PATH / "df_graded.parquet"

if not DATA_BASE_PATH.exists():
    DATA_BASE_PATH.mkdir()


class KeyListener(QObject):
    key_pressed = Signal(str)

    def __init__(self):
        super().__init__()
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        if key == keyboard.Key.left:
            self.key_pressed.emit("left")
        elif key == keyboard.Key.right:
            self.key_pressed.emit("right")


class MainWindowImpl(MainWindow):

    def __init__(self, test_mode) -> None:
        super().__init__()
        self.test_mode = test_mode
        self.init_ui_impl()
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setWindowTitle("Diabetic Retinopathy Grading Application")
        self.load_settings()

        self.islogin = False
        self.isroot = False

    def init_ui_impl(self):
        # 初始化布局组件
        self._init_app()
        self._init_right_dock()
        self._init_left_dock()
        self._init_gradwidge()
        self._init_setwidge()

        # 初始化其他
        self._init_labels()
        self._init_comboboxes()
        self._init_combobox_confident()
        self._init_combobox_gradable()
        self._init_combobox_diagosis()
        self._init_combobox_icdr()
        self._init_img_slider()
        self._init_img_spinbox()
        self._init_img_reset_button()
        self._init_clear_button()
        self._init_login_button()
        self._init_folder_button()
        self._init_patients_tree()
        self._init_df_database()
        self._init_df_graded()
        self._init_save_button()
        self._init_next_and_previous_button()
        self._init_key_listener()
        self._init_grad_spinbox()
        self._init_grad_general_others()
        self._init_dr_severity_dict()
        self._init_combobox_gradable()
        self._init_combobox_ma()

        # 初始化事件相关函数
        self.installEventFilter(self)
        self.setFocusPolicy(Qt.StrongFocus)  # 确保窗口可以接收键盘事件

        # 初始化menu
        self._init_menu()  # 放在最后, 因为需要连接其他控件

        # 初始化测试模块
        if self.test_mode:
            self._init_debug_mode()

    def _init_dr_severity_dict(self):
        self.dict_level_severity = {
            "": "",
            "10": "Absent",
            "14 & 15": "Questionable DR",
            "20": "Minimal DR",
            "35": "Mild NPDR",
            "43": "Moderate NPDR",
            "47": "Moderately Severe NPDR",
            "53": "Severe DR",
            "61": "Mild PDR",
            "65": "Moderate PDR",
            "71": "Severe PDR",
            "81 & 85": "Advanced PDR",
            "90": "Inactive PDR",
            "99": "Ungradable",
        }

    def _init_debug_mode(self):

        self.menu.debug = QAction("Debug", self)
        self.menu.help_menu.addAction(self.menu.debug)
        self.menu.debug.triggered.connect(self.on_debug_clicked)

        self.menu.data_inject = QAction("Data inject", self)
        self.menu.help_menu.addAction(self.menu.data_inject)
        self.menu.data_inject.triggered.connect(self.on_data_inject_clicked)

    def closeEvent(self, event):
        if not self.df_database.empty:
            with ThreadPoolExecutor() as executor:

                executor.submit(self.save_parquet, DF_DATABASE_PATH, self.df_database)
                executor.submit(
                    self.save_parquet,
                    DF_GRADED_PATH,
                    self.df_graded,
                )

        self.save_settings()
        event.accept()

    def _init_grad_spinbox(self):
        self.list_spinBox = [
            self.grad.spinBox_RH_quadrants,
            self.grad.spinBox_IRMA_quadrants,
            self.grad.spinBox_VB_quadrants,
            self.grad.spinBox_NVE_quadrants,
        ]
        self.dict_combobox_spinbox = {
            "RH": (self.grad.comboBox_RH, self.grad.spinBox_RH_quadrants),
            "IRMA": (self.grad.comboBox_IRMA, self.grad.spinBox_IRMA_quadrants),
            "VB": (self.grad.comboBox_VB, self.grad.spinBox_VB_quadrants),
            "NVE": (self.grad.comboBox_NVE, self.grad.spinBox_NVE_quadrants),
        }

        for spinbox in self.list_spinBox:
            spinbox.setSpecialValueText(" ")
            spinbox.setEnabled(False)
            spinbox.valueChanged.connect(self.calculate_display_levels_severity)

        self.set_combobox_none_to_disable_spinbox()

    # working
    def set_combobox_none_to_disable_spinbox(self):

        def enable_disable_combobox(current_text, spinbox):
            if current_text in ("None", ""):
                spinbox.setEnabled(False)
                spinbox.setValue(0)
            else:
                spinbox.setEnabled(True)
                spinbox.setValue(1)

        for combobox, spinbox in self.dict_combobox_spinbox.values():
            # 使用 partial 时不传递 combobox 的 currentText()
            func = partial(enable_disable_combobox, spinbox=spinbox)
            # 连接信号，传递的 current_text 由信号提供
            combobox.currentTextChanged.connect(func)

    def _init_grad_general_others(self):
        # general + others
        self.list_general_others = [
            self.grad.comboBox_gradable,
            self.grad.comboBox_clarity,
            self.grad.comboBox_is_dr,
            self.grad.comboBox_diagnoses,
            self.grad.lineEdit_other_diagnoses,
            self.grad.comboBox_ICDR,
        ] + [self.grad.comboBox_confident]

    def _init_key_listener(self):
        self.key_listener = KeyListener()
        self.key_listener.key_pressed.connect(self.on_key_pressed)

    def on_key_pressed(self, key_text):
        if key_text == "right":
            self.img_dock.pushButton_next.click()
        if key_text == "left":
            self.img_dock.pushButton_previous.click()

    def save_settings(self):
        settings = QSettings("MyCompany", "MyApp")
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("windowState", self.saveState())
        settings.setValue("username", self.set.lineEdit_user.text())

    def load_settings(self):
        settings = QSettings("MyCompany", "MyApp")
        self.restoreGeometry(settings.value("geometry"))
        self.restoreState(settings.value("windowState"))
        self.set.lineEdit_user.setText(settings.value("username", ""))

    def save_parquet(self, file_path, df):
        df.to_parquet(file_path)

    def _init_right_dock(self):
        # set right dock
        self.tabwidget = QTabWidget(self)
        self.right_dock.setWidget(self.tabwidget)

    def _init_left_dock(self):
        self._init_img_widget()
        self._init_imgdock()
        # set left dock
        self.left_dock.setWidget(self.img_dock.centralwidget)
        img_layout = self.img_dock.widget_img.parentWidget().layout()
        img_layout.replaceWidget(self.img_dock.widget_img, self.widget_img)
        setattr(self.img_dock, self.img_dock.widget_img.objectName(), self.widget_img)
        self.img_dock.widget_img = self.widget_img

    def _init_img_widget(self):
        # 创建一个GraphicsLayoutWidget
        self.widget_img = GraphicsLayoutWidget()

        # 添加一个PlotItem
        self.plot_item = self.widget_img.addPlot()

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

    def display_img(self, path):
        self.img = Image.open(path)
        self.img = np.array(self.img)
        self.img = np.rot90(self.img, -1)
        self.img_item.setImage(self.img)

    def on_update_image(self):
        brightness = self.img_dock.horizontalSlider_brightness.value()
        contrast = self.img_dock.horizontalSlider_contrast.value()

        adjustedImage = self.img.astype(np.float32)
        adjustedImage = adjustedImage * (contrast / 50.0 + 1) + brightness
        adjustedImage = np.clip(adjustedImage, 0, 255).astype(np.uint8)

        self.img_item.setImage(adjustedImage)

    def _init_img_slider(self):
        self.img_dock.horizontalSlider_brightness.valueChanged.connect(
            self.on_update_image
        )
        self.img_dock.horizontalSlider_contrast.valueChanged.connect(
            self.on_update_image
        )

        self.img_dock.horizontalSlider_brightness.valueChanged.connect(
            lambda: self.img_dock.spinBox_brightness.setValue(
                self.img_dock.horizontalSlider_brightness.value()
            )
        )

        self.img_dock.horizontalSlider_contrast.valueChanged.connect(
            lambda: self.img_dock.spinBox_contrast.setValue(
                self.img_dock.horizontalSlider_contrast.value()
            )
        )

    def _init_img_spinbox(self):
        self.img_dock.spinBox_brightness.valueChanged.connect(
            lambda: self.img_dock.horizontalSlider_brightness.setValue(
                self.img_dock.spinBox_brightness.value()
            )
        )

        self.img_dock.spinBox_contrast.valueChanged.connect(
            lambda: self.img_dock.horizontalSlider_contrast.setValue(
                self.img_dock.spinBox_contrast.value()
            )
        )

    def _init_img_reset_button(self):
        self.img_dock.pushButton_img_reset.clicked.connect(self.on_img_reset_clicked)

    def on_img_reset_clicked(self):
        self.img_dock.horizontalSlider_contrast.setValue(0)
        self.img_dock.horizontalSlider_brightness.setValue(0)

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
        self.tabwidget.addTab(self.set.centralwidget, "Setting")

    def _init_register_dialog(self):

        self.register = RegisterDialog.Ui_Dialog()
        self.register.setupUi(self)

    def _init_gradwidge(self):
        self.grad = GradWidget.Ui_MainWindow()
        self.grad.setupUi(self)

        # 创建一个新的widget作为中间容器
        container_widget = QWidget()
        self.scroll_area = QScrollArea()

        # 创建一个垂直布局，并将其对齐方式设置为居中
        layout = QVBoxLayout(container_widget)
        layout.setAlignment(Qt.AlignCenter)

        # 将content添加到布局中
        layout.addWidget(self.grad.centralwidget)

        # 将容器widget设置为scroll_area的widget
        self.scroll_area.setWidget(container_widget)
        self.scroll_area.setWidgetResizable(True)

        # 将scroll_area添加到tabwidget中
        self.tabwidget.addTab(self.scroll_area, "Grading")

    def _init_imgdock(self):
        self.img_dock = ImgDock.Ui_MainWindow()
        self.img_dock.setupUi(self)

    def _init_combobox_confident(self):
        # 禁用wheelevent
        def new_wheelevent(event):
            pass

        self.grad.comboBox_confident.wheelEvent = new_wheelevent

    def _init_comboboxes(self):
        self.comboboxes_options()

        dict_comboboxes = {
            self.grad.comboBox_MA: self.options_MA,
            self.grad.comboBox_RH: self.options_RH,
            self.grad.comboBox_HE: self.options_HE,
            self.grad.comboBox_SE: self.options_SE,
            self.grad.comboBox_IRMA: self.options_IRMA,
            self.grad.comboBox_VB: self.options_VB,
            self.grad.comboBox_NVD: self.options_NVD,
            self.grad.comboBox_NVE: self.options_NVE,
            self.grad.comboBox_FP: self.options_FP,
            self.grad.comboBox_PRH_VH: self.options_PRH_VH,
            self.grad.comboBox_VEN: self.options_VEN,
            self.grad.comboBox_LASER: self.options_LASER,
            self.grad.comboBox_RD: self.options_RD,
        }
        self.hover_label = HoverLabel()

        self.grad.list_comboboxes = []
        for comboBox, options in dict_comboboxes.items():
            hover_combobox = ComboBoxWithHover(self.hover_label, options)
            # print(options)
            hover_combobox.addItems(list(options.keys()))

            layout = comboBox.parentWidget().layout()
            layout.replaceWidget(comboBox, hover_combobox)
            comboBox.deleteLater()

            setattr(
                self.grad, comboBox.objectName(), hover_combobox
            )  # 绑定到新的变量上
            hover_combobox.setCurrentIndex(-1)
            hover_combobox.currentTextChanged.connect(
                self.calculate_display_levels_severity
            )

            self.grad.list_comboboxes.append(hover_combobox)

        self.dict_comboboxes = {
            "MA": [self.grad.comboBox_MA, self.options_MA],
            "RH": [self.grad.comboBox_RH, self.options_RH],
            "HE": [self.grad.comboBox_HE, self.options_HE],
            "SE": [self.grad.comboBox_SE, self.options_SE],
            "IRMA": [self.grad.comboBox_IRMA, self.options_IRMA],
            "VB": [self.grad.comboBox_VB, self.options_VB],
            "NVD": [self.grad.comboBox_NVD, self.options_NVD],
            "NVE": [self.grad.comboBox_NVE, self.options_NVE],
            "FP": [self.grad.comboBox_FP, self.options_FP],
            "PRH_VH": [self.grad.comboBox_PRH_VH, self.options_PRH_VH],
            "VEN": [self.grad.comboBox_VEN, self.options_VEN],
            "LASER": [self.grad.comboBox_LASER, self.options_LASER],
            "RD": [self.grad.comboBox_RD, self.options_RD],
        }

    def _init_combobox_icdr(self):
        items = {
            "No apparent DR": "No abnormalities",
            "Mild NPDR": "Microaneurysms only",
            "Moderate NPDR ": "More than just microaneurysms but less than severe nonproliferative diabetic retinopathy",
            "Severe NPDR ": "Any of the following: more than 20 intraretinal hemorrhages in each of 4 quadrants; "
            "definite venous beading in 2+ quadrants;\n"
            "Prominent intraretinal microvascular abnormalities in 1 + quadrant And no signs of proliferative retinopathy",
            "PDR": "One or more of the following: neovascularization, vitreous/preretinahemorrhage",
        }
        combobox_icdr = ComboBoxWithToolTips()
        for text, tip in items.items():
            combobox_icdr.addItem(text)
            combobox_icdr.setItemData(combobox_icdr.count() - 1, tip, Qt.ToolTipRole)

        layout = self.grad.comboBox_ICDR.parentWidget().layout()
        fixed_width = 150
        combobox_icdr.setCurrentIndex(-1)

        combobox_icdr.setMinimumWidth(fixed_width)
        combobox_icdr.setMaximumWidth(fixed_width)
        layout.replaceWidget(self.grad.comboBox_ICDR, combobox_icdr)
        self.grad.comboBox_ICDR.deleteLater()
        setattr(self.grad, "comboBox_ICDR", combobox_icdr)

    def _init_combobox_diagosis(self):
        checkable_combobox = CheckableComboBox()
        with open(".meta/combobox_diagnoses.json", "r") as file:
            list_diagnoses = json.load(file)["diagnoses"]
        checkable_combobox.addItems(list_diagnoses)
        fixed_width = 150
        checkable_combobox.setMinimumWidth(fixed_width)
        checkable_combobox.setMaximumWidth(fixed_width)
        layout = self.grad.comboBox_diagnoses.parentWidget().layout()
        self.grad.comboBox_diagnoses.deleteLater()
        layout.replaceWidget(self.grad.comboBox_diagnoses, checkable_combobox)
        setattr(self.grad, "comboBox_diagnoses", checkable_combobox)

    def calculate_display_levels_severity(self):
        self.calculate_levels()
        self.grad.label_levels.setText(f"DR levels: {self.levels}")

        self.severity = self.dict_level_severity[self.levels]
        self.grad.label_severity.setText(f"DR severity: {self.severity}")

    def displace_photo_number(self):
        self.num_img = len(self.list_img_path)

        self.grad.label_num_photo.setText(
            f"NO. photo / Total photos: {self.img_index+1} / {self.num_img}"
        )
        self.img_dock.label_num_photo.setText(
            f"NO. photo / Total photos: {self.img_index+1} / {self.num_img}"
        )

    def _set_disabled_etdr_except(self, list_combobox_excluded):
        for name, (combobox, _) in self.dict_comboboxes.items():
            if name in list_combobox_excluded:
                pass
            else:
                # 设置除了list_combobox_excluded外的其他combobox不能被修改
                combobox.setEnabled(False)
                combobox.setCurrentIndex(-1)

        # 设置comboBox_VH_extent为空字符串, 并设置他们不能被修改
        self.grad.comboBox_VH_extent.setCurrentIndex(-1)
        self.grad.comboBox_VH_extent.setEnabled(False)

    def _set_enabled_etdr(self):

        for _, (combobox, _) in self.dict_comboboxes.items():
            combobox.setEnabled(True)

        self.grad.comboBox_VH_extent.setCurrentText("")
        self.grad.comboBox_VH_extent.setEnabled(True)

    def _set_disable_all_except_gradable(self):
        # disable general and others
        for widget in self.list_general_others[1:]:
            widget.setEnabled(False)

        # set general and others to ''
        self.grad.comboBox_clarity.setCurrentIndex(-1)
        self.grad.comboBox_is_dr.setCurrentIndex(-1)
        self.grad.comboBox_confident.setCurrentIndex(-1)

        self.grad.lineEdit_other_diagnoses.setText("")
        self.grad.comboBox_ICDR.setCurrentIndex(-1)

        # disable etdr
        self._set_disabled_etdr_except([])

    def _set_enabled_all(self):
        # set general and others to correct text
        self.grad.comboBox_clarity.setCurrentText("No")
        self.grad.comboBox_is_dr.setCurrentText("Yes")
        self.grad.comboBox_confident.setCurrentText("Yes")

        # enable general and others
        for widget in self.list_general_others[1:]:
            widget.setEnabled(True)

        # enable etdr
        self._set_enabled_etdr()

    def calculate_levels(self):
        # levels为 99 的情况
        condition_lv_99 = self.grad.comboBox_gradable.currentText() == "No"
        if condition_lv_99:
            self.levels = "99"
        else:
            self.levels = ""

        # levels为10的情况
        condition_lv_10 = (self.grad.comboBox_MA.currentText() == "Absent") and (
            self.grad.comboBox_RH.currentText() == "None"
        )
        if condition_lv_10:
            self.levels = "10"
            # self._set_disabled_except(["MA", "RH"])

        # levels为14&15的情况
        condition_lv_14_15 = (self.grad.comboBox_MA.currentText() == "Absent") and (
            self.grad.comboBox_RH.currentIndex() > 0
        )
        if condition_lv_14_15:
            self.levels = "14 & 15"
            # self._set_disabled_except(["MA", "RH"])

        all_spinbox_status = []
        for spinBox in self.list_spinBox:
            all_spinbox_status.append(spinBox.isEnabled())

        # levels为20的情况
        self.other_combobox_text = {}
        for name, (combobox, option) in self.dict_comboboxes.items():
            if name not in ["MA", "RH"]:
                self.other_combobox_text[name] = combobox.currentText()

        l = [i == "None" for i in self.other_combobox_text.values()]
        if all(l):
            self.levels = "20"

        # levels为90需要跳转到35的情况
        condition_lv_90_focal_scar = (
            self.grad.comboBox_LASER.currentIndex() == 1
        ) and (
            (self.grad.comboBox_NVD.currentIndex() == 0)
            and (self.grad.comboBox_NVE.currentIndex() == 0)
        )
        if condition_lv_90_focal_scar:
            self.levels = "35"

        # levels为35的情况
        must_conditon = self.grad.comboBox_MA.currentText() == "Present"
        if must_conditon and (
            (
                (self.grad.comboBox_RH.currentText() == "< SP1")
                and (
                    self.grad.comboBox_HE.currentIndex() > 0
                    or self.grad.comboBox_SE.currentIndex() > 0
                    or self.grad.comboBox_VEN.currentIndex() > 0
                    or (
                        self.grad.comboBox_IRMA.currentText() == "Questionable"
                        or self.grad.comboBox_VB.currentText() == "Questionable"
                    )
                )
            )
        ):
            self.levels = "35"

        # levels为43的情况, 需要增加RH quadrant的情况
        self.condition_lv_43_1 = (
            (self.grad.comboBox_RH.currentText() == "≥ SP1, < SP2A")
            and (self.grad.spinBox_RH_quadrants.value() >= 1)
        ) or (
            (self.grad.comboBox_RH.currentText() == "≥ SP2A")
            and (self.grad.spinBox_RH_quadrants.value() == 1)
        )

        self.condition_lv_43_2 = (
            self.grad.comboBox_IRMA.currentText() == "< SP8A"
        ) and (self.grad.spinBox_IRMA_quadrants.value() in (1, 2, 3))

        if self.condition_lv_43_1 or self.condition_lv_43_2:
            self.levels = "43"

        # levels为47的情况
        # Mild `IRMA<SP8A` in 4 quadrants
        condition_lv_47_1 = (self.grad.comboBox_IRMA.currentText() == "< SP8A") and (
            self.grad.spinBox_IRMA_quadrants.value() == 4
        )

        # Severe RH>SP2A in 2 to 3 quadrants
        condition_lv_47_2 = (self.grad.comboBox_RH.currentText() == "≥ SP2A") and (
            self.grad.spinBox_RH_quadrants.value() in (2, 3)
        )

        # `VB>SP6A` in 1 quadrant
        conditon_lv_47_3 = (self.grad.comboBox_VB.currentText() == "≥ SP6A") and (
            self.grad.spinBox_VB_quadrants.value() == 1
        )

        if condition_lv_47_1 or condition_lv_47_2 or conditon_lv_47_3:
            self.levels = "47"

        # levels为53的情况
        # >2 of the 4 level 47 characteristics
        condition_lv_53_1 = (
            (condition_lv_47_1 and condition_lv_47_2)
            or (condition_lv_47_1 and conditon_lv_47_3)
            or (condition_lv_47_2 and conditon_lv_47_3)
        )

        # Severe `RH>SP2A` in 4 quadrants
        condition_lv_53_2 = (self.grad.comboBox_RH.currentText() == "≥ SP2A") and (
            self.grad.spinBox_RH_quadrants.value() == 4
        )

        # Moderate to Severe IRMA>=SP8A in at least one quadrant
        condition_lv_53_3 = (self.grad.comboBox_IRMA.currentText() == "≥ SP8A") and (
            self.grad.spinBox_IRMA_quadrants.value() >= 1
        )

        # VB ("≥ SP6A") in at least 2 quadrants
        condition_lv_53_4 = (self.grad.comboBox_VB.currentText() == "≥ SP6A") and (
            self.grad.spinBox_VB_quadrants.value() >= 2
        )
        if (
            condition_lv_53_1
            or condition_lv_53_2
            or condition_lv_53_3
            or condition_lv_53_4
        ):
            self.levels = "53"

        # levels为61的情况
        # NVE<0.5 DA in 1 or more quadrants
        condition_lv_61 = (
            self.grad.comboBox_NVE.currentText() == "< 1/2 Disc area"
        ) and (self.grad.spinBox_NVE_quadrants.value() >= 1)

        if condition_lv_61:
            self.levels = "61"

        # levels为65的情况
        # NVE > 0.5 DA or (VH or PRH)
        condition_lv_65_1 = (
            self.grad.comboBox_NVE.currentText() == "≥ 1/2 Disc area"
        ) or (self.grad.comboBox_PRH_VH.currentIndex() > 0)

        # NVD <SP 10A
        condition_lv_65_2 = self.grad.comboBox_NVD.currentText() == "< SP 10A"

        if condition_lv_65_1 or condition_lv_65_2:
            self.levels = "65"

        # levels为71的情况
        # NVE > 0.5 DA and VH or PRH
        condition_lv_71_1 = (
            self.grad.comboBox_NVE.currentText() == "≥ 1/2 Disc area"
        ) and (self.grad.comboBox_PRH_VH.currentIndex() > 0)

        # NVD >=SP 10A or (NVD `<SP 10A` and VH or PRH )
        condition_lv_71_2 = self.grad.comboBox_NVD.currentText() == "≥ SP 10A" or (
            (self.grad.comboBox_NVD.currentText() == "< SP 10A")
            and (self.grad.comboBox_PRH_VH.currentIndex() > 0)
        )

        # VH or PRH > 1 DA
        condition_lv_71_3 = self.grad.comboBox_PRH_VH.currentIndex() > 1

        if condition_lv_71_1 or condition_lv_71_2 or condition_lv_71_3:
            self.levels = "71"

        # levels为 81&85 的情况
        condition_lv_81_85 = (self.grad.comboBox_VH_extent.currentIndex() == 2) or (
            self.grad.comboBox_RD.currentIndex() > 1
        )

        if condition_lv_81_85:
            self.levels = "81 & 85"

        # levels为 90 的情况
        # Laser scars or FPD or FPE, but NVD and NVE absent
        condition_lv_90 = (
            self.grad.comboBox_LASER.currentIndex() > 1
            or self.grad.comboBox_FP.currentIndex() > 0
        ) and (
            (self.grad.comboBox_NVD.currentIndex() == 0)
            and (self.grad.comboBox_NVE.currentIndex() == 0)
        )
        if condition_lv_90:
            self.levels = "90"

    def _init_app(self):
        app = QApplication.instance()
        app.setStyle("Fusion")

    def _init_next_and_previous_button(self):
        self.img_dock.pushButton_next.clicked.connect(self.on_next_clicked)
        self.img_dock.pushButton_next.clicked.connect(self.on_display_img)
        self.img_dock.pushButton_next.clicked.connect(self.displace_photo_number)

        self.img_dock.pushButton_next.clicked.connect(self.disable_next_button)

        self.img_dock.pushButton_next.clicked.connect(self.enable_previous_button)

        self.img_dock.pushButton_previous.clicked.connect(self.on_previous_clicked)
        self.img_dock.pushButton_previous.clicked.connect(self.on_display_img)
        self.img_dock.pushButton_previous.clicked.connect(self.displace_photo_number)
        self.img_dock.pushButton_previous.clicked.connect(self.disable_previous_button)

        self.img_dock.pushButton_previous.clicked.connect(self.enable_next_button)

    def disable_next_button(self):
        if self.img_index + 1 == self.num_img:
            self.img_dock.pushButton_next.setEnabled(False)

    def disable_previous_button(self):
        if self.img_index + 1 == 1:
            self.img_dock.pushButton_previous.setEnabled(False)

    def enable_previous_button(self):
        if self.img_index + 1 != 1:
            self.img_dock.pushButton_previous.setEnabled(True)

    def enable_next_button(self):
        if self.img_index + 1 != self.num_img:
            self.img_dock.pushButton_next.setEnabled(True)

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
        self.menu.export.setEnabled(False)
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
        self.grad.comboBox_gradable.setCurrentText("Yes")
        self.grad.comboBox_clarity.setCurrentText("Clear")
        self.grad.comboBox_is_dr.setCurrentText("Yes")
        self.grad.comboBox_diagnoses.setCurrentText("AMD")
        self.grad.lineEdit_other_diagnoses.setText("test other diagnosis")

        self.grad.comboBox_ICDR.setCurrentText("PDR")

        self.grad.comboBox_MA.setCurrentText("Present")
        self.grad.comboBox_RH.setCurrentIndex(1)
        self.grad.comboBox_HE.setCurrentIndex(0)
        self.grad.comboBox_SE.setCurrentIndex(0)
        self.grad.comboBox_IRMA.setCurrentIndex(0)
        self.grad.comboBox_VB.setCurrentIndex(0)
        self.grad.comboBox_NVD.setCurrentIndex(0)
        self.grad.comboBox_NVE.setCurrentIndex(0)
        self.grad.comboBox_FP.setCurrentIndex(0)
        self.grad.comboBox_PRH_VH.setCurrentIndex(0)
        self.grad.comboBox_VH_extent.setCurrentIndex(0)
        self.grad.comboBox_VEN.setCurrentIndex(0)
        self.grad.comboBox_LASER.setCurrentIndex(0)
        self.grad.comboBox_RD.setCurrentIndex(0)

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
            "Email: xujialiuphd@gmail.com<br>"
            'Website: <a href="github.com/xujialiu/ETDR-grading-app">https://github.com/xujialiu/ETDR-grading-app</a><br>'
            ''
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
            exec(f"{code}")
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
                self.set.folder_button.setEnabled(False)
                self.menu.export.setEnabled(True)
            else:
                QMessageBox.information(self, "Login Successful", "You are logged in.")
                self.islogin = True
                self.isroot = False
                self.menu.reset.setEnabled(True)
                self.set.lineEdit_user.setEnabled(False)
                self.set.lineEdit_password.setEnabled(False)
                self.set.pushButton_login.setEnabled(False)
                self.set.folder_button.setEnabled(True)
                self.menu.export.setEnabled(True)

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
        # general
        self.grad.comboBox_gradable.setCurrentIndex(0)
        self.grad.comboBox_clarity.setCurrentIndex(-1)
        self.grad.comboBox_is_dr.setCurrentText("Yes")
        self.grad.comboBox_diagnoses.setCurrentIndex(-1)
        self.grad.lineEdit_other_diagnoses.setText("")
        self.grad.comboBox_ICDR.setCurrentIndex(-1)

        # ETDR
        comboboxes = (combobox for _, (combobox, _) in self.dict_comboboxes.items())
        for combobox in comboboxes:
            combobox.setCurrentIndex(-1)

        self._set_enabled_etdr()
        self.grad.comboBox_VH_extent.setCurrentIndex(-1)

        # Others
        self.grad.comboBox_confident.setCurrentText("Yes")
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

    def _init_combobox_ma(self):
        self.grad.comboBox_MA.currentTextChanged.connect(self.on_ma_text_changed)

    def on_ma_text_changed(self):
        if self.grad.comboBox_MA.currentText() == "Absent":
            self._set_disabled_etdr_except(["MA", "RH"])
            print(1)
        if self.grad.comboBox_MA.currentText() == "Present":
            self._set_enabled_etdr()

    # working
    def on_gradable_text_changed(self):
        if self.grad.comboBox_gradable.currentText() == "No":
            # disable全部
            self._set_disable_all_except_gradable()
        if self.grad.comboBox_gradable.currentText() == "Yes":
            # enable全部
            self._set_enabled_all()

        # self.enable_disable_all
        self.calculate_levels()
        self.calculate_display_levels_severity()

    def is_all_filled(self):
        # 如果是gradable为No, 直接返回True(其他选项不需要填写)
        if self.grad.comboBox_gradable.currentText() == "No":
            return True

        comboboxes_choices = [
            combobox.currentText() != ""
            for (combobox, _) in self.dict_comboboxes.values()
        ]

        # 如果gradable为Yes, 需要进一步判断combobox_with_hover
        if (
            self.grad.comboBox_gradable.currentText() == "Yes"
            and all(comboboxes_choices)
            and self.grad.comboBox_confident.currentText()
            and self.grad.comboBox_clarity.currentText()
        ):
            return True

        # 其余情况, 返回false
        else:
            return False

    def _check_login_all_filled(self):
        if not self.islogin:
            QMessageBox.warning(self, "Error", "Please login!")
            return False
        elif not self.is_all_filled():
            QMessageBox.warning(self, "Error", "Please fill all options!")
            return False
        else:
            return True

    def on_save_clicked(self):
        if self._check_login_all_filled():

            self.update_df_database()
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

    def update_df_database(self):
        dict_results = {
            # basic info
            "patient_id": self.patient_id,
            "visit_date": self.visit_date,
            "grader": self.user,
            "eye": self.eye,
            "levels": self.levels,
            "severity": self.severity,
            # general
            "is_gradable": self.grad.comboBox_gradable.currentText(),
            "clarity": self.grad.comboBox_clarity.currentText(),
            "is_dr": self.grad.comboBox_is_dr.currentText(),
            "combobox_diagnoses": self.grad.comboBox_diagnoses.currentText(),
            "other_diagnoses": self.grad.lineEdit_other_diagnoses.text(),
            "ICDR": self.grad.comboBox_ICDR.currentText(),
            # etdr
            "MA": self.grad.comboBox_MA.currentText(),
            "RH": self.grad.comboBox_RH.currentText(),
            "RH_quadrants": self.grad.spinBox_RH_quadrants.value(),
            "HE": self.grad.comboBox_HE.currentText(),
            "SE": self.grad.comboBox_SE.currentText(),
            "IRMA": self.grad.comboBox_IRMA.currentText(),
            "IRMA_quadrants": self.grad.spinBox_IRMA_quadrants.value(),
            "VB": self.grad.comboBox_VB.currentText(),
            "VB_quadrants": self.grad.spinBox_VB_quadrants.value(),
            "NVD": self.grad.comboBox_NVD.currentText(),
            "NVE": self.grad.comboBox_NVE.currentText(),
            "NVE_quadrants": self.grad.spinBox_NVE_quadrants.value(),
            "FP": self.grad.comboBox_FP.currentText(),
            "PRH_VH": self.grad.comboBox_PRH_VH.currentText(),
            "VEN": self.grad.comboBox_VEN.currentText(),
            "LASER": self.grad.comboBox_LASER.currentText(),
            "RD": self.grad.comboBox_RD.currentText(),
            # others
            "confident": self.grad.comboBox_confident.currentText(),
            "comment": self.grad.textEdit_comment.toPlainText(),
        }
        df_data = pd.DataFrame([dict_results])
        self.df_database = pd.concat([self.df_database, df_data])

    def comboboxes_options(self):
        with open(".meta/combobox_options.json", "r", encoding="utf-8") as f:
            options_data = json.load(f)

        self.options_MA = self._parse_options(options_data["MA"])
        self.options_RH = self._parse_options(options_data["RH"])
        self.options_HE = self._parse_options(options_data["HE"])
        self.options_SE = self._parse_options(options_data["SE"])
        self.options_IRMA = self._parse_options(options_data["IRMA"])
        self.options_VB = self._parse_options(options_data["VB"])
        self.options_NVD = self._parse_options(options_data["NVD"])
        self.options_NVE = self._parse_options(options_data["NVE"])
        self.options_FP = self._parse_options(options_data["FP"])
        self.options_PRH_VH = self._parse_options(options_data["PRH_VH"])
        self.options_VEN = self._parse_options(options_data["VEN"])
        self.options_LASER = self._parse_options(options_data["LASER"])
        self.options_RD = self._parse_options(options_data["RD"])

    def _parse_options(self, options_dict):
        return {
            key: OptionScoreImgPath(value["score"], value["image"])
            for key, value in options_dict.items()
        }


if __name__ == "__main__":
    TEST_MODE = True

    app = QApplication(sys.argv)
    mwImpl = MainWindowImpl(test_mode=TEST_MODE)
    mwImpl.show()
    sys.exit(app.exec())
