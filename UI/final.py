from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5 import QtCore

import math, os

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 1082, 62))
        self.widget1.setStyleSheet("")
        self.widget1.setObjectName("widget1")
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(0, 58, 1082, 682))
        self.widget2.setObjectName("widget2")
        self.table = QtWidgets.QTableWidget(self.widget2)
        self.table.setGeometry(QtCore.QRect(-10, 2, 1102, 682))
        self.table.setStyleSheet("QHeaderView::section {\n"
                         "    background-color: rgb(255, 255, 255);\n"
                         "    border: none\n"
                         "}\n"
                         "QTableWidget {\n"
                         "    border: none;\n"
                         "}\n")

        
        self.table.setObjectName("table")
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(5)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 400)
        self.table.setColumnWidth(4, 100)
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
        self.syncButton = QtWidgets.QPushButton(self.widget2)
        self.syncButton.setGeometry(QtCore.QRect(880, 560, 90, 102))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.syncButton.setFont(font)
        self.syncButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.syncButton.setObjectName("syncButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.syncButton2 = QtWidgets.QPushButton(self.widget2)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Path"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Size"))
        self.syncButton.setToolTip(_translate("MainWindow", "Select files to Sync"))
        self.syncButton2.setToolTip(_translate("MainWindow", "Select folder to Sync"))
        self.syncButton.setText(_translate("MainWindow", "SYNC\n"
"Files"))
        self.syncButton2.setText(_translate("MainWindow", "SYNC\n"
"Folder"))





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.syncButton.clicked.connect(self.sync_files)
        self.syncButton2.clicked.connect(self.sync_folders)
        self.table.cellDoubleClicked.connect(self.open_file_explorer)
        self.icon_provider = QtWidgets.QFileIconProvider()

    def sync_folders(self):
        folder_dialog = QtWidgets.QFileDialog(self)
        folder_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        folder_dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        if folder_dialog.exec_():
            selected_folders = folder_dialog.selectedFiles()
            for folder_path in selected_folders:
                if self.is_folder_already_added(folder_path):
                    QtWidgets.QMessageBox.warning(self, "Folder Already Added", "The folder '{}' is already being synced.".format(folder_path))
                else:
                    folder_info = QtCore.QDir(folder_path)
                    # Add folder information to the table
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)
                    
                    # Add folder icon
                    icon_label = QtWidgets.QLabel()
                    icon = self.icon_provider.icon(QtCore.QFileInfo(folder_path))
                    icon_label.setPixmap(icon.pixmap(20, 20))
                    icon_label.setAlignment(QtCore.Qt.AlignCenter)
                    self.table.setCellWidget(row_position, 0, icon_label)
                    
                    # Add folder name
                    item_name = QtWidgets.QTableWidgetItem(folder_info.dirName())
                    item_name.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_name.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 1, item_name)
                    
                    # Add folder status
                    item_status = QtWidgets.QTableWidgetItem("Synced")
                    item_status.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_status.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 2, item_status)
                    
                    # Add folder path
                    item_path = QtWidgets.QTableWidgetItem(folder_path)
                    item_path.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_path.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 3, item_path)
                    
                    # Add folder size (you can adjust this according to your requirement)
                    item_size = QtWidgets.QTableWidgetItem("")
                    item_size.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_size.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 4, item_size)

    def is_folder_already_added(self, folder_path):
        for row in range(self.table.rowCount()):
            existing_path_item = self.table.item(row, 3)  # Path column is column index 3
            if existing_path_item and existing_path_item.text() == folder_path:
                return True
        return False



    def sync_files(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                file_info = QtCore.QFileInfo(file_path)
                file_already_exists = False
                for row in range(self.table.rowCount()):
                    existing_path_item = self.table.item(row, 3)  # Path column is column index 2
                    if existing_path_item and existing_path_item.text() == file_info.absoluteFilePath():
                        file_already_exists = True
                        break
                
                if not file_already_exists:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)
                    
                    icon = self.icon_provider.icon(file_info)
                    icon_label = QtWidgets.QLabel()
                    icon_label.setPixmap(icon.pixmap(20, 20))
                    icon_label.setAlignment(QtCore.Qt.AlignCenter)
                    self.table.setCellWidget(row_position, 0, icon_label)

                    item_name = QtWidgets.QTableWidgetItem(file_info.fileName())
                    item_name.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_name.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 1, item_name)

                    item_status = QtWidgets.QTableWidgetItem("Synced")
                    item_status.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_status.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 2, item_status)

                    item_path = QtWidgets.QTableWidgetItem(file_info.absoluteFilePath())
                    item_path.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_path.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 3, item_path)

                    item_size = QtWidgets.QTableWidgetItem(convert_size(file_info.size()))
                    item_size.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_size.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 4, item_size)

                else:
                    QtWidgets.QMessageBox.warning(self, "File Already Exists", "The file '{}' is already being synced.".format(file_info.fileName()))

    def open_file_explorer(self, row, column):
        if column == 3:  
            file_path = self.table.item(row, column).text()
            if os.path.exists(file_path):
                folder_path = os.path.dirname(file_path)  
                os.startfile(folder_path) 
            else:
                QtWidgets.QMessageBox.warning(self, "File Not Found", "The file does not exist.")

        elif column == 1:
            file_path_item = self.table.item(row, 3)
            file_path = file_path_item.text()
            if os.path.exists(file_path):
                os.startfile(file_path)
            else:
                QtWidgets.QMessageBox.warning(self, "File Not Found", "The file does not exist.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("SwiftSynk")
    window.show()
    sys.exit(app.exec_())