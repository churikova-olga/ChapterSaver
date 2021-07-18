from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import Qt
from PyQt5.QtCore import Qt as core
from PyQt5.QtGui import QIcon
import parse_readmanga

class Widget(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        self.setWindowIcon(QIcon('pixil_logo.png'))
        self.setStyleSheet("QWidget#Form{background-image: url(back.jpg)}\
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
        lay = Qt.QVBoxLayout(self)
        lay.addWidget(self.login_lineEdit)
        lay.addWidget(self.password_lineEdit)

        #if check == 'False':
            #self.login_Button.clicked.connect(self.closeEvent)
    def my_slot_function(self):
        f = open('login.txt', 'w', encoding='utf-8')
        password = (self.password_lineEdit.text())
        login = (self.login_lineEdit.text())
        f.write(login+'\n'+password)
        f.close()
        parse_readmanga.main()
        check = open('check.txt', 'r')
        check = check.readline()
        print(check)

    #def closeEvent(self, event):
        #reply = QMessageBox(self, 'Message',
            #"Неверный логин или пароль, порбуйте еще раз", QMessageBox.Ok)
        #if reply == QMessageBox.Ok:
            #event.ignore()



app = QtWidgets.QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())
