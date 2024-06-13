from PySide6.QtWidgets import QDialog
from RegisterDialog import Ui_Dialog


# class RegisterDialog(Ui_Dialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)
        
        
class RegisterDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.setupUi(self)