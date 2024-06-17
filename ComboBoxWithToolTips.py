from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Qt

class ComboBoxWithToolTips(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setToolTip("Select an option")

    def showPopup(self):
        for i in range(self.count()):
            item = self.view().indexWidget(self.model().index(i, 0))
            if item:
                item.setToolTip(self.itemData(i, Qt.ToolTipRole))
        super().showPopup()