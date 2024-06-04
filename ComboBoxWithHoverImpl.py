from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QHoverEvent
from PySide6.QtWidgets import QComboBox


class ComboBoxWithHover(QComboBox):
    def __init__(self, hover_label, images, parent=None):
        super().__init__(parent)
        self.hover_label = hover_label
        self.images = images
        self.view().setMouseTracking(True)
        self.view().viewport().installEventFilter(self)
        self.view().viewport().setAttribute(Qt.WA_Hover)

    def eventFilter(self, source, event):
        if event.type() == QHoverEvent.HoverMove and source == self.view().viewport():
            index = self.view().indexAt(event.pos())
            if index.isValid():
                option_text = self.itemText(index.row())
                image_path = self.images.get(option_text)
                if image_path:
                    self.hover_label.show_image(image_path, self.view().mapToGlobal(event.pos() + QPoint(20, 20)))
            else:
                self.hover_label.hide_image()
        elif event.type() == QHoverEvent.HoverLeave:
            self.hover_label.hide_image()
        return super().eventFilter(source, event)