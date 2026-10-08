from PySide6.QtWidgets import  QWidget, QMessageBox
from PySide6.QtUiTools import  QUiLoader
from sqlalchemy.orm import Session
from student import Student, engine, Group

class EditStudent(QWidget):
    def __init__(self,st, parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui=loader.load("edit_student.ui",self)

        self.student=st
        self.ui.lineEdit.setText(st.surname)
        self.ui.lineEdit_2.setText(st.name)
        self.ui.lineEdit_3.setText(st.patr)
        index = self.ui.comboBox.findData(st.group.id)
        self.ui.comboBox.setCurrentIndex(index)

        self.load_groups()
        self.ui.pushButton.clicked.connect(self.save_student)
        self.ui.pushButton_2.clicked.connect(self.close)

    def save_student(self):
        new_surname =self.ui.lineEdit.text()
        new_name =self.ui.lineEdit_2.text()
        new_patr =self.ui.lineEdit_3.text()
        new_group =self.ui.comboBox.currentData()

        with Session(engine) as db:
            st=db.query(Student).get(self.student.id)
            st.surname=new_surname
            st.name=new_name
            st.patr=new_patr
            st.group_id=new_group
            db.commit()
            msg = QMessageBox(self)
            msg.setText('Студент успешно изменен')
            msg.exec()


    def load_groups(self):
        with Session(engine) as db:
            groups = db.query(Group).all()
            for group in groups:
                self.ui.comboBox.addItem(group.title,group.id)
