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
        self.load_groups()
        self.window_add_student = None
        self.ui.pushButton.clicked.connect(self.show_add)
        self.ui.pushButton_2.clicked.connect(self.close)

    def show_add(self):
        if self.window_add_student is None:
            self.window_add_student = AddStudent()
        self.window_add_student.show()

    def addStudent(self):
        self.surname =self.ui.lineEdit.text()
        self.name =self.ui.lineEdit_2.text()
        self.patr =self.ui.lineEdit_3.text()
        self.group =int(self.ui.comboBox.currentData())
        msg = QMessageBox(self)
        try:
            with Session(autoflush=False,bind=engine) as db:
                new_student =Student(surname=self.surname,name=self.name,patr=self.patr,group_id=self.group)
                db.add(new_student)
                db.commit()
                msg.setText('Студент успешно добавлен')
                msg.exec()
        except Exception as e:
            msg.setText(f'Ошибка: {str(e)}')
            msg.exec()

    def load_groups(self):
        with Session(engine) as db:
            groups = db.query(Group).all()
            for group in groups:
                self.ui.comboBox.addItem(group.title,group.id)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())


