# mainwindowimpl.py
from PySide6.QtWidgets import QFileDialog, QHBoxLayout, QMessageBox, QTextEdit, QWidget
from mainwindow import MainWindow
import gradwidget, setwidget
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from util import OptionScoreImgPath, comboboxes_options

# from mainwindowimpl import MainWindowImpl
from ComboboxWithHover import ComboBoxWithHover, HoverLabel

user_data = {"xujialiu": "lxj"}


class my_widget(QWidget):
    def __init__(self):
        super(my_widget, self).__init__()
        text_edit = QTextEdit()
        box = QHBoxLayout()
        box.addWidget(text_edit)
        self.setLayout(box)


class MainWindowImpl(MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui_impl()

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
        comboboxes_options(self.grad)

        dict_comboboxes = {
            self.grad.comboBox_HMA: self.grad.options_HMA,
            self.grad.comboBox_HE: self.grad.options_HE,
            self.grad.comboBox_SE: self.grad.options_SE,
            self.grad.comboBox_IRMA: self.grad.options_IRMA,
            self.grad.comboBox_VB: self.grad.options_VB,
            self.grad.comboBox_NVD: self.grad.options_NVD,
            self.grad.comboBox_NVE: self.grad.options_NVE,
            self.grad.comboBox_FP: self.grad.options_FP,
            self.grad.comboBox_PRH_VH: self.grad.options_PRH_VH,
            self.grad.comboBox_EDEMA: self.grad.options_EDEMA,
            self.grad.comboBox_CTR: self.grad.options_CTR,
            self.grad.comboBox_VEN: self.grad.options_VEN,
            self.grad.comboBox_LASER: self.grad.options_LASER,
            self.grad.comboBox_RX: self.grad.options_RX,
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
        folder_path = QFileDialog.getExistingDirectory(
            self, "Select the data folder", "./"
        )
        if folder_path:
            self.set.label_folder.setText(folder_path)

    def _init_folder_button(self):
        self.set.folder_button.clicked.connect(self.select_folder)

    def _init_login_button(self):
        self.set.pushButton_login.clicked.connect(self.login_user)

    def login_user(self):

        user = self.set.lineEdit_user.text()
        password = self.set.lineEdit_password.text()

        if user in user_data and user_data[user] == password:
            QMessageBox.information(self, "Success", "Login successful!")
            self.islogin = True

        else:
            QMessageBox.warning(self, "Error", "Invalid username or password!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mwImpl = MainWindowImpl()
    mwImpl.show()

    sys.exit(app.exec())
