

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 740)
        MainWindow.setStyleSheet("#widget1{\n"
"    background-color: rgb(106, 90, 205)\n"
"}\n"
"\n"
"#table{\n"
"    background-color: rgb(194, 194, 255);\n"
"    border-width: 0px;\n"
"    gridline-color: rgb(194, 194, 255)\n"
"}\n"
"\n"
"#table2{\n"
"    background-color: rgb(194, 194, 255);\n"
"    border-width: 0px;\n"
"    gridline-color: rgb(194, 194, 255)\n"
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
"#backbutton{\n"
"    background-color: rgb(106, 90, 205);\n"
"    border-radius: 5;\n"
"    border: none;\n"
"    color: white\n"
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
"#signupswitch{\n"
"    background-color: transparent\n"
"}\n"
"\n"
"#signupwid{\n"
"    background-color: rgb(205, 208, 255);\n"
"    border-radius: 25;\n"
"    drop-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);\n"
"}\n"
"#signupbutton{\n"
"    color: white;\n"
"    background-color: rgb(106, 90, 205);\n"
"    border: none;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"#emailbox_su{\n"
"    border-radius: 5\n"
"}\n"
"#passbox_su{\n"
"    border-radius: 5\n"
"}\n"
"#unamebox_su{\n"
"    border-radius: 5\n"
"}\n"
"#loginswitch{\n"
"    background-color: transparent\n"
"}\n"
"\n"
"#wc_widget{\n"
"    background-color: rgb(205, 208, 255);\n"
"    border-radius: 25;\n"
"    drop-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);\n"
"}\n"
"#gdrivebutton{\n"
"    background-color: white;\n"
"    border-radius: 15\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 1082, 62))
        self.widget1.setStyleSheet("")
        self.widget1.setObjectName("widget1")
        self.mainlabel = QtWidgets.QLabel(self.widget1)
        self.mainlabel.setGeometry(QtCore.QRect(14, 10, 162, 42))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.mainlabel.setFont(font)
        self.mainlabel.setObjectName("mainlabel")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 58, 1082, 682))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.table = QtWidgets.QTableWidget(self.page)
        self.table.setGeometry(QtCore.QRect(0, 0, 1082, 682))
        self.table.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: none\n"
"}")
        self.table.setObjectName("table")
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(7)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 400)
        self.table.setColumnWidth(4, 100)
        self.table.setColumnWidth(5, 25)
        self.table.setColumnWidth(6, 25)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        self.syncButton = QtWidgets.QPushButton(self.page)
        self.syncButton.setGeometry(QtCore.QRect(880, 560, 90, 102))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.syncButton.setFont(font)
        self.syncButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.syncButton.setObjectName("syncButton")
        self.syncButton2 = QtWidgets.QPushButton(self.page)
        self.syncButton2.setGeometry(QtCore.QRect(972, 560, 90, 102))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.syncButton2.setFont(font)
        self.syncButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.syncButton2.setStyleSheet("#syncButton2{\n"
"    text : SYNC \\n Folder\n"
"}")
        self.syncButton2.setObjectName("syncButton2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.table2 = QtWidgets.QTableWidget(self.page_2)
        self.table2.setGeometry(QtCore.QRect(0, 0, 1082, 682))
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
        self.table2.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(5, item)
        self.backbutton = QtWidgets.QPushButton(self.page_2)
        self.backbutton.setGeometry(QtCore.QRect(920, 620, 112, 42))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backbutton.setFont(font)
        self.backbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backbutton.setObjectName("backbutton")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        
        self.logwid = QtWidgets.QWidget(self.page_3)
        self.logwid.setGeometry(QtCore.QRect(180, 120, 702, 442))
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(0, 0)
        effect.setBlurRadius(30)
        self.logwid.setGraphicsEffect(effect)
        self.logwid.setObjectName("logwid")
        self.label = QtWidgets.QLabel(self.logwid)
        self.label.setGeometry(QtCore.QRect(310, 40, 102, 62))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.logwid)
        self.label_2.setGeometry(QtCore.QRect(180, 216, 102, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.logwid)
        self.label_3.setGeometry(QtCore.QRect(180, 136, 102, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.emailbox = QtWidgets.QLineEdit(self.logwid)
        self.emailbox.setGeometry(QtCore.QRect(320, 134, 226, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emailbox.setFont(font)
        self.emailbox.setObjectName("emailbox")
        self.passbox = QtWidgets.QLineEdit(self.logwid)
        self.passbox.setGeometry(QtCore.QRect(320, 214, 226, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.passbox.setFont(font)
        self.passbox.setText("")
        self.passbox.setObjectName("passbox")
        self.passbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbutton = QtWidgets.QPushButton(self.logwid)
        self.loginbutton.setGeometry(QtCore.QRect(290, 300, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.loginbutton.setFont(font)
        self.loginbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginbutton.setObjectName("loginbutton")
        self.label_4 = QtWidgets.QLabel(self.logwid)
        self.label_4.setGeometry(QtCore.QRect(290, 380, 102, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.signupswitch = QtWidgets.QPushButton(self.logwid)
        self.signupswitch.setGeometry(QtCore.QRect(366, 374, 62, 42))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.signupswitch.setFont(font)
        self.signupswitch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupswitch.setObjectName("signupswitch")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.signupwid = QtWidgets.QWidget(self.page_4)
        self.signupwid.setGeometry(QtCore.QRect(180, 80, 702, 522))
        self.signupwid.setObjectName("signupwid")
        self.label_5 = QtWidgets.QLabel(self.signupwid)
        self.label_5.setGeometry(QtCore.QRect(300, 20, 122, 62))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.signupwid)
        self.label_6.setGeometry(QtCore.QRect(180, 282, 102, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.signupwid)
        self.label_7.setGeometry(QtCore.QRect(180, 202, 102, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.unamebox_su = QtWidgets.QLineEdit(self.signupwid)
        self.unamebox_su.setGeometry(QtCore.QRect(320, 200, 226, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.unamebox_su.setFont(font)
        self.unamebox_su.setObjectName("unamebox_su")
        self.passbox_su = QtWidgets.QLineEdit(self.signupwid)
        self.passbox_su.setGeometry(QtCore.QRect(320, 280, 226, 40))
        self.passbox_su.setText("")
        self.passbox_su.setObjectName("passbox_su")
        self.signupbutton = QtWidgets.QPushButton(self.signupwid)
        self.signupbutton.setGeometry(QtCore.QRect(290, 364, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.signupbutton.setFont(font)
        self.signupbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupbutton.setObjectName("signupbutton")
        self.label_8 = QtWidgets.QLabel(self.signupwid)
        self.label_8.setGeometry(QtCore.QRect(270, 440, 142, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.loginswitch = QtWidgets.QPushButton(self.signupwid)
        self.loginswitch.setGeometry(QtCore.QRect(390, 434, 62, 42))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.loginswitch.setFont(font)
        self.loginswitch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginswitch.setObjectName("loginswitch")
        self.email_label = QtWidgets.QLabel(self.signupwid)
        self.email_label.setGeometry(QtCore.QRect(280, 110, 262, 42))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("border: 2px solid rgb(166, 166, 166);\n"
"border-radius: 10px;\n"
"padding: 3px;\n"
"")
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.wc_widget = QtWidgets.QWidget(self.page_5)
        self.wc_widget.setGeometry(QtCore.QRect(180, 80, 742, 522))
        self.wc_widget.setObjectName("wc_widget")
        self.label_9 = QtWidgets.QLabel(self.wc_widget)
        self.label_9.setGeometry(QtCore.QRect(200, 60, 322, 42))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.wc_widget)
        self.label_10.setGeometry(QtCore.QRect(160, 140, 422, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gdrivebutton = QtWidgets.QPushButton(self.wc_widget)
        self.gdrivebutton.setGeometry(QtCore.QRect(280, 220, 182, 182))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gdrivebutton.setFont(font)
        self.gdrivebutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Projects\\SEM 4\\SwiftSynk_PythonProject\\App\\Images\\google_drive_PNG6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gdrivebutton.setIcon(icon)
        self.gdrivebutton.setIconSize(QtCore.QSize(100, 100))
        self.gdrivebutton.setObjectName("gdrivebutton")
        self.label_11 = QtWidgets.QLabel(self.wc_widget)
        self.label_11.setGeometry(QtCore.QRect(312, 420, 122, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainlabel.setText(_translate("MainWindow", "SwiftSynk"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Path"))
        item = self.table.horizontalHeaderItem(4)
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
        self.backbutton.setToolTip(_translate("MainWindow", "Go Back to Files"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.label_3.setText(_translate("MainWindow", "Username:"))
        self.loginbutton.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "New Account? "))
        self.signupswitch.setToolTip(_translate("MainWindow", "<html><head/><body><p>Sign Up</p></body></html>"))
        self.signupswitch.setText(_translate("MainWindow", "Sign Up!"))
        self.label_5.setText(_translate("MainWindow", "Sign Up"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.label_7.setText(_translate("MainWindow", "Username:"))
        self.unamebox_su.setToolTip(_translate("MainWindow", "Enter a desired username"))
        self.signupbutton.setText(_translate("MainWindow", "Sign Up"))
        self.label_8.setText(_translate("MainWindow", "Already registered? "))
        self.loginswitch.setToolTip(_translate("MainWindow", "Log in with an existing account"))
        self.loginswitch.setText(_translate("MainWindow", "Log in!"))
        self.email_label.setText(_translate("MainWindow", "Email"))
        self.label_9.setText(_translate("MainWindow", "Welcome to SwiftSynk"))
        self.label_10.setText(_translate("MainWindow", "Power of Google Drive straight from your desktop!"))
        self.label_11.setText(_translate("MainWindow", "Add Google Drive"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
