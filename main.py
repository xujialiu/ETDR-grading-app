import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from MainWindowImpl import MainWindowImpl




if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = QMainWindow()
    mwImpl = MainWindowImpl(mw)
    mw.show()

    sys.exit(app.exec())
    
