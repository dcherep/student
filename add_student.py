from PySide6.QtWidgets import  QWidget
from PySide6.QtWidgets import  QUiLoader


class AddStudent(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui=loader.load("add_student.ui", self)