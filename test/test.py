import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class new_text(QTextEdit):
    def __init__(self):
        super(new_text, self).__init__()
        self.setFrameShape(QFrame.NoFrame)
        self.resize(QSize(100, 70))


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        self.resize(QSize(500, 500))
        dock1 = QDockWidget('the test dock1..')
        dock2 = QDockWidget('the test dock2..')
        dock1.setAllowedAreas(Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
        dock2.setAllowedAreas(Qt.AllDockWidgetAreas)
        # dock1.setTitleBarWidget()
        self.addDockWidget(Qt.TopDockWidgetArea, dock1)
        self.addDockWidget(Qt.TopDockWidgetArea, dock2)
        # dock1.setFeatures(QDockWidget.DockWidgetVerticalTitleBar)
        # dock1.setFloating(True)
        # cw = QWidget()
        # self.setCentralWidget(cw)

        text_edit1 = new_text()
        text_edit2 = new_text()
        dock1.setWidget(text_edit1)
        dock2.setWidget(text_edit2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())