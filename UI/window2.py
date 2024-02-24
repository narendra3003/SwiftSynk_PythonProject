

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 740)
        MainWindow.setGeometry(420, 225, 1080, 740)
        MainWindow.setStyleSheet("#widget1{\n"
"    background-color: rgb(106, 90, 205)\n"
"}\n"
"\n"
"#table2{\n"
"    background-color: rgb(194, 194, 255);\n"
"    border-width: 0px;\n"
"    gridline-color: rgb(194, 194, 255)\n"
"}\n"
"\n"
"#backbutton{\n"
"    background-color: rgb(194, 194, 255);\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius: 6\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 1081, 62))
        self.widget1.setStyleSheet("")
        self.widget1.setObjectName("widget1")
        self.backbutton = QtWidgets.QPushButton(self.widget1)
        self.backbutton.setGeometry(QtCore.QRect(10, 10, 112, 42))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backbutton.setFont(font)
        self.backbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backbutton.setObjectName("backbutton")
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(0, 58, 1082, 682))
        self.widget2.setObjectName("widget2")
        self.table2 = QtWidgets.QTableWidget(self.widget2)
        self.table2.setGeometry(QtCore.QRect(-10, 2, 1102, 682))
        self.table2.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: none\n"
"}")
        self.table2.setObjectName("table2")
        self.table2.verticalHeader().setVisible(False)
        self.table2.setColumnCount(5)
        self.table2.setColumnWidth(0, 50)
        self.table2.setColumnWidth(1, 150)
        self.table2.setColumnWidth(2, 100)
        self.table2.setColumnWidth(3, 400)
        self.table2.setColumnWidth(4, 100)
        self.table2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(4, item)
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.backbutton.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backbutton.setText(_translate("MainWindow", "◀ Back"))
        item = self.table2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.table2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Path"))
        item = self.table2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Size"))


class StaticWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow = StaticWindow()
    MainWindow.show()
    sys.exit(app.exec_())
