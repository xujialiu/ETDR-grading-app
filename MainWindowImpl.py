# mainwindowimpl.py
from PySide6.QtWidgets import QHBoxLayout, QTextEdit, QWidget
from mainwindow import MainWindow
import gradwidget, setwidget
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

# from mainwindowimpl import MainWindowImpl


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

    def _init_setwidge(self):
        self.set = setwidget.Ui_MainWindow()
        self.set.setupUi(self)
        self.tabwidget.addTab(self.set.centralwidget, "Settings")

    def _init_gradwidge(self):
        self.grad = gradwidget.Ui_MainWindow()
        self.grad.setupUi(self)
        self.tabwidget.addTab(self.grad.centralwidget, "Grading Area")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mwImpl = MainWindowImpl()
    mwImpl.show()

    sys.exit(app.exec())
