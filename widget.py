import sys

from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
from ui_form import Ui_Widget
from sqlalchemy.orm import Session
from student import Student, engine, create, Group
from add_student import AddStudent

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        create()
        self.window_add_student = None
        self.ui.pushButton.clicked.connect(self.show_add)

    def show_add(self):
        if self.window_add_student is None:
            self.window_add_student = AddStudent()
        self.window_add_student.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())


