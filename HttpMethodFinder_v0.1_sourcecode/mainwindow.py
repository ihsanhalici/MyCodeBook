# -*- coding: utf-8 -*-

#This program used for finding allow http methods
#Copyright (C) 2011  Kaan KULA

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Form implementation generated from reading ui file 'C:\Users\Kaan\Desktop\Projects\HttpMethod\mainwindow.ui'
#
# Created: Sun Apr 03 23:17:44 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(459, 510)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 41, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.findmethods = QtGui.QPushButton(self.centralwidget)
        self.findmethods.setGeometry(QtCore.QRect(150, 90, 75, 23))
        self.findmethods.setObjectName(_fromUtf8("findmethods"))
        self.server_text = QtGui.QLineEdit(self.centralwidget)
        self.server_text.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.server_text.setObjectName(_fromUtf8("server_text"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 63, 46, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.port_text = QtGui.QLineEdit(self.centralwidget)
        self.port_text.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.port_text.setObjectName(_fromUtf8("port_text"))
        self.result = QtGui.QTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(80, 160, 271, 281))
        self.result.setObjectName(_fromUtf8("result"))
        self.label3 = QtGui.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(80, 120, 211, 31))
        self.label3.setText(_fromUtf8(""))
        self.label3.setObjectName(_fromUtf8("label3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionUsage = QtGui.QAction(MainWindow)
        self.actionUsage.setObjectName(_fromUtf8("actionUsage"))
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Server :", None, QtGui.QApplication.UnicodeUTF8))
        self.findmethods.setText(QtGui.QApplication.translate("MainWindow", "Find Methods", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Port : ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsage.setText(QtGui.QApplication.translate("MainWindow", "Usage", None, QtGui.QApplication.UnicodeUTF8))

