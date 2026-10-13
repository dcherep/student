import sys

from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
from ui_form import Ui_Widget
from sqlalchemy.orm import Session
from student import Student, engine, create, Group
from add_student import AddStudent
from show_student import ShowStudent
from login import Login


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        create()
        self.filter_group_id = None
        self.filter_surname = None
        self.user=None

        self.load_groups()
        #self.load_students()

        self.window_add_student = None
        self.window_edit_student = None
        self.ui.pushButton.clicked.connect(self.show_add)
        self.ui.pushButton_2.clicked.connect(self.exit)
        self.ui.comboBox.currentIndexChanged.connect(self.group_changed)
        self.ui.lineEdit.textChanged.connect(self.surname_changed)


    def exit(self):
        self.user=None
        self.hide()
        login_window.ui.lineEdit.setText('')
        login_window.ui.lineEdit_2.setText('')
        login_window.show()


    def surname_changed(self):
        if len(self.ui.lineEdit.text())>0:
            self.filter_surname = self.ui.lineEdit.text()
        else:
            self.filter_surname = None
        self.load_students()

    def group_changed(self, index):
        group_id=int(self.ui.comboBox.currentData())
        self.filter_group_id = group_id
        self.load_students()

    def clear_area(self):
        layout = self.ui.scrollArea.widget().layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()

    def load_students(self):
        self.clear_area()
        with Session(engine) as db:
            students = db.query(Student).all()
            if self.filter_group_id is not None:
                students = [s for s in students if s.group.id == self.filter_group_id]
            if self.filter_surname is not None:
                students = [s for s in students if s.surname.find(self.filter_surname) !=-1]
            for s in students:
                student = ShowStudent(s, self)
                self.ui.scrollAreaWidgetContents.layout().addWidget(student)
                student.show()

    def show_add(self):
        if self.window_add_student is None:
            self.window_add_student = AddStudent()
        self.window_add_student.show()


    def load_groups(self):
        with Session(engine) as db:
            groups = db.query(Group).all()
            for group in groups:
                self.ui.comboBox.addItem(group.title, group.id)

    def check_role(self):
        if self.user is None:
            return
        if self.user.role.id ==1:
            pass
        elif self.user.role.id ==2:
            self.ui.pushButton.hide()
        else:
            self.ui.groupBox.hide()
            self.ui.pushButton.hide()
            self.ui.pushButton_2.hide()
            for i in range(self.ui.verticalLayout_2.count()):
                item = self.ui.verticalLayout_2.itemAt(i)
                widget = item.widget()
                if widget is not None:
                    widget.setVisible(False)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    login_window = Login(widget)
    login_window.show()
    sys.exit(app.exec())


