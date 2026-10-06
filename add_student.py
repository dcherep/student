from PySide6.QtWidgets import  QWidget,QMessageBox
from PySide6.QtUiTools import  QUiLoader
from sqlalchemy.orm import Session
from student import Student, engine, Group


class AddStudent(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui=loader.load("add_student.ui", self)

        self.load_groups()
        self.ui.pushButton.clicked.connect(self.save_student)
        self.ui.pushButton_2.clicked.connect(self.close)

    def save_student(self):
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

