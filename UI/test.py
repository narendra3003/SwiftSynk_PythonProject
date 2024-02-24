


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 370)
        MainWindow.setStyleSheet("#widget1{\n"
"    background-color: rgb(106, 90, 205)\n"
"}\n"
"\n"
"#table1{\n"
"    background-color: rgb(194, 194, 255)\n"
"}\n"
"\n"
"#table2{\n"
"    background-color: rgb(194, 194, 255)\n"
"}\n"
"\n"
"#syncButton{\n"
"    background-color: rgb(106, 90, 205);\n"
"    border-top-left-radius: 12;\n"
"    border-bottom-left-radius: 12;\n"
"    color: white\n"
"}\n"
"\n"
"#syncButton2{\n"
"    background-color: rgb(106, 90, 205);\n"
"    border-top-right-radius: 12;\n"
"    border-bottom-right-radius: 12;\n"
"    color: white;\n"
"    border-left-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"#mainlabel{\n"
"    color: white\n"
"}\n"
"\n"
"#logwid{\n"
"    background-color: rgb(205, 208, 255);\n"
"    border-radius: 25;\n"
"    drop-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);\n"
"}\n"
"\n"
"#emailbox{\n"
"    border-radius: 5\n"
"}\n"
"#passbox{\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 541, 31))
        self.widget1.setStyleSheet("")
        self.widget1.setObjectName("widget1")
        self.mainlabel = QtWidgets.QLabel(self.widget1)
        self.mainlabel.setGeometry(QtCore.QRect(7, 5, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.mainlabel.setFont(font)
        self.mainlabel.setObjectName("mainlabel")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 29, 541, 341))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.table1 = QtWidgets.QTableWidget(self.page)
        self.table1.setGeometry(QtCore.QRect(0, 0, 541, 341))
        self.table1.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: none\n"
"}")
        self.table1.setObjectName("table1")
        self.table1.setColumnCount(5)
        self.table1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table1.setHorizontalHeaderItem(4, item)
        self.syncButton = QtWidgets.QPushButton(self.page)
        self.syncButton.setGeometry(QtCore.QRect(440, 280, 45, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.syncButton.setFont(font)
        self.syncButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.syncButton.setObjectName("syncButton")
        self.syncButton2 = QtWidgets.QPushButton(self.page)
        self.syncButton2.setGeometry(QtCore.QRect(486, 280, 45, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.syncButton2.setFont(font)
        self.syncButton2.setStyleSheet("#syncButton2{\n"
"    text : SYNC \\n Folder\n"
"}")
        self.syncButton2.setObjectName("syncButton2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.table2 = QtWidgets.QTableWidget(self.page_2)
        self.table2.setGeometry(QtCore.QRect(0, 0, 541, 341))
        self.table2.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: none\n"
"}")
        self.table2.setObjectName("table2")
        self.table2.setColumnCount(5)
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
        self.backbutton = QtWidgets.QPushButton(self.page_2)
        self.backbutton.setGeometry(QtCore.QRect(470, 310, 56, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backbutton.setFont(font)
        self.backbutton.setObjectName("backbutton")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        
        self.logwid = QtWidgets.QWidget(self.page_3)
        self.logwid.setGeometry(QtCore.QRect(90, 60, 351, 221))
        self.logwid.setObjectName("logwid")
        self.label = QtWidgets.QLabel(self.logwid)
        self.label.setGeometry(QtCore.QRect(160, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.logwid)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.logwid)
        self.label_3.setGeometry(QtCore.QRect(100, 80, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.emailbox = QtWidgets.QLineEdit(self.logwid)
        self.emailbox.setGeometry(QtCore.QRect(160, 77, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emailbox.setFont(font)
        self.emailbox.setObjectName("emailbox")
        self.passbox = QtWidgets.QLineEdit(self.logwid)
        self.passbox.setGeometry(QtCore.QRect(160, 117, 113, 20))
        self.passbox.setText("")
        self.passbox.setObjectName("passbox")
        self.pushButton = QtWidgets.QPushButton(self.logwid)
        self.pushButton.setGeometry(QtCore.QRect(150, 160, 56, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainlabel.setText(_translate("MainWindow", "SwiftSynk"))
        item = self.table1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.table1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Path"))
        item = self.table1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Size"))
        self.syncButton.setToolTip(_translate("MainWindow", "Select files to Sync"))
        self.syncButton.setText(_translate("MainWindow", "SYNC\n"
"Files"))
        self.syncButton2.setText(_translate("MainWindow", "SYNC\n"
"Folders"))
        item = self.table2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.table2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Path"))
        item = self.table2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Size"))
        self.backbutton.setText(_translate("MainWindow", "◀ Back"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.label_3.setText(_translate("MainWindow", "Email ID:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
