
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import Qt
from PyQt5.QtGui import QIcon
import datetime
import parse_readmanga
import start_window
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setFixedSize(783, 776)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        self.MainWindow.setFont(font)
        self.MainWindow.setAutoFillBackground(False)
        self.MainWindow.setStyleSheet("QPushButton{\n"
"    color: #fe6637;\n"
"    background: #2a2a5c;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #fe6637;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #5959a8;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 40, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"text-shadow: 2px 0 0 #fff, -2px 0 0 #fff, 0 2px 0 #fff, 0 -2px 0 #fff, 1px 1px #fff, -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 111, 101))
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pixel_logo.png"))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 110, 701, 511))
        font = QtGui.QFont()
        font.setFamily("Joystix")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listWidget.setAutoScroll(False)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 640, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 640, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 690, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.MainWindow.setWindowIcon(QIcon('pixil_logo.png'))
        self.centralwidget.setStyleSheet(
            "QWidget#centralwidget{background-image: url(back.jpg)} QListWidget {background: rgba(255,255,255,200)}")

        now = datetime.datetime.now()
        today = datetime.date(now.year, now.month, now.day)

        f = open('manga.txt', 'r', encoding='utf-8')
        for i in f:
            widget_manga = i[:-1]
            item = Qt.QListWidgetItem(widget_manga)
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setFont(QtGui.QFont("Times New Roman", 10))
            self.listWidget.addItem(item)

        def button1_clicked():
            parse_readmanga.main()
            f = open('datas.txt', 'w', encoding='utf-8')
            f.write(str(today))
            f.close()
            self.listWidget.clear()
            f = open('manga.txt', 'a', encoding='utf-8')
            g = open('update.txt', 'r', encoding='utf-8')
            x = open('manga.txt', 'r', encoding='utf-8')
            for elem in g:
                flag = False
                x.seek(0)
                for el in x:
                    if el==elem:
                        flag = True
                        break
                if not flag:
                    f.write(elem)

            x.close()
            g.close()
            f.close()
            x = open('manga.txt', 'r', encoding='utf-8')
            for line in x:
                widget_manga = line[:-1]
                item = Qt.QListWidgetItem(widget_manga)
                item.setCheckState(QtCore.Qt.Unchecked)
                item.setFont(QtGui.QFont("Times New Roman", 10))
                self.listWidget.addItem(item)
            x.close()

        def button2_clicked():
            for x in range(self.listWidget.count()):
                self.listWidget.item(x).setCheckState(QtCore.Qt.Checked)

        def button3_clicked():
            items = []
            deleted = open('deleted.txt', 'a', encoding='utf-8')
            for x in range(self.listWidget.count()):
                if self.listWidget.item(x).checkState() == QtCore.Qt.Checked:
                    items.append(self.listWidget.item(x).text())
                    deleted.write(items[-1]+'\n')
            deleted.close()
            f = open('manga.txt', 'r', encoding='utf-8')
            g = open('temp_manga.txt', 'w', encoding='utf-8')
            for elem in f:
                if elem[:-1] not in items:
                    g.write(elem)
            f.close()
            g.close()
            os.remove('manga.txt')
            os.rename('temp_manga.txt', 'manga.txt')
            button1_clicked()
        self.pushButton_4.clicked.connect(button1_clicked)
        self.pushButton_2.clicked.connect(button2_clicked)
        self.pushButton_3.clicked.connect(button3_clicked)
        self.pushButton.clicked.connect(self.clicked_start)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Выбор сайта"))
        self.label.setText(_translate("MainWindow", "ChapterSaver"))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать все"))
        self.pushButton_3.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_4.setText(_translate("MainWindow", "Обновить"))

    def clicked_start(self):
        self.MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = start_window.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())