from PySide6.QtWidgets import QApplication, QComboBox

QApplication()
a = QComboBox()
a.addItems(["1", "2"])


# print(a.view())
print(a.view().viewport())
