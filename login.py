from PySide6.QtWidgets import  QWidget, QMessageBox
from PySide6.QtUiTools import  QUiLoader
from sqlalchemy.orm import Session
from student import engine, User

class Login(QWidget):
    def __init__(self,main_window, parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui=loader.load("login.ui",self)

        self.main_window=main_window

        self.ui.pushButton.clicked.connect(self.check_login)
        self.ui.pushButton_2.clicked.connect(self.close)

    def check_login(self):
        l=self.ui.lineEdit.text()
        p=self.ui.lineEdit_2.text()

        with Session(engine) as db:
            user=db.query(User).filter(User.loginr==l, User.password ==p).first()
            if user is None:
                msg = QMessageBox(self)
                msg.setText('Неверный логин или пароль')
                msg.exec()
            else:
                self.main_window.show()
                self.main_window.user =user
                self.main_window.check_role()
                self.main_window.load_students()
                self.close()