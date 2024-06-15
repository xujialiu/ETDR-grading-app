# main.py
import sys
from PySide6.QtWidgets import QApplication
from MainWindowImpl import MainWindowImpl


TEST_MODE = True

app = QApplication(sys.argv)
app.setStyle("fusion")

mwImpl = MainWindowImpl(test_mode=TEST_MODE)
mwImpl.show()

sys.exit(app.exec())
