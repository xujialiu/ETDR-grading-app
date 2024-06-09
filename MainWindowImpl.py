from PySide6.QtWidgets import QHBoxLayout, QTextEdit, QWidget
from mainwindow import MainWindow
import tabwidget

class my_widget(QWidget):
    def __init__(self):
        super(my_widget, self).__init__()
        text_edit = QTextEdit()
        box = QHBoxLayout()
        box.addWidget(text_edit)
        self.setLayout(box)


class MainWindowImpl(MainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        # self.tabwidget = tabwidget.Ui_Form()
        # self.tabwidget.setupUi(self)
        
        # self.
        
        # self.right_dock.setWidget(self.tabwidget.tabWidget)
        self._init_grad_set()

    
    def _init_grad_set(self):
        
        dummy_widget_1 = my_widget()
        dummy_widget_2 = my_widget()
        dummy_widget_3 = my_widget()
        
        self.tabwidget.addTab(dummy_widget_1, "Grading Area")
        self.tabwidget.addTab(dummy_widget_3, "Settings")
        
        
        
    
    
