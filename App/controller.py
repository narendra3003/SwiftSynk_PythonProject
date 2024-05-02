import threading
import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
import connector.classes
from ui import Ui_MainWindow
import ui
import math, os
import connector.authentication
import connector.fileoprations
import connector.folderoprations
import connector.helpers
import connector.reuploader
import connector.state_features
import connector.log
import connector.basic
from ui import Ui_MainWindow
import ui
import math, os
import dbm

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
        self.userlabel.setText(str(dbm.getUsers()[1][0]))
        self.syncButton.clicked.connect(self.sync_files)
        self.syncButton2.clicked.connect(self.sync_folders)
        self.table.cellDoubleClicked.connect(self.open_item_explorer)
        self.table2.cellDoubleClicked.connect(self.open_item_explorer)
        self.icon_provider = QtWidgets.QFileIconProvider()
        self.backbutton.clicked.connect(self.go_to_page)
        self.gdrivebutton.clicked.connect(self.gdrive)
        self.signupbutton.clicked.connect(self.signup)
        for button in [self.lmhome,self.lmhome2, self.lmhome3, self.lmhome4]:
            button.clicked.connect(self.home)
        for button in [self.lmlog,self.lmlog2, self.lmlog3, self.lmlog4]:
            button.clicked.connect(self.log)
        for button in [self.lmuser,self.lmuser2, self.lmuser3, self.lmuser4]:
            button.clicked.connect(self.user)
        self.refresh_but.clicked.connect(self.populate_log_table)
        self.dellog_but.clicked.connect(self.deleteLogRecords)
        self.logout.clicked.connect(self.deleteuser)

        if(dbm.getUsers() != ()):
            self.stackedWidget.setCurrentWidget(self.page)
        else:
            self.stackedWidget.setCurrentWidget(self.page_5)
        

    def deleteuser(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setWindowTitle("Delete Warning")
        msg_box.setText("Do you want to delete the account with all the files on drive?")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
        result = msg_box.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            msg_box.setWindowTitle("Delete Warning")
            msg_box.setText("Delete the account with all the files on drive?")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
            result = msg_box.exec_()
            if result == QtWidgets.QMessageBox.Yes:
                # delete the user with all the files
                pass
        else:
            #delete user without deleting files
            pass


    def deleteLogRecords(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setWindowTitle("Delete Warning")
        msg_box.setText("Are you sure you want to delete all the log files?")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
        result = msg_box.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            dbm.deletelog()
        self.populate_log_table()

    def home(self):
        self.stackedWidget.setCurrentWidget(self.page)
    def log(self):
        self.stackedWidget.setCurrentWidget(self.page_6)
    def user(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

    def gdrive(self):
        # Email address redirect function
        # if gmail login successful then ↓
        if(not connector.classes.isUserPresent()):
            self.stackedWidget.setCurrentWidget(self.page_4)
        else:
            pass

    def refresh_table(self):
        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)
        data=dbm.providePaths(connector.basic.mainUser.base_drive_folder_id, connector.basic.mainUser.username)
        self.show_folders_on_table(data[0])
        self.show_files_on_table(data[1])
        self.file_count, self.folder_count = dbm.countFiles()
        self.fileno.setText("Total Files Synced: "+ str(self.file_count[0]))
        self.folderno.setText("Total Folders Synced: "+ str(self.folder_count[0]))


    def signup(self):
        username = self.unamebox_su.text()
        creds = connector.authentication.authenticate()
        service = connector.helpers.build('drive', 'v3', credentials=creds)
        base_drive_folder_id= connector.authentication.create_folder(service, username+"_SwiftSynK")
        connector.authentication.grant_access(service, base_drive_folder_id)
        secondary_folder_id=connector.folderoprations.create_folder_in_parent_on_drive("Second_space", base_drive_folder_id)
        signedUp=dbm.insertUser(username, base_drive_folder_id, secondary_folder_id)
        connector.basic.mainUser.modifyUser(username, base_drive_folder_id, secondary_folder_id)

        if(signedUp==1):
            self.stackedWidget.setCurrentWidget(self.page) #correct signUp
        else:
            QtWidgets.QMessageBox.warning(self,"Signup failed","Error") # invalid signUp

    def signOut(self):
        username=connector.basic.mainUser.username
        dbm.deleteUser(username)
        connector.basic.mainUser.modifyUser(None, "", "")
    
    def syncingfiles(self, files):
        print("called and file_path = ", files)
        for file in files:
            if os.path.isdir(file):
                file_info = QtCore.QDir(file)
            else:
                file_info = QtCore.QFileInfo(file)
                print("File Info:", file_info)
            row_position = self.table.rowCount()
            print("Before Row Position: ", row_position)
            self.table.insertRow(row_position)
            print("After row position: ", row_position)

            icon = self.icon_provider.icon(file_info)
            icon_label = QtWidgets.QLabel()
            icon_label.setPixmap(icon.pixmap(20, 20))
            icon_label.setAlignment(QtCore.Qt.AlignCenter)
            self.table.setCellWidget(row_position, 0, icon_label)

            item_name = QtWidgets.QTableWidgetItem(file_info.fileName())
            item_name.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_name.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 1, item_name)

            item_status = QtWidgets.QTableWidgetItem("Syncing....")
            item_status.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_status.setForeground(QtGui.QColor('grey'))
            item_status.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 2, item_status)

            item_path = QtWidgets.QTableWidgetItem(file_info.absoluteFilePath())
            item_path.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_path.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 10, item_path)

            item_size = QtWidgets.QTableWidgetItem(convert_size(file_info.size()))
            item_size.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_size.setTextAlignment(QtCore.Qt.AlignCenter)
            if os.path.isdir(file):
                item_size.setText("▶")
            else:
                item_size.setText(convert_size(file_info.size()))
            self.table.setItem(row_position, 3, item_size)


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
                if(dbm.is_folder_already_added(folder_path)):
                    QtWidgets.QMessageBox.warning(self, "Folder Already Added", "The folder '{}' is already being synced.".format(folder_path))
                else:
                    # self.syncingfiles(folder_path)
                    connector.folderoprations.upload_folder_to_drive(folder_path)
                    self.refresh_table()

    def show_folders_on_table(self, selected_folders):
        print("Selected Folders: ",selected_folders)
        # row_position=0
        sorted_folders = sorted(selected_folders)
        print("Sorted Folders: ", sorted_folders)
        filtered_folders = sorted_folders.copy()
        for i, folder in enumerate(sorted_folders):
            for other_folder in sorted_folders[i+1:]:
                if folder in other_folder:
                    filtered_folders.remove(other_folder)
                    break
        print("Filtered Folders: ", filtered_folders)
        for folder_path in filtered_folders:
            folder_info = QtCore.QDir(folder_path)
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            
            icon_label = QtWidgets.QLabel()
            icon = self.icon_provider.icon(QtCore.QFileInfo(folder_path))
            icon_label.setPixmap(icon.pixmap(20, 20))
            icon_label.setAlignment(QtCore.Qt.AlignCenter)
            self.table.setCellWidget(row_position, 0, icon_label)
            
            item_name = QtWidgets.QTableWidgetItem(folder_info.dirName())
            item_name.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_name.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 1, item_name)
            
            item_status = QtWidgets.QTableWidgetItem("Synced")
            item_status.setForeground(QtGui.QColor('lightgreen'))
            item_status.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_status.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 2, item_status)
            
            item_path = QtWidgets.QTableWidgetItem(folder_path)
            item_path.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_path.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 11, item_path)
            
            item_size = QtWidgets.QTableWidgetItem("▶")
            item_size.setFont(QtGui.QFont("Bahnschrift Condensed", 15, QtGui.QFont.Bold))
            item_size.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 3, item_size)
            
            item_ps = QtWidgets.QTableWidgetItem()
            item_ps.setIcon(QtGui.QIcon(imgpath + "\\pause.png"))
            item_ps.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 9, item_ps)

            item_del = QtWidgets.QTableWidgetItem()
            item_del.setIcon(QtGui.QIcon(imgpath + "\\remove.png"))
            item_del.setTextAlignment(QtCore.Qt.AlignLeft)
            self.table.setItem(row_position, 10, item_del)


    def sync_files(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                print("Syncing file:", file_path)
                if(dbm.file_already_added(file_path)):
                    QtWidgets.QMessageBox.warning(self, "File Already Exists", "The file '{}' is already being synced.".format(file_path))
                else:
                    # self.syncingfiles(file_path)
                    connector.fileoprations.upload_file_to_drive(file_path)
                    self.refresh_table()

    def show_files_on_table(self, selected_files):
        for file_path in selected_files:
            print("Normal file: ", file_path)
            file_info = QtCore.QFileInfo(file_path)
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            
            icon = self.icon_provider.icon(file_info)
            icon_label = QtWidgets.QLabel()
            icon_label.setPixmap(icon.pixmap(20, 20))
            icon_label.setAlignment(QtCore.Qt.AlignCenter)
            self.table.setCellWidget(row_position, 0, icon_label)

            item_name = QtWidgets.QTableWidgetItem(file_info.fileName())
            item_name.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_name.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 1, item_name)

            item_status = QtWidgets.QTableWidgetItem(dbm.getSize(file_path))
            item_status.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            if(dbm.getSize(file_path) == 'Synced'):
                item_status.setForeground(QtGui.QColor('lightgreen'))
            else:
                item_status.setForeground(QtGui.QColor('grey'))
            item_status.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 2, item_status)

            item_path = QtWidgets.QTableWidgetItem(file_info.absoluteFilePath())
            item_path.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_path.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 11, item_path)

            item_size = QtWidgets.QTableWidgetItem(convert_size(file_info.size()))
            item_size.setFont(QtGui.QFont("Bahnschrift Condensed", 10, QtGui.QFont.Bold))
            item_size.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 3, item_size)


            if(dbm.is_twoStated(file_path)):
                item_2down = QtWidgets.QTableWidgetItem()
                item_2down.setIcon(QtGui.QIcon(imgpath + "\\download.png")) #download
                item_2down.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row_position, 5, item_2down)

                item_retnew = QtWidgets.QTableWidgetItem()
                item_retnew.setIcon(QtGui.QIcon(imgpath + "\\clock1.png")) #delete current, retain previous
                item_retnew.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row_position, 6, item_retnew)

                item_step = QtWidgets.QTableWidgetItem()
                item_step.setIcon(QtGui.QIcon(imgpath + "\\exchange.png")) # step for 2 state
                item_step.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row_position, 7, item_step)

                item_2stop = QtWidgets.QTableWidgetItem()
                item_2stop.setIcon(QtGui.QIcon(imgpath + "\\clock2.png")) #delete previous, retain current
                item_2stop.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row_position, 8, item_2stop)

            else:
                item_2st = QtWidgets.QTableWidgetItem()
                item_2st.setIcon(QtGui.QIcon(imgpath + "\\2stateinit.png")) # initiate 2state
                item_2st.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row_position, 8, item_2st)

            item_ps = QtWidgets.QTableWidgetItem()
            item_ps.setIcon(QtGui.QIcon(imgpath + "\\pause.png"))
            item_ps.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row_position, 9, item_ps)
            
            item_del = QtWidgets.QTableWidgetItem()
            item_del.setIcon(QtGui.QIcon(imgpath + "\\remove.png"))
            item_del.setTextAlignment(QtCore.Qt.AlignLeft)
            self.table.setItem(row_position, 10, item_del)

    def populate_log_table(self):
        self.logtable.clearContents()
        self.logtable.setRowCount(0)
        data = connector.log.getlogdata()
        for dataset in reversed(data):
            row_position = self.logtable.rowCount()
            self.logtable.insertRow(row_position)

            time = dataset[0]
            time_item = QtWidgets.QTableWidgetItem(str(time))
            time_item.setFont(QtGui.QFont("Bahnschrift Condensed", 10))
            time_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.logtable.setItem(row_position, 0, time_item)

            log_desc = dataset[1]
            log_desc_item = QtWidgets.QTableWidgetItem(log_desc)
            log_desc_item.setFont(QtGui.QFont("Bahnschrift Condensed", 10))
            log_desc_item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.logtable.setItem(row_position, 1, log_desc_item)


    def open_item_explorer(self, row, column):
        # if column == 3:  
        #     file_path = self.table.item(row, column).text() if self.sender() == self.table else self.table2.item(row, column).text()
        #     if os.path.exists(file_path):
        #         folder_path = os.path.dirname(file_path)  
        #         os.startfile(folder_path) 
        #     else:
        #         QtWidgets.QMessageBox.warning(self, "File Not Found", "The file does not exist.")

        if column == 1:
            file_path_item = self.table.item(row, 11) if self.sender() == self.table else self.table2.item(row, 3)
            file_path = file_path_item.text()
            if os.path.exists(file_path):
                os.startfile(file_path)
            else:
                QtWidgets.QMessageBox.warning(self, "File Not Found", "The file does not exist.")
        elif (column == 3 and os.path.isdir(self.table.item(row, 11).text()) and self.sender() == self.table):  
            file_path = self.table.item(row, 11).text()
            if os.path.exists(file_path):
                folder_path = os.path.dirname(file_path)
                self.populate_folder_table(file_path) 
                self.stackedWidget.setCurrentIndex(1)  
            else:
                QtWidgets.QMessageBox.warning(self, "Folder Not Found", "The folder does not exist.")

        elif(column == 4 and os.path.isdir(self.table2.item(row, 3).text()) and self.sender() == self.table2):
            file_path = self.table2.item(row, 3).text()
            if os.path.exists(file_path):
                folder_path = os.path.dirname(file_path)
                self.populate_folder_table(file_path) 
                self.stackedWidget.setCurrentIndex(1)
            else:
                QtWidgets.QMessageBox.warning(self, "Folder Not Found", "The folder does not exist.")

        elif (column == 5 and os.path.isfile(self.table.item(row, 11).text()) and dbm.is_twoStated(self.table.item(row, 11).text())):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Question)
            msg_box.setWindowTitle("Download Previous State File?")
            msg_box.setText("Do you want to replace this file's previous saved state?")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg_box.setDefaultButton(QtWidgets.QMessageBox.Yes)
            result = msg_box.exec_()
            if result == QtWidgets.QMessageBox.Yes:
                connector.state_features.download_file_from_drive(dbm.getVersion(dbm.give_id_by_path(self.table.item(row, 11).text()))) #download
                tooltip = QtWidgets.QLabel("Downloaded", self)
                tooltip.setStyleSheet("QLabel { background-color: lightgrey; color: black; padding: 4px; border-radius: 4px; font-family: Bahnschrift; }")
                tooltip.setGraphicsEffect(self.createShadowEffect())
                tooltip.move(510, 680)
                tooltip.resize(120, 25)
                tooltip.show()
                QtCore.QTimer.singleShot(3000, tooltip.hide)
                print("should download")

        elif (column == 6 and os.path.isfile(self.table.item(row, 11).text()) and dbm.is_twoStated(self.table.item(row, 11).text())):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Question)
            msg_box.setWindowTitle("Retain Previous state?")
            msg_box.setText("Do you want to delete this file's current state and retain the previous state on Drive?")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
            result = msg_box.exec_()
            if result == QtWidgets.QMessageBox.Yes:
                connector.state_features.getBackToVersion(self.table.item(row, 11).text()) #retain previous, delete new
                tooltip = QtWidgets.QLabel("Updates Done", self)
                tooltip.setStyleSheet("QLabel { background-color: lightgrey; color: black; padding: 4px; border-radius: 4px; font-family: Bahnschrift; }")
                tooltip.setGraphicsEffect(self.createShadowEffect())
                tooltip.move(510, 680)
                tooltip.resize(100, 25)
                tooltip.show()
                QtCore.QTimer.singleShot(3000, tooltip.hide)
                self.refresh_table()

        elif (column == 7 and os.path.isfile(self.table.item(row, 11).text()) and dbm.is_twoStated(self.table.item(row, 11).text())):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Question)

            if (dbm.is_twoStated(self.table.item(row, 11).text())):
                msg_box.setWindowTitle("Update this as latest state?")
                msg_box.setText("Do you want to update this file's previous state as current state?")
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
                result = msg_box.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    connector.state_features.updateVersion(self.table.item(row, 11).text()) #update version
                    tooltip = QtWidgets.QLabel("Updated previous version", self)
                    tooltip.setStyleSheet("QLabel { background-color: lightgrey; color: black; padding: 4px; border-radius: 4px; font-family: Bahnschrift; }")
                    tooltip.setGraphicsEffect(self.createShadowEffect())
                    tooltip.move(510, 680)
                    tooltip.resize(150, 25)
                    tooltip.show()
                    QtCore.QTimer.singleShot(3000, tooltip.hide)
                    self.refresh_table()

        elif (column == 8 and os.path.isfile(self.table.item(row, 11).text())):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Question)

            if (dbm.is_twoStated(self.table.item(row, 11).text())):
                msg_box.setWindowTitle("Keep Current state?")
                msg_box.setText("Do you want to delete this file's previous state and keep only the current state on Drive?")
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
                result = msg_box.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    connector.state_features.retainVersion(self.table.item(row, 11).text()) #retain current, delete previous
                    tooltip = QtWidgets.QLabel("Updates Done", self)
                    tooltip.setStyleSheet("QLabel { background-color: lightgrey; color: black; padding: 4px; border-radius: 4px; font-family: Bahnschrift; }")
                    tooltip.setGraphicsEffect(self.createShadowEffect())
                    tooltip.move(510, 680)
                    tooltip.resize(100, 25)
                    tooltip.show()
                    QtCore.QTimer.singleShot(3000, tooltip.hide)
                    self.refresh_table()

            else:
                msg_box.setWindowTitle("Note")
                msg_box.setText("Do you want to initiate 2 State for this file?")
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                msg_box.setDefaultButton(QtWidgets.QMessageBox.Yes)
                result = msg_box.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    connector.state_features.create_state2_file(self.table.item(row, 11).text()) #2state initiation function
                    tooltip = QtWidgets.QLabel("2-State initiated", self)
                    tooltip.setStyleSheet("QLabel { background-color: lightgrey; color: black; padding: 4px; border-radius: 4px; font-family: Bahnschrift; }")
                    tooltip.setGraphicsEffect(self.createShadowEffect())
                    tooltip.move(510, 680)
                    tooltip.resize(120, 25)
                    tooltip.show()
                    QtCore.QTimer.singleShot(3000, tooltip.hide)
                    self.refresh_table()

            

        elif column == 9:
            connector.state_features.toggeleUpload(self.table.item(row, 11).text(), self.table.item(row, 2).text())
            self.refresh_table()

        elif column == 10:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Question)
            msg_box.setWindowTitle("Delete Warning")
            msg_box.setText("Are you sure you want to delete the file from Google Drive?")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
            result = msg_box.exec_()
            if result == QtWidgets.QMessageBox.Yes:

                path = self.table.item(row, 11).text() if self.table.item(row, column) == self.table.item(row, column) else self.table2.item(row, 3).text()
                if os.path.isdir(path):
                    dbm.deleteFolder(connector.folderoprations.delete_folder_from_drive(path))
                else:
                    dbm.deleteFile(connector.fileoprations.delete_file_from_drive(path))
                self.table.removeRow(row)
                tooltip_text = "Deleted " + os.path.basename(path)
                tooltip = QtWidgets.QLabel(tooltip_text, self)
                tooltip.setStyleSheet("QLabel { background-color: lightgrey; color: black; padding: 4px; border-radius: 4px; font-family: Bahnschrift; }")
                tooltip.setGraphicsEffect(self.createShadowEffect())
                tooltip.move(530, 680)
                tooltip.resize(200, 25)
                tooltip.show()
                QtCore.QTimer.singleShot(3000, tooltip.hide)
            self.refresh_table()

    def createShadowEffect(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setColor(QtGui.QColor(50, 50, 50, 150))
        shadow.setOffset(2, 2)
        return shadow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("SwiftSynk")
    window.refresh_table()
    thread = threading.Thread(target=connector.reuploader.modifiedUploader)
    thread.start()
    window.show()
    sys.exit(app.exec_())