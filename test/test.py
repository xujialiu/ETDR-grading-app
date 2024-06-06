from PySide6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.comboBox = QComboBox()
        self.comboBox.addItems(["Item 1", "Item 2", "Item 3"])
        self.comboBox.setCurrentIndex(-1)  # 使QComboBox启动时没有选择任何项
        
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
