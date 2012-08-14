# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ana_ekran.ui'
#
# Created: Mon Aug 13 21:53:46 2012
#      by: PyQt4 UI code generator 4.9.1
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
        MainWindow.resize(369, 286)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../usr/share/icons/Humanity/actions/64/stock_new-text.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 369, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDosya = QtGui.QMenu(self.menubar)
        self.menuDosya.setObjectName(_fromUtf8("menuDosya"))
        self.menuHakkimda = QtGui.QMenu(self.menubar)
        self.menuHakkimda.setObjectName(_fromUtf8("menuHakkimda"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionKapat = QtGui.QAction(MainWindow)
        self.actionKapat.setObjectName(_fromUtf8("actionKapat"))
        self.actionHakkimda = QtGui.QAction(MainWindow)
        self.actionHakkimda.setObjectName(_fromUtf8("actionHakkimda"))
        self.menuDosya.addAction(self.actionKapat)
        self.menuHakkimda.addAction(self.actionHakkimda)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuHakkimda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Halit Alptekin", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Ekle", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDosya.setTitle(QtGui.QApplication.translate("MainWindow", "Dosya", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHakkimda.setTitle(QtGui.QApplication.translate("MainWindow", "Ayarlar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionKapat.setText(QtGui.QApplication.translate("MainWindow", "Kapat", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHakkimda.setText(QtGui.QApplication.translate("MainWindow", "Hakkimda", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

