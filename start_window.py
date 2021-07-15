import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import Qt
from PyQt5.QtCore import Qt as core
from PyQt5.QtGui import QIcon


class Widget(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("start.ui", self)
        self.setWindowIcon(QIcon('pixil_logo.png'))
        self.listWidget.setStyleSheet("font-size: 20px")
        self.centralwidget.setStyleSheet("QWidget#centralwidget{background-image: url(back.jpg)} QListWidget {background: rgba(255,255,255,200)}")
        item_text_list = ['ReadManga.live', 'ReManga', 'Tl.Rulate.ru']

        for item_text in item_text_list:
            item = Qt.QListWidgetItem(item_text)
            item.setTextAlignment(core.AlignHCenter)
            self.listWidget.addItem(item)




app = QtWidgets.QApplication(sys.argv)
ex=Widget()
ex.show()
sys.exit(app.exec_())
