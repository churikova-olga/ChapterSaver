import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import Qt
from PyQt5.QtCore import Qt as core
from PyQt5.QtGui import QIcon

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

app = QtWidgets.QApplication(sys.argv)
ex=Widget()
ex.show()
sys.exit(app.exec_())
