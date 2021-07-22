
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
import parse_readmanga
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
import updates_list
import start_window

class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.setFixedSize(783, 773)
        self.Form.setStyleSheet("QWidget#Form{\n"
"    background-image: url(back.jpg);\n"
"}\n"
"QPushButton{\n"
"    color: #fe6637;\n"
"    background: #2a2a5c;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #fe6637;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #5959a8;\n"
"}")
        self.login_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.login_lineEdit.setGeometry(QtCore.QRect(130, 280, 511, 41))
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.password_lineEdit.setGeometry(QtCore.QRect(130, 380, 511, 41))
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.back_Button = QtWidgets.QPushButton(self.Form)
        self.back_Button.setGeometry(QtCore.QRect(130, 470, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.back_Button.setFont(font)
        self.back_Button.setObjectName("back_Button")
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(70, 40, 641, 61))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background: rgba(255,255,255,200)")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.site_name = QtWidgets.QLabel(self.Form)
        self.site_name.setGeometry(QtCore.QRect(130, 170, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Joystix")
        font.setPointSize(14)
        self.site_name.setFont(font)
        self.site_name.setAlignment(QtCore.Qt.AlignCenter)
        self.site_name.setObjectName("site_name")
        self.login_label = QtWidgets.QLabel(self.Form)
        self.login_label.setGeometry(QtCore.QRect(130, 260, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Joystix")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.password_label = QtWidgets.QLabel(self.Form)
        self.password_label.setGeometry(QtCore.QRect(130, 360, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Joystix")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.frame = QtWidgets.QFrame(self.Form)
        self.frame.setGeometry(QtCore.QRect(70, 150, 641, 441))
        self.frame.setStyleSheet("border: 1px solid black;\n"
"background: rgba(255,255,255,200)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.login_Button = QtWidgets.QPushButton(self.Form)
        self.login_Button.setGeometry(QtCore.QRect(440, 470, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.login_Button.setFont(font)
        self.login_Button.setObjectName("login_Button")
        self.frame.raise_()
        self.login_lineEdit.raise_()
        self.password_lineEdit.raise_()
        self.back_Button.raise_()
        self.label.raise_()
        self.site_name.raise_()
        self.login_label.raise_()
        self.password_label.raise_()
        self.login_Button.raise_()

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        self.Form.setWindowIcon(QIcon('pixil_logo.png'))
        self.Form.setStyleSheet("QWidget#Form{background-image: url(back.jpg)}\
               QPushButton{\
               	color: #fe6637;\
               	background: #2a2a5c;\
               	border-radius: 8px;\
               	border: 2px solid #fe6637;\
               }\
               QPushButton:hover{\
               	background: #5959a8;\
               }")
        self.site_name.setText('ReadManga.live')

        self.login_Button.clicked.connect(self.my_slot_function)
        self.back_Button.clicked.connect(self.clicked_start)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.back_Button.setText(_translate("Form", "Назад"))
        self.label.setText(_translate("Form", "Введите логин и пароль от вашей учетной записи на сайте"))
        self.site_name.setText(_translate("Form", "Site name"))
        self.login_label.setText(_translate("Form", "Логин"))
        self.password_label.setText(_translate("Form", "Пароль"))
        self.login_Button.setText(_translate("Form", "Войти"))

    def my_slot_function(self):
        f = open('login.txt', 'w', encoding='utf-8')
        login = (self.login_lineEdit.text())
        password = (self.password_lineEdit.text())
        f.write(login+'\n'+password+'\n')
        f.close()
        parse_readmanga.main()
        check = open('check.txt', 'r')
        check = check.readline()
        if check == 'False':
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Неправильно введен логин или пароль")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            self.Form.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = updates_list.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

    def clicked_start(self):
        self.Form.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = start_window.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
