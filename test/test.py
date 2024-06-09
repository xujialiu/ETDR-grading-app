import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QHBoxLayout, QWidget
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
        self.left_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.left_dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.left_dock)

        # Right dock widget
        self.right_dock = QDockWidget("Right Dock", self)
        self.right_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.right_dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        self.addDockWidget(Qt.RightDockWidgetArea, self.right_dock)
        print("Right Dock Features:", self.right_dock.features())
        print("Right Dock Allowed Areas:", self.right_dock.allowedAreas())

    def _init_tabs(self):
        dummy_widget = my_widget()
        self.right_dock.setWidget(dummy_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())