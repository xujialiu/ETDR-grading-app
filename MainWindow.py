# mainwindow.py
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QDockWidget,
    QTableWidget,
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
        self.setWindowTitle("Diabetic Retinopathy Grading System")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        self._init_docks()
        self._init_tabs()

    def _init_docks(self):

        # Left dock widget
        self.left_dock = QDockWidget("Left Dock", self)
        self.left_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.left_dock.setFeatures(
            QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable
        )
        self.addDockWidget(Qt.TopDockWidgetArea, self.left_dock)

        # Right dock widget
        self.right_dock = QDockWidget("Right Dock", self)
        self.right_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.right_dock.setFeatures(
            QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable
        )
        self.addDockWidget(Qt.TopDockWidgetArea, self.right_dock)


        print(self.right_dock.allowedAreas())

    def _init_tabs(self):
        dummy_widget_1 = my_widget()
        dummy_widget_2 = my_widget()
        self.right_dock.setWidget(dummy_widget_1)
        self.left_dock.setWidget(dummy_widget_2)

