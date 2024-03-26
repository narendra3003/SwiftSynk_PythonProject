import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
import ui, dbm, connector
import math, os
import connector

imgpath = ui.imgpath

def refresh_table(self):
        data=connector.dbm.providePaths(connector.base_drive_folder_id, connector.email)
        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)
        self.show_folders_on_table(data[0])
        self.show_files_on_table(data[1])

        
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

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