import sys

from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
from ui_form import Ui_Widget
from sqlalchemy.orm import Session
from student import Student, engine, create

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        create()
        self.ui.pushButton.clicked.connect(self.addStudent)

    def addStudent(self):
        self.surname =self.ui.lineEdit.text()
        self.name =self.ui.lineEdit_2.text()
        self.patr =self.ui.lineEdit_3.text()
        self.group =int(self.ui.lineEdit_4.text())
        msg = QMessageBox(self)
        try:
            with Session(autoflush=False,bind=engine) as db:
                new_student =Student(surname=self.surname,name=self.name,patr=self.patr,group_id=self.group)
                db.add(new_student)
                db.commit()
                msg.setText('Студент успешно добавлен')
                msg.exec()
        except Exception as e:
            msg.setText(f'{str(e)}')
            msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())


