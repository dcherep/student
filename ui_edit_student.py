# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_student.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(733, 543)
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(240, 330, 111, 24))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(240, 210, 113, 22))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 320, 161, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_5.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 200, 161, 31))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_2.setFont(font2)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 280, 161, 31))
        self.label_4.setFont(font2)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(240, 250, 113, 22))
        self.lineEdit_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 240, 161, 31))
        self.label_3.setFont(font2)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 430, 141, 61))
        font3 = QFont()
        font3.setPointSize(22)
        self.pushButton.setFont(font3)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 430, 141, 61))
        self.pushButton_2.setFont(font3)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(240, 290, 113, 22))
        self.lineEdit_3.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 120, 341, 81))
        font4 = QFont()
        font4.setPointSize(20)
        self.label.setFont(font4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 id \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0444\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u043e\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u043e\u0435 \u0438\u043c\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
    # retranslateUi

