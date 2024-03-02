import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from main import Ui_MainWindow
import math, os
import connector



def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.syncButton.clicked.connect(self.sync_files)
        self.syncButton2.clicked.connect(self.sync_folders)
        self.table.cellDoubleClicked.connect(self.open_item_explorer)
        self.table2.cellDoubleClicked.connect(self.open_item_explorer)
        self.icon_provider = QtWidgets.QFileIconProvider()
        self.backbutton.clicked.connect(self.go_to_page)
        self.loginbutton.clicked.connect(self.login)
        self.stackedWidget.setCurrentWidget(self.page_3)

    def login(self):
        email = self.emailbox.text()
        password = self.passbox.text()
        print(email, password)

        if(connector.dbm.checkLogin(email, password)==0):
            self.stackedWidget.setCurrentIndex(0)
        elif(connector.dbm.checkLogin(email, password)==1):
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Incorrect Email")
        elif(connector.dbm.checkLogin(email, password)==2):
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Incorrect Password")
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Error")

    def go_to_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def populate_folder_table(self, folder_path):
        files = os.listdir(folder_path)
        self.table2.setRowCount(0) 
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            file_info = QtCore.QFileInfo(file_path)
            row_position = self.table2.rowCount()
            self.table2.insertRow(row_position)

            icon = self.icon_provider.icon(file_info)
            icon_label = QtWidgets.QLabel()
            icon_label.setPixmap(icon.pixmap(20, 20))
            icon_label.setAlignment(QtCore.Qt.AlignCenter)
            self.table2.setCellWidget(row_position, 0, icon_label)

            item_name = QtWidgets.QTableWidgetItem(file_info.fileName())
            item_name.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
            item_name.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table2.setItem(row_position, 1, item_name)

            item_status = QtWidgets.QTableWidgetItem("Synced")
            item_status.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
            item_status.setForeground(QtGui.QColor('green'))
            item_status.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table2.setItem(row_position, 2, item_status)

            item_path = QtWidgets.QTableWidgetItem(file_info.absoluteFilePath())
            item_path.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
            item_path.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table2.setItem(row_position, 3, item_path)

            item_size = QtWidgets.QTableWidgetItem(convert_size(file_info.size()))
            item_size.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
            item_size.setTextAlignment(QtCore.Qt.AlignCenter)
            if os.path.isdir(file_path):
                item_size.setText("")
            else:
                item_size.setText(convert_size(file_info.size()))
            self.table2.setItem(row_position, 4, item_size)

    def sync_folders(self):
        folder_dialog = QtWidgets.QFileDialog(self)
        folder_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        folder_dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        if folder_dialog.exec_():
            selected_folders = folder_dialog.selectedFiles()
            self.show_folders_on_table(selected_folders)

    def show_folders_on_table(self, selected_folders):
        for folder_path in selected_folders:
                if self.is_folder_already_added(folder_path):
                    QtWidgets.QMessageBox.warning(self, "Folder Already Added", "The folder '{}' is already being synced.".format(folder_path))
                else:
                    print("bye", folder_path)
                    connector.upload_folder_to_drive(folder_path)
                    folder_info = QtCore.QDir(folder_path)
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
                    item_status.setForeground(QtGui.QColor('green'))
                    item_status.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_status.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 2, item_status)
                    
                    # Add folder path
                    item_path = QtWidgets.QTableWidgetItem(folder_path)
                    item_path.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_path.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 3, item_path)
                    
                    # Add folder size
                    item_size = QtWidgets.QTableWidgetItem("▶")
                    item_size.setFont(QtGui.QFont("Agency FB", 15, QtGui.QFont.Bold))
                    item_size.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 4, item_size)

                    item_del = QtWidgets.QTableWidgetItem("Delete")
                    item_del.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_del.setForeground(QtGui.QColor('red'))
                    item_del.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 5, item_del)




    def is_folder_already_added(self, folder_path):
        for row in range(self.table.rowCount()):
            existing_path_item = self.table.item(row, 3)
            if existing_path_item and existing_path_item.text() == folder_path:
                return True
        return False

    def sync_files(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            self.show_files_on_table(selected_files)

    def show_files_on_table(self, selected_files):
        for file_path in selected_files:
                file_info = QtCore.QFileInfo(file_path)
                file_already_exists = False
                for row in range(self.table.rowCount()):
                    existing_path_item = self.table.item(row, 3)
                    if existing_path_item and existing_path_item.text() == file_info.absoluteFilePath():
                        file_already_exists = True
                        break
                
                if not file_already_exists:
                    print("bye")
                    connector.upload_file_to_drive(file_path)
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
                    item_status.setForeground(QtGui.QColor('green'))
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

                    item_del = QtWidgets.QTableWidgetItem("Delete")
                    item_del.setFont(QtGui.QFont("Agency FB", 10, QtGui.QFont.Bold))
                    item_del.setForeground(QtGui.QColor('red'))
                    item_del.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_position, 5, item_del)

                else:
                    QtWidgets.QMessageBox.warning(self, "File Already Exists", "The file '{}' is already being synced.".format(file_info.fileName()))

    def open_item_explorer(self, row, column):
        if column == 3:  
            file_path = self.table.item(row, column).text() if self.sender() == self.table else self.table2.item(row, column).text()
            if os.path.exists(file_path):
                folder_path = os.path.dirname(file_path)  
                os.startfile(folder_path) 
            else:
                QtWidgets.QMessageBox.warning(self, "File Not Found", "The file does not exist.")
        elif column == 1:
            file_path_item = self.table.item(row, 3) if self.sender() == self.table else self.table2.item(row, 3)
            file_path = file_path_item.text()
            if os.path.exists(file_path):
                os.startfile(file_path)
            else:
                QtWidgets.QMessageBox.warning(self, "File Not Found", "The file does not exist.")
        elif column == 4:  
            file_path = self.table.item(row, 3).text() if self.sender() == self.table else self.table2.item(row, 3).text()
            if os.path.exists(file_path):
                folder_path = os.path.dirname(file_path)  
                self.populate_folder_table(folder_path) 
                self.stackedWidget.setCurrentIndex(1)  
            else:
                QtWidgets.QMessageBox.warning(self, "File Not Found", "The file does not exist.")

        elif column == 5:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                msg_box.setWindowTitle("Delete Warning")
                msg_box.setText("Are you sure you want to delete the file from Google Drive?")
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
                result = msg_box.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    file_path = self.table.item(row, 3).text() if self.table.item(row, column) == self.table.item(row, column) else self.table2.item(row, 3).text()
                    connector.delete_file_from_drive(file_path)
                    self.table.removeRow(row)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("SwiftSynk")
    selected=[x[2] for x in connector.dbm.getFiles()]
    print("hii", selected)
    window.show_files_on_table(selected)
    window.show()
    sys.exit(app.exec_())