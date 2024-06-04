from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QWidget


class ImageWindow(QWidget):
    def __init__(self, img_path):
        super().__init__()
        
        
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(img_path))
        self.resize(self.image_label.pixmap().size())