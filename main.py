import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from MainWindowImpl import MainWindowImpl


def before_quit():
    """do something before quit"""
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mwImpl = MainWindowImpl()
    mwImpl.show()

    app.aboutToQuit.connect(before_quit())

    sys.exit(app.exec())
