import threading
import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from ui import Ui_MainWindow
import ui
import math, os
import connector

imgpath = ui.imgpath

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
        self.populate_log_table()
        self.syncButton.clicked.connect(self.sync_files)
        self.syncButton2.clicked.connect(self.sync_folders)
        self.table.cellDoubleClicked.connect(self.open_item_explorer)
        self.table2.cellDoubleClicked.connect(self.open_item_explorer)
        self.icon_provider = QtWidgets.QFileIconProvider()
        self.backbutton.clicked.connect(self.go_to_page)
        self.loginbutton.clicked.connect(self.login)
        self.gdrivebutton.clicked.connect(self.gdrive)
        self.loginswitch.clicked.connect(self.login_switch)
        self.signupswitch.clicked.connect(self.signup_switch)
        for button in [self.lmhome,self.lmhome2, self.lmhome3]:
            button.clicked.connect(self.home)
        for button in [self.lmlog,self.lmlog2, self.lmlog3]:
            button.clicked.connect(self.log)

        self.stackedWidget.setCurrentWidget(self.page_5)

    def home(self):
        self.stackedWidget.setCurrentWidget(self.page)
    def log(self):
        self.stackedWidget.setCurrentWidget(self.page_6)

    def gdrive(self):
        self.stackedWidget.setCurrentWidget(self.page_4)

    def login_switch(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

    def signup_switch(self):
        self.stackedWidget.setCurrentWidget(self.page_4)

    def refresh_table(self):
        data=connector.dbm.providePaths(connector.base_drive_folder_id, connector.email)
        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)
        self.show_folders_on_table(data[0])
        self.show_files_on_table(data[1])

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

    def signup(self):
        username = self.unamebox_su.text()
        email = self.emailbox.text()
        password = self.passbox_su.text()
        print(username,email,password)

        if(connector.dbm.insertSignup(email,username,password)==1):
            self.stackedWidget.setCurrentIndex(3)
        elif(connector.dbm.insertSignup(email,username,password==0)):
            QtWidgets.QMessageBox.warning(self, "Password must contain 8 characters")
        else:
            QtWidgets.QMessageBox.warning(self,"Signup failed","Error")


    
        


    def go_to_page(self):
        if(self.counter == 1):
            self.counter -= 1
            self.stackedWidget.setCurrentIndex(0)
        else:  
            self.populate_folder_table(self.backpath)

    counter = 0
    backpath = ''

    def populate_folder_table(self, folder_path):
        if(inspect.stack()[1].function == 'go_to_page'):
            self.counter -= 1
            print(self.counter)
        else:
            self.counter += 1
            print(self.counter)
        self.backpath = os.path.dirname(folder_path)
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
            item_name.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_name.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table2.setItem(row_position, 1, item_name)

            item_status = QtWidgets.QTableWidgetItem("Synced")
            item_status.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_status.setForeground(QtGui.QColor('lightgreen'))
            item_status.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table2.setItem(row_position, 2, item_status)

            item_path = QtWidgets.QTableWidgetItem(file_info.absoluteFilePath())
            item_path.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_path.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table2.setItem(row_position, 3, item_path)

            item_size = QtWidgets.QTableWidgetItem(convert_size(file_info.size()))
            item_size.setFont(QtGui.QFont("Bahnschrift Condensed", 15, QtGui.QFont.Bold))
            item_size.setTextAlignment(QtCore.Qt.AlignCenter)
            if os.path.isdir(file_path):
                item_size.setText("▶")
            else:
                item_size.setText(convert_size(file_info.size()))
            self.table2.setItem(row_position, 4, item_size)

    def sync_folders(self):
        folder_dialog = QtWidgets.QFileDialog(self)
        folder_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        folder_dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        if folder_dialog.exec_():
            selected_folders = folder_dialog.selectedFiles()
            for folder_path in selected_folders:
                print("folder", folder_path)
                if(connector.dbm.is_folder_already_added(folder_path)):
                    QtWidgets.QMessageBox.warning(self, "Folder Already Added", "The folder '{}' is already being synced.".format(folder_path))
                else:
                    connector.upload_folder_to_drive(folder_path)
                    self.refresh_table()

    def show_folders_on_table(self, selected_folders):
        # row_position=0
        for folder_path in selected_folders:
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
            item_name.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_name.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 1, item_name)
            
            # Add folder status
            item_status = QtWidgets.QTableWidgetItem("Synced")
            item_status.setForeground(QtGui.QColor('lightgreen'))
            item_status.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_status.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 2, item_status)
            
            # Add folder path
            item_path = QtWidgets.QTableWidgetItem(folder_path)
            item_path.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_path.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 3, item_path)
            
            # Add folder size
            item_size = QtWidgets.QTableWidgetItem("▶")
            item_size.setFont(QtGui.QFont("Bahnschrift Condensed", 15, QtGui.QFont.Bold))
            item_size.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 4, item_size)
            
            item_ps = QtWidgets.QTableWidgetItem()
            item_ps.setIcon(QtGui.QIcon(imgpath + "\\pause.png"))
            item_ps.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 5, item_ps)

            item_del = QtWidgets.QTableWidgetItem()
            item_del.setIcon(QtGui.QIcon(imgpath + "\\remove.png"))
            item_del.setTextAlignment(QtCore.Qt.AlignLeft)
            self.table.setItem(row_position, 6, item_del)


    def sync_files(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                print(file_path)
                if(connector.dbm.file_already_added(file_path)):
                    QtWidgets.QMessageBox.warning(self, "File Already Exists", "The file '{}' is already being synced.".format(file_path))
                else:
                    connector.upload_file_to_drive(file_path)
                    self.refresh_table()

    def show_files_on_table(self, selected_files):
        for file_path in selected_files:
            file_info = QtCore.QFileInfo(file_path)
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            
            icon = self.icon_provider.icon(file_info)
            icon_label = QtWidgets.QLabel()
            icon_label.setPixmap(icon.pixmap(20, 20))
            icon_label.setAlignment(QtCore.Qt.AlignCenter)
            self.table.setCellWidget(row_position, 0, icon_label)

            item_name = QtWidgets.QTableWidgetItem(file_info.fileName())
            item_name.setFont(QtGui.QFont("Bahnschrift Condensed", 10))
            item_name.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 1, item_name)

            item_status = QtWidgets.QTableWidgetItem("Synced")
            item_status.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_status.setForeground(QtGui.QColor('lightgreen'))
            item_status.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 2, item_status)

            item_path = QtWidgets.QTableWidgetItem(file_info.absoluteFilePath())
            item_path.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_path.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 3, item_path)

            item_size = QtWidgets.QTableWidgetItem(convert_size(file_info.size()))
            item_size.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_size.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 4, item_size)

            item_ps = QtWidgets.QTableWidgetItem()
            item_ps.setIcon(QtGui.QIcon(imgpath + "\\pause.png"))
            item_ps.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 5, item_ps)
            
            item_del = QtWidgets.QTableWidgetItem()
            item_del.setIcon(QtGui.QIcon(imgpath + "\\remove.png"))
            item_del.setTextAlignment(QtCore.Qt.AlignLeft)
            self.table.setItem(row_position, 6, item_del)

    def populate_log_table(self):
        data = connector.getlogdata()
        print("Data:", data)
        for dataset in data:
            row_position = self.logtable.rowCount()
            self.logtable.insertRow(row_position)
            print("Row Position:", row_position)

            log_type = dataset[0]
            print("Log Type:", log_type)
            log_type_item = QtWidgets.QTableWidgetItem(log_type)
            log_type_item.setFont(QtGui.QFont("Bahnschrift Condensed", 10))
            log_type_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.logtable.setItem(row_position, 0, log_type_item)

            if len(dataset) > 4:
                if log_type != 'User':
                    file_name = os.path.basename(dataset[4])
                    file_name_item = QtWidgets.QTableWidgetItem(file_name)
                    file_name_item.setFont(QtGui.QFont("Bahnschrift Condensed", 10))
                    file_name_item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.logtable.setItem(row_position, 1, file_name_item)
                else:
                    user_name = dataset[4]
                    user_name_item = QtWidgets.QTableWidgetItem(user_name)
                    user_name_item.setFont(QtGui.QFont("Bahnschrift Condensed", 10))
                    user_name_item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.logtable.setItem(row_position, 1, user_name_item)

            action = dataset[1].capitalize()
            action_item = QtWidgets.QTableWidgetItem(action)
            action_item.setFont(QtGui.QFont("Bahnschrift Condensed", 10))
            action_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.logtable.setItem(row_position, 2, action_item)

            time = dataset[3]
            time_item = QtWidgets.QTableWidgetItem(str(time))  # Assuming time is a string or convertible to string
            time_item.setFont(QtGui.QFont("Bahnschrift Condensed", 10))
            time_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.logtable.setItem(row_position, 3, time_item)

            if len(dataset) > 4 and log_type != 'User':
                path = dataset[4]
                path_item = QtWidgets.QTableWidgetItem(path)
                path_item.setFont(QtGui.QFont("Bahnschrift Condensed", 10))
                path_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.logtable.setItem(row_position, 4, path_item)
            print("Table populated successfully")
            

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
            if self.sender() == self.table:
                # file_path = self.table.item(row, 3).text() if self.sender() == self.table else self.table2.item(row, 3).text()
                file_path = self.table.item(row, 3).text()
                if os.path.exists(file_path):
                    folder_path = os.path.dirname(file_path)
                    # self.counter += 1
                    # print(self.counter)
                    self.populate_folder_table(file_path) 
                    self.stackedWidget.setCurrentIndex(1)  
                else:
                    QtWidgets.QMessageBox.warning(self, "Folder Not Found", "The folder does not exist.")

            elif self.sender() == self.table2:
                file_path = self.table2.item(row, 3).text()
                if os.path.exists(file_path):
                    folder_path = os.path.dirname(file_path)
                    self.populate_folder_table(file_path) 
                    self.stackedWidget.setCurrentIndex(1)  
                else:
                    QtWidgets.QMessageBox.warning(self, "Folder Not Found", "The folder does not exist.")


        elif column == 5:
            pass
            #for pause sync

        elif column == 6:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("Delete Warning")
            msg_box.setText("Are you sure you want to delete the file from Google Drive?")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
            result = msg_box.exec_()
            if result == QtWidgets.QMessageBox.Yes:
                path = self.table.item(row, 3).text() if self.table.item(row, column) == self.table.item(row, column) else self.table2.item(row, 3).text()
                if os.path.isdir(path):
                    connector.dbm.deleteFolder(connector.delete_folder_from_drive(path))
                else:
                    connector.dbm.deleteFile(connector.delete_file_from_drive(path))
                self.table.removeRow(row)
            self.refresh_table()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("SwiftSynk")
    window.refresh_table()
    thread = threading.Thread(target=connector.modifiedUploader)
    thread.start()
    window.show()
    sys.exit(app.exec_())