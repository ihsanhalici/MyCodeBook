# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Wed Jan 21 06:53:15 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 705)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/kamera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_webcam = QtGui.QLabel(self.centralwidget)
        self.label_webcam.setMinimumSize(QtCore.QSize(640, 480))
        self.label_webcam.setAlignment(QtCore.Qt.AlignCenter)
        self.label_webcam.setObjectName("label_webcam")
        self.horizontalLayout_2.addWidget(self.label_webcam)
        spacerItem1 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtGui.QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_configure = QtGui.QPushButton(self.centralwidget)
        self.pushButton_configure.setObjectName("pushButton_configure")
        self.horizontalLayout.addWidget(self.pushButton_configure)
        self.pushButton_about = QtGui.QPushButton(self.centralwidget)
        self.pushButton_about.setObjectName("pushButton_about")
        self.horizontalLayout.addWidget(self.pushButton_about)
        spacerItem2 = QtGui.QSpacerItem(439, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea_photos = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_photos.setMinimumSize(QtCore.QSize(0, 140))
        self.scrollArea_photos.setWidgetResizable(True)
        self.scrollArea_photos.setObjectName("scrollArea_photos")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea_photos)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 649, 136))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_photos.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea_photos)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Kamera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_webcam.setText(QtGui.QApplication.translate("MainWindow", "Getting video from webcam", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_configure.setText(QtGui.QApplication.translate("MainWindow", "&Configure...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_about.setText(QtGui.QApplication.translate("MainWindow", "&About...", None, QtGui.QApplication.UnicodeUTF8))

import kamera_rc
