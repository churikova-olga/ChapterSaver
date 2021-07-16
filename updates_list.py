import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import Qt
from PyQt5.QtCore import Qt as core
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
import parse_readmanga
import re

class Widget(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("updates_list.ui", self)
        self.setWindowIcon(QIcon('pixil_logo.png'))
        self.centralwidget.setStyleSheet("QWidget#centralwidget{background-image: url(back.jpg)} QListWidget {background: rgba(255,255,255,200)}")

        today = parse_readmanga.today
        def button1_clicked():
            f = open('datas.txt', 'w')
            f.write(str(today))
            f.close()

            for i in range(len(parse_readmanga.manga)):
                widget_manga = parse_readmanga.manga[i]
                #if len(widget_manga) >= 40:
                    #widget_manga = widget_manga[:40]+re.sub(' ', '\n', widget_manga[40:], 1)
                box = QtWidgets.QCheckBox(widget_manga)
                box.setStyleSheet('margin-left: 15px')
                #box.setMinimumHeight(100)
                box.setFont(QtGui.QFont("Joystix", 9))
                item = Qt.QListWidgetItem()
                #self.listWidget.setSpacing(10)
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item, box)
        self.pushButton_4.clicked.connect(button1_clicked)




app = QtWidgets.QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())
