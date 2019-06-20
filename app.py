# bash history gui with pyqt
# https://pythonbasics.org/pyqt/

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
import os
import subprocess

class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('gui.ui', self)

        result = subprocess.check_output("cat ~/\#.bash_history\#", shell=True)
        lines = result.decode("utf-8").split("\n")
        model = QStandardItemModel(self.listView)
        
        for line in lines:
            item = QStandardItem(str(line))
            model.appendRow(item)
         
        self.listView.setModel(model)
 
app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
