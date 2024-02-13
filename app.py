from PyQt5 import QtWidgets, uic
import sys, os

class file:
    def __init__(self,file_name, file_status, file_path, file_size):
        self.file_name=file_name
        self.status=file_status
        self.file_path=file_path
        self.size=file_size

# files=[{"file_name" : "reference_files", "status" :"Synced", "file_path": "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\reference_files", "size": "10mb"},
#        {"file_name" : "app.py", "status" :"To Sync", "file_path": "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\app.py", "size": "40kb"}]

files=[file("reference_files", "Synced", "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\reference_files",1000), 
    file("app.py", "To Sync", "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\app.py", 40)]


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setMinimumSize(1270, 720)
        uic.loadUi('app.ui', self)
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,650)
        self.tableWidget.setColumnWidth(3,75)
        self.addData("app.py", "To Sync", "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\app.py", 40)
        self.loadData()
        self.show()

    def loadData(self):
        # row=0
        # self.tableWidget.setRowCount(len(files))
        # for file in files:
        #     self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(files[row].get("file_name")))
        #     self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(files[row].get("status")))
        #     self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(files[row].get("file_path")))
        #     self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(files[row].get("size")))
        #     row+=1
        row=0
        self.tableWidget.setRowCount(len(files))
        for file in files:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(files[row].file_name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(files[row].status))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(files[row].file_path))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(files[row].size))
            row+=1
    def addData(self, file_name, file_status, file_path, file_size):
        files.append(file(file_name, file_status, file_path, file_size))
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
