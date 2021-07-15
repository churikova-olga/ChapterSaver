import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import Qt
from PyQt5.QtCore import Qt as core
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

class Widget(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("updates_list.ui", self)
        self.setWindowIcon(QIcon('pixil_logo.png'))
        self.centralwidget.setStyleSheet("QWidget#centralwidget{background-image: url(back.jpg)} QListWidget {background: rgba(255,255,255,200)}")
        box = QtWidgets.QCheckBox('Возвращение замороженного игрока 1-38')
        box.setStyleSheet('margin-left: 15px')
        box.setFont(QtGui.QFont("Joystix", 9))
        item = Qt.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, box)


app = QtWidgets.QApplication(sys.argv)
ex=Widget()
ex.show()
sys.exit(app.exec_())
