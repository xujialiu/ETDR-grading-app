from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton

from ImageWindowImpl import ImageWindow


class HoverButton(QPushButton):
    def __init__(self, name, img_path, text='', parent=None):
        super().__init__(text, parent)
        self.image_window = ImageWindow(img_path)
        self.setObjectName(name)
        icon = QIcon()
        icon.addFile(u"question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon)

    def enterEvent(self, event):
        self.image_window.move(self.mapToGlobal(self.rect().bottomRight()))
        self.image_window.show()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.image_window.hide()
        super().leaveEvent(event)