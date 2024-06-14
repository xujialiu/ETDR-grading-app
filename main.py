# main.py
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from MainWindowImpl import MainWindowImpl

TEST_MODE = True
if __name__ == "__main__":
    app = QApplication(sys.argv)

    mwImpl = MainWindowImpl(test_mode=False)

    mwImpl.show()

    sys.exit(app.exec())