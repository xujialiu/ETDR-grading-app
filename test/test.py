from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QToolButton
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 创建 QToolButton
        self.button1 = QToolButton(self)
        icon = QIcon()
        icon.addFile(u"question.png", QSize(), QIcon.Normal, QIcon.Off)
        # 设置图标
        self.button1.setIcon(icon)
    

        # 设置按钮的位置和大小
        self.button1.setGeometry(100, 100, 100, 50)
        
        # 设置窗口大小
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("QToolButton Example")

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    # 创建主窗口
    window = MainWindow()
    window.show()

    # 运行应用程序
    app.exec()