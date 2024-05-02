from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QTableWidget
from PyQt5.QtCore import Qt
from Images import resources

#copy your 'Images' folder path & paste it here with double backslash
# imgpath = "C:\\Projects\\SEM 4\\SwiftSynk_PythonProject\\App\\Images" #Saif
imgpath = r"C:\Users\tupti\OneDrive\Desktop\new Lang\Sem4\SwiftSynk_PythonProject\App\Images" #Narendra

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 740)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 740))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 740))
        MainWindow.setStyleSheet("#widget1{\n"
"    background-color: #DCECE\n"
"}\n"
"#leftmenu, #leftmenu2, #leftmenu3, #leftmenu4{\n"
"    background-color: rgb(56, 68, 101);\n"
"    border-radius: 5\n"
"}\n"
"#lmhome,#lmlog,#lmuser,#lmhome2,#lmlog2,#lmuser2,#lmhome3,#lmlog3,#lmuser3,#lmuser4, #lmhome4, #lmlog4{\n"
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
"#unamebox_su{\n"
"    border-radius: 10;\n"
"    color: rgb(56, 68, 101);\n"
"    background-color: rgb(205, 219, 219)\n"
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
"QLineEdit:focus{\n"
"       border: 2px solid grey;\n"
"}\n"
"QScrollBar:vertical\n"
"    {\n"
"        background-color: #2A2929;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        background-color: #CDDBDB;\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"#userlabel, #folderno, #fileno {\n"
"    color: rgb(56, 68, 101);\n"
"}\n"
"#logout{\n"
"    background-color: rgb(56, 68, 101);\n"
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
        self.table.setColumnCount(12)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 126)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 50)
        self.table.setColumnWidth(4, 210)
        self.table.setColumnWidth(5, 25)
        self.table.setColumnWidth(6, 25)
        self.table.setColumnWidth(7, 25)
        self.table.setColumnWidth(8, 25)
        self.table.setColumnWidth(9, 25)
        self.table.setColumnWidth(10, 25)
        self.table.setColumnWidth(11, 0)
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
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(11, item)
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
        self.lmuser = QtWidgets.QPushButton(self.leftmenu)
        self.lmuser.setGeometry(QtCore.QRect(20, 640, 46, 46))
        self.lmuser.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(imgpath+"\\user-gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lmuser.setIcon(icon3)
        self.lmuser.setIconSize(QtCore.QSize(30, 30))
        self.lmuser.setObjectName("lmuser")
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
        self.textBrowser = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser.setGeometry(QtCore.QRect(120, 140, 942, 582))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(56, 68, 101);\n"
"border-radius: 5")
        self.textBrowser.setObjectName("textBrowser")
        self.userlabel = QtWidgets.QLabel(self.page_3)
        self.userlabel.setGeometry(QtCore.QRect(140, 40, 342, 32))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.userlabel.setFont(font)
        self.userlabel.setObjectName("userlabel")
        self.fileno = QtWidgets.QLabel(self.page_3)
        self.fileno.setGeometry(QtCore.QRect(140, 90, 282, 32))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fileno.setFont(font)
        self.fileno.setObjectName("fileno")
        self.folderno = QtWidgets.QLabel(self.page_3)
        self.folderno.setGeometry(QtCore.QRect(480, 90, 282, 32))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.folderno.setFont(font)
        self.folderno.setObjectName("folderno")
        self.logout = QtWidgets.QPushButton(self.page_3)
        self.logout.setGeometry(QtCore.QRect(980, 40, 62, 62))
        self.logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logout.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(imgpath+"\\power-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon4)
        self.logout.setIconSize(QtCore.QSize(32, 32))
        self.logout.setObjectName("logout")
        self.url = QtWidgets.QLabel(self.page_3)
        self.url.setGeometry(QtCore.QRect(480, 30, 342, 32))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.url.setFont(font)
        self.url.setText("")
        self.url.setObjectName("url")
        self.leftmenu4 = QtWidgets.QWidget(self.page_3)
        self.leftmenu4.setGeometry(QtCore.QRect(20, 20, 82, 700))
        self.leftmenu4.setObjectName("leftmenu4")
        self.lmuser4 = QtWidgets.QPushButton(self.leftmenu4)
        self.lmuser4.setGeometry(QtCore.QRect(20, 640, 46, 46))
        self.lmuser4.setText("")
        self.lmuser4.setIcon(icon3)
        self.lmuser4.setIconSize(QtCore.QSize(30, 30))
        self.lmuser4.setObjectName("lmuser4")
        self.lmhome4 = QtWidgets.QPushButton(self.leftmenu4)
        self.lmhome4.setGeometry(QtCore.QRect(20, 40, 46, 46))
        self.lmhome4.setText("")
        self.lmhome4.setIcon(icon)
        self.lmhome4.setIconSize(QtCore.QSize(30, 30))
        self.lmhome4.setObjectName("lmhome4")
        self.lmlog4 = QtWidgets.QPushButton(self.leftmenu4)
        self.lmlog4.setGeometry(QtCore.QRect(20, 110, 46, 46))
        self.lmlog4.setText("")
        self.lmlog4.setIcon(icon1)
        self.lmlog4.setIconSize(QtCore.QSize(30, 30))
        self.lmlog4.setObjectName("lmlog4")
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
        self.label_7.setGeometry(QtCore.QRect(180, 170, 362, 70))
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
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bahnschrift\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#cddbdb;\">User Guide [ </span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\">ℹ ]</span><span style=\" font-size:12pt; color:#cddbdb;\">: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#cddbdb;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\"> </span><img src=\":/newPrefix/book-alt.png\" width=\"30\" height=\"30\" /><span style=\" font-size:12pt; color:#cddbdb;\">  Log Files</span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\"> - Contains all the synced/unsynced files/folders along with the user logs. Log files can be cleared using the delete button present beneath the table.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400; color:#cddbdb;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/pause.png\" width=\"30\" height=\"30\" /><span style=\" font-size:12pt; color:#cddbdb;\">  Pause Sync</span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\"> - This button pauses the sync of that file/folder and stops reflecting the changes made on your local device onto the drive. After a file/folder\'s sync is paused, the button can be pressed again to restart the sync. The status of the file would display if the file/folder sync is paused or not.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400; color:#cddbdb;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/remove.png\" width=\"30\" height=\"30\" /><span style=\" font-size:12pt; color:#cddbdb;\">  Stop Sync</span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\"> - This button stops the syncing and also deletes the file from the drive. If clicked while a file is in 2-state then both the previous file and the current file would be deleted from the drive.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400; color:#cddbdb;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/2stateinit.png\" width=\"30\" height=\"30\" /><span style=\" font-size:12pt; color:#cddbdb;\">  Initiate 2-state</span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\"> - This button initiates 2-state for the file. Once initiated, the current state of the file is saved on a secondary folder on the drive, this file acts a savepoint. In the main folder, the file\'s sync goes on continuously. Due to any problem/needs the previous saved file(savepoint) can be restored.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400; color:#cddbdb;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/clock1.png\" width=\"30\" height=\"30\" /><span style=\" font-size:12pt; color:#cddbdb;\">  Delete current, retain previous</span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\"> - This button appears for the 2-state initiated files. It deletes the current syncing file from the main folder of drive and brings in the previously saved file(savepoint) from the secondary folder onto the main folder and starts syncing this newly brought file. It can be used to go back to the previous savepoint. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400; text-decoration: underline; color:#cddbdb;\">Note:</span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\"> This stops the 2-state for the file and initiates normal sync for this newly brought file.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400; color:#cddbdb;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/clock2.png\" width=\"30\" height=\"30\" /><span style=\" font-size:12pt; color:#cddbdb;\">  Delete previous, retain current</span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\"> - This button appears for the 2-state initiated files. It deletes the previously saved file(savepoint) from the main folder of drive and keeps the currently syncing file only in the main folder and continues it\'s sync normally. It can be used to delete the previous savepoint. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400; text-decoration: underline; color:#cddbdb;\">Note:</span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\"> This stops the 2-state for the file and continues normal sync of the current file.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400; color:#cddbdb;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/exchange.png\" width=\"30\" height=\"30\" /><span style=\" font-size:12pt; color:#cddbdb;\">  Change previous and current 2-state files(Step process) - </span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\">For 2-state files. It changes the previously saved file(savepoint) with the current file and saves it in the secondary folder making a new savepoint and starts syncing the changes in this file in the primary folder. This can be used to make a new savepoint and remove the previous savepoint. The 2-state syncing continues for this file.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400; color:#cddbdb;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/download.png\" width=\"30\" height=\"30\" /><span style=\" font-size:12pt; color:#cddbdb;\">  Download savepoint file - </span><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\">For 2-state files. It can be used to download the previous </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400; color:#cddbdb;\">state(savepoint) of the file if required and continuing the 2-state sync normally.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400; color:#cddbdb;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400; color:#cddbdb;\"><br /></p></body></html>"))
        self.userlabel.setText(_translate("MainWindow", "Username"))
        self.fileno.setText(_translate("MainWindow", "Total Files Synced: "))
        self.folderno.setText(_translate("MainWindow", "Total Folders Synced: "))
        self.logout.setToolTip(_translate("MainWindow", "Delete Account"))
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
