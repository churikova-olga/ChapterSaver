
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import Qt
from PyQt5.QtCore import Qt as core
from PyQt5.QtGui import QIcon
import login_window

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setFixedSize(783, 776)
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(80, 160, 600, 500))
        font = QtGui.QFont()
        font.setFamily("Joystix")
        font.setPointSize(22)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("")
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 700, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 601, 101))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 20, 601, 121))
        self.frame.setStyleSheet("background: rgba(255,255,255,200)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.listWidget.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.MainWindow.setWindowIcon(QIcon('pixil_logo.png'))
        self.listWidget.setStyleSheet("font-size: 20px")
        self.centralwidget.setStyleSheet(
            "QWidget#centralwidget{background-image: url(back.jpg)} QListWidget {background: rgba(255,255,255,200)}")
        item_text_list = ['ReadManga.live', 'ReManga', 'Tl.Rulate.ru']

        for item_text in item_text_list:
            item = Qt.QListWidgetItem(item_text)
            item.setTextAlignment(core.AlignHCenter)
            self.listWidget.addItem(item)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = login_window.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Дальше"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Добро пожаловать в приложение ChapterSaver!</span></p><p align=\"center\">Выберете один из сайтов обновления которого вы бы</p><p align=\"center\">хотели получить:</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
