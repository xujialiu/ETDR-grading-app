from PySide6.QtWidgets import QHBoxLayout, QTextEdit, QWidget
from mainwindow import MainWindow


class my_widget(QWidget):
    def __init__(self, title):
        super(my_widget, self).__init__()
        self.setWindowTitle(title)
        text_edit = QTextEdit()
        box = QHBoxLayout()
        box.addWidget(text_edit)
        self.setLayout(box)

class MainWindowImpl(MainWindow):
    def __init__(self) -> None:
        super().__init__()
