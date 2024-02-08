from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileSystemModel, QMessageBox
from PyQt5.QtCore import QModelIndex, QFileInfo, Qt

from UI import ui
import os, shutil

class CustomFileSystemModel(QFileSystemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.headers = ["Name", "Status", "Size", "Type", "Date Modified"]  # Define headers

    def columnCount(self, parent=QModelIndex()):
        return 5

    def headerData(self, section, orientation, role=0):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section] if section < len(self.headers) else None
        return super().headerData(section, orientation, role)

    def data(self, index, role=0):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            if index.column() == 1:  
                return ""  
            elif index.column() == 2:  
                file_info = QFileInfo(self.filePath(index))
                if file_info.isDir() or file_info.isRoot():
                    return ""
                size = file_info.size()
                size_formatted = self.get_size_formatted(size)
                return size_formatted
            elif index.column() == 3: 
                file_info = QFileInfo(self.filePath(index))
                if file_info.isDir():
                    return ""
                else:
                    return file_info.suffix().upper()
            elif index.column() == 4:  
                file_info = QFileInfo(self.filePath(index))
                return file_info.lastModified().toString(Qt.DefaultLocaleShortDate)
            elif index.column() == 5: 
                return "" 

        return super().data(index, role)



    def get_size_formatted(self, size):
        if size < 1024:
            return f"{size} B"
        size_kb = size / 1024
        if size_kb < 1024:
            return f"{size_kb:.2f} KB"
        size_mb = size_kb / 1024
        if size_mb < 1024:
            return f"{size_mb:.2f} MB"
        size_gb = size_mb / 1024
        return f"{size_gb:.2f} GB"

class MyFileBrowser(ui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()
        self.treeView.setColumnWidth(0, 300)
        
    
    def populate(self):
        path = r"This PC"
        self.setWindowTitle("SyncIN")
        self.model = CustomFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)

        

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        open.triggered.connect(self.open_file)
        sync = menu.addAction("Sync")
        sync.triggered.connect(self.sync_file)
        delete = menu.addAction("Delete")
        delete.triggered.connect(self.delete_file)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

    def delete_file(self):
        index=self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Warning)
        warning.setText("Are you sure you want to delete this file?")
        warning.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        warning.setDefaultButton(QMessageBox.Cancel)
        ret = warning.exec_()
        if ret == QMessageBox.Ok:
            try:
                if os.name == 'nt':  
                    os.makedirs(r'C:\$Recycle.Bin', exist_ok=True)  
                    shutil.move(file_path, os.path.join(r'C:\$Recycle.Bin', os.path.basename(file_path)))
                else:
                    os.remove(file_path)  
                QMessageBox.information(self, "File Deleted", "File has been moved to the recycle bin.")
            except PermissionError:
                QMessageBox.critical(self, "Permission Error", "You do not have sufficient permissions to delete this file.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete file: {e}")
        

    def sync_file(self):
        index = self.treeView.currentIndex()
        self.model.setData(index, "Synced", role=Qt.DisplayRole)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()
