import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QMessageBox
from PySide6.QtCore import Signal, Slot

class DebugWindow(QWidget):
    code_submitted = Signal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Debug Window")
        self.layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.text_edit)

        self.execute_button = QPushButton("Execute", self)
        self.execute_button.clicked.connect(self.on_execute_clicked)
        self.layout.addWidget(self.execute_button)

        self.setLayout(self.layout)

    def on_execute_clicked(self):
        code = self.text_edit.toPlainText()
        self.code_submitted.emit(code)