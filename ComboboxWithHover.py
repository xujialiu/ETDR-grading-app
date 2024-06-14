from PySide6.QtCore import QEvent, QPoint, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QComboBox, QLabel


class HoverLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.ToolTip)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: white; border: 1px solid black;")
        self.setVisible(False)

    def show_image(self, image_path, item_rect_top_left):
        if not image_path:  # If image_path is empty, hide the label and return
            self.hide_image()
            return

        pixmap = QPixmap(image_path)
        self.setPixmap(pixmap)
        self.adjustSize()
        # Adjust position to show image on the left side of the item rectangle
        self.move(item_rect_top_left - QPoint(self.width() + 5, 0))
        self.setVisible(True)

    def hide_image(self):
        self.setVisible(False)


class ComboBoxWithHover(QComboBox):
    def __init__(self, hover_label, options, parent=None):
        super().__init__(parent)
        self.hover_label = hover_label
        self.options = options
        self.view().setMouseTracking(True)
        self.view().viewport().installEventFilter(self)
        self.view().viewport().setAttribute(Qt.WA_Hover)

        fixed_width = 150
        self.setMinimumWidth(fixed_width)
        self.setMaximumWidth(fixed_width)
        self.setCurrentIndex(1)

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseMove and source == self.view().viewport():
            index = self.view().indexAt(event.pos())
            if not index.isValid():
                self.hover_label.hide_image()
                return super().eventFilter(source, event)

            option_text = self.itemText(index.row())
            image_path = self.options[option_text].path
            if not image_path:
                self.hover_label.hide_image()
                return super().eventFilter(source, event)

            item_rect = self.view().visualRect(index)
            item_rect_top_left = self.view().mapToGlobal(item_rect.topLeft())
            self.hover_label.show_image(image_path, item_rect_top_left)
        elif event.type() in (QEvent.HoverLeave, QEvent.Leave):
            self.hover_label.hide_image()
        
        return super().eventFilter(source, event)
