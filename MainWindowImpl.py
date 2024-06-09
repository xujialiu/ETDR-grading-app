# mainwindowimpl.py
from PySide6.QtWidgets import QHBoxLayout, QTextEdit, QWidget
from mainwindow import MainWindow
import gradwidge
import MainWindow_old


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
        self._init_grad_set()

    def _init_grad_set(self):

        dummy_widget_1 = my_widget()
        dummy_widget_2 = my_widget()
        dummy_widget_3 = my_widget()

        # self.grad = gradwidge.Ui_Form()
        # self.grad.setupUi(self)

        self.grad = MainWindow_old.Ui_MainWindow()
        self.grad.setupUi(self)
        
        self.tabwidget.addTab(self.grad.centralwidget, "Grading Area")
        self.tabwidget.addTab(dummy_widget_3, "Settings")
