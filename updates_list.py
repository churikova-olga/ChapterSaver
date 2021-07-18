import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import Qt
from PyQt5.QtCore import Qt as core
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
import datetime
import parse_readmanga
import re


class Widget(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("updates_list.ui", self)
        self.setWindowIcon(QIcon('pixil_logo.png'))
        self.centralwidget.setStyleSheet("QWidget#centralwidget{background-image: url(back.jpg)} QListWidget {background: rgba(255,255,255,200)}")

        now = datetime.datetime.now()
        today = datetime.date(now.year, now.month, now.day)

        f = open('manga.txt', 'r', encoding = 'utf-8')
        last_manga = f.readlines()
        for i in range(len(last_manga)):
            box = QtWidgets.QCheckBox(' '.join(last_manga[i].split()))
            box.setStyleSheet('margin-left: 15px')
            # box.setMinimumHeight(100)
            box.setFont(QtGui.QFont("Times New Romans", 7))
            item = Qt.QListWidgetItem()
            # self.listWidget.setSpacing(10)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, box)

        def button1_clicked():
            parse_readmanga.main()
            f = open('datas.txt', 'w', encoding = 'utf-8')
            f.write(str(today))
            f.close()
            self.listWidget.clear()
            f = open('manga.txt', 'w', encoding = 'utf-8')
            g = open('update.txt', 'r', encoding = 'utf-8')
            for line in g:
                widget_manga = line[:-1]
                #if len(widget_manga) >= 40:
                    #widget_manga = widget_manga[:40]+re.sub(' ', '\n', widget_manga[40:], 1)
                box = QtWidgets.QCheckBox(widget_manga)
                box.setStyleSheet('margin-left: 15px')
                #box.setMinimumHeight(100)
                box.setFont(QtGui.QFont("Times New Romans", 7))
                item = Qt.QListWidgetItem()
                #self.listWidget.setSpacing(10)
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item, box)
                f.write(str(widget_manga)+'\n')
            f.close()
        self.pushButton_4.clicked.connect(button1_clicked)

app = QtWidgets.QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())
