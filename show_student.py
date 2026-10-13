from PySide6.QtWidgets import  QWidget, QVBoxLayout, QMessageBox
from PySide6.QtUiTools import  QUiLoader
from sqlalchemy.orm import Session
from student import Student, engine, Group
from PySide6.QtGui import QPixmap
from pathlib import Path
from edit_student import EditStudent

BASE_DIR = Path(__file__).resolve().parent

class ShowStudent(QWidget):
        def __init__(self, st, parent=None):
                super().__init__(parent)
                loader=QUiLoader()
                self.ui=loader.load("show_student.ui")

                main_layout=QVBoxLayout(self)
                main_layout.addWidget(self.ui)

                self.student=st

                self.ui.label.setText(st.surname)
                self.ui.label_2.setText(st.name)
                self.ui.label_3.setText(st.patr)
                self.ui.label_4.setText(st.group.title)
                if st.logo == '':
                                if st.gender == 'Мужской':
                                                st.logo = BASE_DIR / 'images/no_logo_man.png'
                                else:
                                                st.logo = BASE_DIR / 'images/no_logo_woman.png'
                else:
                                st.logo = BASE_DIR / st.logo
                self.ui.label_5.setPixmap(QPixmap(BASE_DIR/st.logo))

                if parent.user.role.id != 1:
                                self.ui.pushButton.hide()
                                self.ui.pushButton_2.hide()




                self.window_edit_student=None
                self.ui.pushButton.clicked.connect(self.show_edit)
                self.ui.pushButton_2.clicked.connect(self.delete_student)


        def show_edit(self):
                if self.window_edit_student is None:
                        self.window_edit_student= EditStudent(self.student)
                        self.window_edit_student.show()

        def delete_student(self):
                reply = QMessageBox.question(
                self,
                'Вы уверены?',
                f'Вы действительно хотите удалить {self.student.surname} {self.student.name}?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
                )

                if reply == QMessageBox.StandardButton.Yes:
                                with Session (engine) as db:
                                                st= db.query(Student).get(self.student.id)
                                                db.delete(st)
                                                db.commit()
                                                msg=QMessageBox(self)
                                                msg.setText('Студент успешно удален')
                                                msg.exec()



