# MainWindow.py
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QDockWidget,
    QTabWidget,
    QTextEdit,
    QWidget,
)
from PySide6.QtCore import Qt


class my_widget(QWidget):
    def __init__(self):
        super(my_widget, self).__init__()
        text_edit = QTextEdit()
        box = QHBoxLayout()
        box.addWidget(text_edit)
        self.setLayout(box)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1500, 800)
        self.init_ui()

    def init_ui(self):
        self._init_docks()

    def _init_docks(self):

        # Left dock widget
        self.left_dock = QDockWidget("Left Dock", self)
        # 设置能够dock在左右, 但是pyside6的代码似乎有问题
        # TopDockWidgetArea和BottomDockWidgetArea代表左右
        # LeftDockWidgetArea和RightDockWidgetArea代表上下
        self.left_dock.setAllowedAreas(Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
        self.left_dock.setFeatures(
            QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable
        )
        self.addDockWidget(Qt.TopDockWidgetArea, self.left_dock)

        # Right dock widget
        self.right_dock = QDockWidget("Right Dock", self)
        # 问题同上
        self.right_dock.setAllowedAreas(Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
        self.right_dock.setFeatures(
            QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable
        )
        self.addDockWidget(Qt.TopDockWidgetArea, self.right_dock)
