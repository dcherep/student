from PySide6.QtWidgets import  QWidget, QVBoxLayout
from PySide6.QtUiTools import  QUiLoader
from edit_student import EditStudent

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

                self.window_edit_student=None
                self.ui.pushButton.clicked.connect(self.show_edit)
                self.ui.pushButton_2.clicked.connect(self.show_delete)


        def show_edit(self):
                if self.window_edit_student is None:
                        self.window_edit_student= EditStudent(self.student)
                        self.window_edit_student.show()

        def show_delete(self):
                if self.window_delete_student is None:
                        self.window_delete_student= EditStudent(self.student)
                        self.window_edit_student.show()

