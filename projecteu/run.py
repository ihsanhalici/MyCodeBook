#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui

from ana import Ui_MainWindow
from captacha import *
import sys

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    @QtCore.pyqtSignature("bool")
    def on_pushButton_2_clicked(self):
        soruno = self.spinBox.text()
        cap = captachaCek(soruno)
        cap.captachaindir()
        self.label.setPixmap(QtGui.QPixmap("capler/" + cap.capid +".png"))

    @QtCore.pyqtSignature("bool")
    def on_pushButton_clicked(self):
        cap = captachaCek(self.spinBox.text())
        cap.captachaindir.cevapyaz(self.lineEdit.text(), "123")

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())