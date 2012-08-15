# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(745, 550)
        Dialog.setMinimumSize(QtCore.QSize(745, 550))
        Dialog.setMaximumSize(QtCore.QSize(745, 550))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        Dialog.setFont(font)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 745, 550))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtGui.QTableView(self.horizontalLayoutWidget)
        self.tableView.setMinimumSize(QtCore.QSize(730, 550));
        self.tableView.setMaximumSize(QtCore.QSize(730, 550));
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableView.setFont(font)
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(85)
        self.tableView.horizontalHeader().setMinimumSectionSize(85)
        self.horizontalLayout.addWidget(self.tableView)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Aylık Vakitler (diyanet.gov.tr)", None, QtGui.QApplication.UnicodeUTF8))
