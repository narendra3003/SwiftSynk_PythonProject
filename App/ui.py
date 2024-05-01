from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QTableWidget
from PyQt5.QtCore import Qt

#copy your 'Images' folder path & paste it here with double backslash
imgpath = "C:\\Projects\\SEM 4\\SwiftSynk_PythonProject\\App\\Images" #Saif
# imgpath = r"C:\Users\tupti\OneDrive\Desktop\new Lang\Sem4\SwiftSynk_PythonProject\App\Images" #Narendra


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 740)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 740))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 740))
        MainWindow.setStyleSheet("#widget1{\n"
"    background-color: #DCECE\n"
"}\n"
"#leftmenu, #leftmenu2, #leftmenu3{\n"
"    background-color: rgb(56, 68, 101);\n"
"    border-radius: 5\n"
"}\n"
"#lmhome,#lmlog,#lmuser,#lmfav,#lmhome2,#lmlog2,#lmuser2,#lmfav2,#lmhome3,#lmlog3,#lmuser3,#lmfav3{\n"
"    background-color:transparent\n"
"}\n"
"#table, #table2, #logtable{\n"
"    background-color: rgb(56, 68, 101);\n"
"    border-radius: 5;\n"
"    gridline-color: rgb(56, 68, 101);\n"
"    color: rgb(205, 219, 219)\n"
"}\n"
"\n"
"#syncButton{\n"
"    background-color: rgb(205, 219, 219);\n"
"    border-top-left-radius: 12;\n"
"    border-bottom-left-radius: 12;\n"
"    color: rgb(56, 68, 101);\n"
"}\n"
"\n"
"#syncButton2{\n"
"    background-color: rgb(205, 219, 219);\n"
"    border-top-right-radius: 12;\n"
"    border-bottom-right-radius: 12;\n"
"    color: rgb(56, 68, 101);\n"
"    border-left-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"#mainlabel{\n"
"    color: white\n"
"}\n"
"\n"
"#logwid{\n"
"    background-color: rgb(56, 68, 101);\n"
"    border-radius: 25;\n"
"    drop-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);\n"
"    color: rgb(205, 219, 219)\n"
"}\n"
"#loginbutton{\n"
"    color: rgb(56, 68, 101);\n"
"    background-color: rgb(205, 219, 219);\n"
"    border: none;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"#emailbox,#passbox,#emailbox_su,#passbox_su,#unamebox_su{\n"
"    border-radius: 5;\n"
"    color: rgb(56, 68, 101)"
"}\n"
"#signupswitch{\n"
"    background-color: transparent\n"
"}\n"
"\n"
"#signupwid{\n"
"    background-color: rgb(56, 68, 101);\n"
"    border-radius: 25;\n"
"    drop-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);\n"
"}\n"
"#signupbutton{\n"
"    color: rgb(56, 68, 101);\n"
"    background-color: rgb(205, 219, 219);\n"
"    border: none;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"#loginswitch{\n"
"    background-color: transparent\n"
"}\n"
"\n"
"#wc_widget{\n"
"    background-color: rgb(56, 68, 101);\n"
"    border-radius: 25;\n"
"    drop-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);\n"
"}\n"
"#gdrivebutton{\n"
"    background-color: rgb(205, 219, 219);\n"
"    border-radius: 15\n"
"}\n"
"#searchtab1,#searchtab2{\n"
"    background-color: rgb(205, 219, 219);\n"
"    border: none;\n"
"    border-radius: 5\n"
"}\n"
"#backbutton, #closebut, #closebut2, #closebut3, #refresh_but, #dellog_but{\n"
"    background-color: rgb(205, 219, 219);\n"
"    border-radius: 5;\n"
"    border: none;\n"
"    color: rgb(56, 68, 101)\n"
"}\n"
"#user_wid, #user_wid2, #user_wid3{\n"
"    background-color: rgb(205, 219, 219);\n"
"    border-radius: 5\n"
"}\n"
"")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1082, 742))
        self.stackedWidget.setGraphicsEffect(shadow)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.table = QtWidgets.QTableWidget(self.page)
        self.table.setGeometry(QtCore.QRect(140, 98, 900, 622))
        self.table.setStyleSheet("::section {\n"
"    background-color: rgb(205, 219, 219);\n"
"    border: none;\n"
"    color: rgb(56, 68, 101)\n"
"}\n"
"::section:first{\n"
"    border-top-left-radius: 5\n"
"}\n"
"::section:last{\n"
"    border-top-right-radius: 5\n"
"}")
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.NoSelection)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setObjectName("table")
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(11)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 126)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 50)
        self.table.setColumnWidth(4, 268)
        self.table.setColumnWidth(5, 25)
        self.table.setColumnWidth(6, 25)
        self.table.setColumnWidth(7, 25)
        self.table.setColumnWidth(8, 25)
        self.table.setColumnWidth(9, 25)
        self.table.setColumnWidth(10, 0)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, item)
        self.syncButton = QtWidgets.QPushButton(self.page)
        self.syncButton.setGeometry(QtCore.QRect(864, 620, 82, 82))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.syncButton.setFont(font)
        self.syncButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.syncButton.setObjectName("syncButton")
        self.syncButton2 = QtWidgets.QPushButton(self.page)
        self.syncButton2.setGeometry(QtCore.QRect(947, 620, 82, 82))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.syncButton2.setFont(font)
        self.syncButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.syncButton2.setStyleSheet("#syncButton2{\n"
"    text : SYNC \\n Folder\n"
"}")
        self.syncButton2.setObjectName("syncButton2")
        self.leftmenu = QtWidgets.QWidget(self.page)
        self.leftmenu.setGeometry(QtCore.QRect(20, 20, 82, 700))
        self.leftmenu.setObjectName("leftmenu")
        self.lmhome = QtWidgets.QPushButton(self.leftmenu)
        self.lmhome.setGeometry(QtCore.QRect(20, 40, 46, 46))
        self.lmhome.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imgpath+"\\home2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lmhome.setIcon(icon)
        self.lmhome.setIconSize(QtCore.QSize(30, 30))
        self.lmhome.setObjectName("lmhome")
        self.lmlog = QtWidgets.QPushButton(self.leftmenu)
        self.lmlog.setGeometry(QtCore.QRect(20, 110, 46, 46))
        self.lmlog.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(imgpath+"\\book-alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lmlog.setIcon(icon1)
        self.lmlog.setIconSize(QtCore.QSize(30, 30))
        self.lmlog.setObjectName("lmlog")
        self.lmfav = QtWidgets.QPushButton(self.leftmenu)
        self.lmfav.setGeometry(QtCore.QRect(20, 180, 46, 46))
        self.lmfav.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(imgpath+"\\starr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lmfav.setIcon(icon2)
        self.lmfav.setIconSize(QtCore.QSize(30, 30))
        self.lmfav.setObjectName("lmfav")
        self.lmuser = QtWidgets.QPushButton(self.leftmenu)
        self.lmuser.setGeometry(QtCore.QRect(20, 640, 46, 46))
        self.lmuser.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(imgpath+"\\user-gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lmuser.setIcon(icon3)
        self.lmuser.setIconSize(QtCore.QSize(30, 30))
        self.lmuser.setObjectName("lmuser")
        self.searchtab1 = QtWidgets.QLineEdit(self.page)
        self.searchtab1.setGeometry(QtCore.QRect(798, 40, 242, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setBold(True)
        font.setWeight(75)
        self.searchtab1.setFont(font)
        self.searchtab1.setInputMask("")
        self.searchtab1.setText("")
        self.searchtab1.setObjectName("searchtab1")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(160, 20, 222, 62))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(56, 68, 101)")
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.table2 = QtWidgets.QTableWidget(self.page_2)
        self.table2.setGeometry(QtCore.QRect(140, 98, 900, 622))
        self.table2.setStyleSheet("::section {\n"
"    background-color: rgb(205, 219, 219);\n"
"    border: none;\n"
"    color: rgb(56, 68, 101)\n"
"}\n"
"::section:first{\n"
"    border-top-left-radius: 5\n"
"}\n"
"::section:last{\n"
"    border-top-right-radius: 5\n"
"}")
        self.table2.setSelectionBehavior(QTableWidget.SelectRows)
        self.table2.setSelectionMode(QTableWidget.NoSelection)
        self.table2.setFocusPolicy(Qt.NoFocus)
        self.table2.setObjectName("table2")
        self.table2.verticalHeader().setVisible(False)
        self.table2.setColumnCount(6)
        self.table2.setColumnWidth(0, 50)
        self.table2.setColumnWidth(1, 126)
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
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(5, item)
        self.backbutton = QtWidgets.QPushButton(self.page_2)
        self.backbutton.setGeometry(QtCore.QRect(928, 40, 112, 42))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.backbutton.setFont(font)
        self.backbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backbutton.setObjectName("backbutton")
        self.backbutton.raise_()
        self.leftmenu2 = QtWidgets.QWidget(self.page_2)
        self.leftmenu2.setGeometry(QtCore.QRect(20, 20, 82, 700))
        self.leftmenu2.setObjectName("leftmenu2")
        self.lmuser2 = QtWidgets.QPushButton(self.leftmenu2)
        self.lmuser2.setGeometry(QtCore.QRect(20, 640, 46, 46))
        self.lmuser2.setText("")
        self.lmuser2.setIcon(icon3)
        self.lmuser2.setIconSize(QtCore.QSize(30, 30))
        self.lmuser2.setObjectName("lmuser2")
        self.lmhome2 = QtWidgets.QPushButton(self.leftmenu2)
        self.lmhome2.setGeometry(QtCore.QRect(20, 40, 46, 46))
        self.lmhome2.setText("")
        self.lmhome2.setIcon(icon)
        self.lmhome2.setIconSize(QtCore.QSize(30, 30))
        self.lmhome2.setObjectName("lmhome2")
        self.lmlog2 = QtWidgets.QPushButton(self.leftmenu2)
        self.lmlog2.setGeometry(QtCore.QRect(20, 110, 46, 46))
        self.lmlog2.setText("")
        self.lmlog2.setIcon(icon1)
        self.lmlog2.setIconSize(QtCore.QSize(30, 30))
        self.lmlog2.setObjectName("lmlog2")
        self.lmfav2 = QtWidgets.QPushButton(self.leftmenu2)
        self.lmfav2.setGeometry(QtCore.QRect(20, 180, 46, 46))
        self.lmfav2.setText("")
        self.lmfav2.setIcon(icon2)
        self.lmfav2.setIconSize(QtCore.QSize(30, 30))
        self.lmfav2.setObjectName("lmfav2")
        self.pathlabel = QtWidgets.QLabel(self.page_2)
        self.pathlabel.setGeometry(QtCore.QRect(160, 20, 522, 62))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pathlabel.setFont(font)
        self.pathlabel.setStyleSheet("color: rgb(56, 68, 101)")
        self.pathlabel.setObjectName("pathlabel")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.signupwid = QtWidgets.QWidget(self.page_4)
        self.signupwid.setGeometry(QtCore.QRect(200, 100, 702, 522))
        self.signupwid.setStyleSheet("color: rgb(205, 219, 219)")
        self.signupwid.setObjectName("signupwid")
        self.label_5 = QtWidgets.QLabel(self.signupwid)
        self.label_5.setGeometry(QtCore.QRect(200, 60, 322, 62))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.signupwid)
        self.label_7.setGeometry(QtCore.QRect(180, 170, 362, 7))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.unamebox_su = QtWidgets.QLineEdit(self.signupwid)
        self.unamebox_su.setStyleSheet("color: rgb(56,68,101)")
        self.unamebox_su.setGeometry(QtCore.QRect(250, 290, 226, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.unamebox_su.setFont(font)
        self.unamebox_su.setObjectName("unamebox_su")
        self.signupbutton = QtWidgets.QPushButton(self.signupwid)
        self.signupbutton.setGeometry(QtCore.QRect(292, 390, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signupbutton.setFont(font)
        self.signupbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupbutton.setStyleSheet("color: rgb(56, 68, 101)")
        self.signupbutton.setObjectName("signupbutton")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.wc_widget = QtWidgets.QWidget(self.page_5)
        self.wc_widget.setGeometry(QtCore.QRect(180, 100, 742, 522))
        self.wc_widget.setStyleSheet("color: rgb(205, 219, 219)")
        self.wc_widget.setObjectName("wc_widget")
        self.label_9 = QtWidgets.QLabel(self.wc_widget)
        self.label_9.setGeometry(QtCore.QRect(180, 60, 402, 62))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.wc_widget)
        self.label_10.setGeometry(QtCore.QRect(146, 146, 470, 32))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gdrivebutton = QtWidgets.QPushButton(self.wc_widget)
        self.gdrivebutton.setGeometry(QtCore.QRect(290, 220, 182, 182))
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gdrivebutton.setFont(font)
        self.gdrivebutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imgpath+"\\google-drive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gdrivebutton.setIcon(icon)
        self.gdrivebutton.setIconSize(QtCore.QSize(100, 100))
        self.gdrivebutton.setObjectName("gdrivebutton")
        self.label_11 = QtWidgets.QLabel(self.wc_widget)
        self.label_11.setGeometry(QtCore.QRect(314, 420, 142, 32))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.leftmenu3 = QtWidgets.QWidget(self.page_6)
        self.leftmenu3.setGeometry(QtCore.QRect(20, 20, 82, 700))
        self.leftmenu3.setObjectName("leftmenu3")
        self.lmuser3 = QtWidgets.QPushButton(self.leftmenu3)
        self.lmuser3.setGeometry(QtCore.QRect(20, 640, 46, 46))
        self.lmuser3.setText("")
        self.lmuser3.setIcon(icon3)
        self.lmuser3.setIconSize(QtCore.QSize(30, 30))
        self.lmuser3.setObjectName("lmuser3")
        self.lmhome3 = QtWidgets.QPushButton(self.leftmenu3)
        self.lmhome3.setGeometry(QtCore.QRect(20, 40, 46, 46))
        self.lmhome3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imgpath+"\\home2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lmhome3.setIcon(icon)
        self.lmhome3.setIconSize(QtCore.QSize(30, 30))
        self.lmhome3.setObjectName("lmhome3")
        self.lmlog3 = QtWidgets.QPushButton(self.leftmenu3)
        self.lmlog3.setGeometry(QtCore.QRect(20, 110, 46, 46))
        self.lmlog3.setText("")
        self.lmlog3.setIcon(icon1)
        self.lmlog3.setIconSize(QtCore.QSize(30, 30))
        self.lmlog3.setObjectName("lmlog3")
        self.lmfav3 = QtWidgets.QPushButton(self.leftmenu3)
        self.lmfav3.setGeometry(QtCore.QRect(20, 180, 46, 46))
        self.lmfav3.setText("")
        self.lmfav3.setIcon(icon2)
        self.lmfav3.setIconSize(QtCore.QSize(30, 30))
        self.lmfav3.setObjectName("lmfav3")
        self.logtable = QtWidgets.QTableWidget(self.page_6)
        self.logtable.setGeometry(QtCore.QRect(140, 98, 900, 622))
        self.logtable.setStyleSheet("::section {\n"
"    background-color: rgb(205, 219, 219);\n"
"    border: none;\n"
"    color:rgb(56, 68, 101)\n"
"}\n"
"::section:first{\n"
"    border-top-left-radius: 5\n"
"}\n"
"::section:last{\n"
"    border-top-right-radius: 5\n"
"}")
        self.logtable.setSelectionBehavior(QTableWidget.SelectRows)
        self.logtable.setSelectionMode(QTableWidget.NoSelection)
        self.logtable.setFocusPolicy(Qt.NoFocus)
        self.logtable.setObjectName("logtable")
        self.logtable.verticalHeader().setVisible(False)
        self.logtable.setColumnCount(2)
        self.logtable.setColumnWidth(0, 200)
        self.logtable.setColumnWidth(1, 700)
        self.logtable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.logtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.logtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.logtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.logtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.logtable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.logtable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.logtable.setHorizontalHeaderItem(5, item)
        self.label_14 = QtWidgets.QLabel(self.page_6)
        self.label_14.setGeometry(QtCore.QRect(160, 20, 222, 62))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(56, 68, 101)")
        self.label_14.setObjectName("label_14")
        self.searchtab2 = QtWidgets.QLineEdit(self.page_6)
        self.searchtab2.setGeometry(QtCore.QRect(798, 40, 242, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setBold(True)
        font.setWeight(75)
        self.searchtab2.setFont(font)
        self.searchtab2.setInputMask("")
        self.searchtab2.setText("")
        self.searchtab2.setObjectName("searchtab2")
        self.refresh_but = QtWidgets.QPushButton(self.page_6)
        self.refresh_but.setGeometry(QtCore.QRect(700, 40, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.refresh_but.setFont(font)
        self.refresh_but.setObjectName("refresh_but")
        self.dellog_but = QtWidgets.QPushButton(self.page_6)
        self.dellog_but.setGeometry(QtCore.QRect(900, 640, 122, 64))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dellog_but.setFont(font)
        self.dellog_but.setObjectName("dellog_but")
        self.stackedWidget.addWidget(self.page_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        # item = self.table.horizontalHeaderItem(3)
        # item.setText(_translate("MainWindow", "Path"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Size"))
        self.syncButton.setToolTip(_translate("MainWindow", "Select files to Sync"))
        self.syncButton.setText(_translate("MainWindow", "SYNC\n"
"Files"))
        self.syncButton2.setText(_translate("MainWindow", "SYNC\n"
"Folders"))
        self.label_12.setText(_translate("MainWindow", "Synced items"))
        item = self.table2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        # item = self.table2.horizontalHeaderItem(3)
        # item.setText(_translate("MainWindow", "Path"))
        item = self.table2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Size"))
        self.backbutton.setText(_translate("MainWindow", "◀ Back"))
        self.pathlabel.setText(_translate("MainWindow", "Folder"))
        self.backbutton.setToolTip(_translate("MainWindow", "Go Back to Files"))
        self.label_5.setText(_translate("MainWindow", "Start Syncing🔁"))
        self.label_7.setText(_translate("MainWindow", "Connect with your digital identity!\n"
"     Enter any desired username"))
        self.unamebox_su.setToolTip(_translate("MainWindow", "Enter a username"))
        self.signupbutton.setText(_translate("MainWindow", "Go"))
        self.label_9.setText(_translate("MainWindow", "Welcome to SwiftSynk📂"))
        self.label_10.setText(_translate("MainWindow", "Power of Google Drive straight from your desktop!"))
        self.label_11.setText(_translate("MainWindow", "Add Google Drive"))
        item = self.logtable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Type"))
        item = self.logtable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        self.label_14.setText(_translate("MainWindow", "Log Records"))
        self.refresh_but.setText(_translate("MainWindow", "Refresh"))
        self.dellog_but.setText(_translate("MainWindow", "Delete\n"
"Log Records"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
