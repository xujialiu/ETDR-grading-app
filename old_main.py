import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from old_MainWindowImpl import MainWindowImpl


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mwImpl = MainWindowImpl()
    mwImpl.show()

    sys.exit(app.exec())
