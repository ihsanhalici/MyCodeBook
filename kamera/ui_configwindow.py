# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/configwindow.ui'
#
# Created: Wed Jan 21 06:53:16 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ConfigWindow(object):
    def setupUi(self, ConfigWindow):
        ConfigWindow.setObjectName("ConfigWindow")
        ConfigWindow.resize(365, 230)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/kamera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfigWindow.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(ConfigWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtGui.QTabWidget(ConfigWindow)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_image_directory = QtGui.QLineEdit(self.tab)
        self.lineEdit_image_directory.setReadOnly(True)
        self.lineEdit_image_directory.setObjectName("lineEdit_image_directory")
        self.horizontalLayout.addWidget(self.lineEdit_image_directory)
        self.pushButton_image_directory = QtGui.QPushButton(self.tab)
        self.pushButton_image_directory.setObjectName("pushButton_image_directory")
        self.horizontalLayout.addWidget(self.pushButton_image_directory)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.comboBox_image_format = QtGui.QComboBox(self.tab)
        self.comboBox_image_format.setObjectName("comboBox_image_format")
        self.comboBox_image_format.addItem(QtCore.QString())
        self.comboBox_image_format.addItem(QtCore.QString())
        self.comboBox_image_format.addItem(QtCore.QString())
        self.comboBox_image_format.addItem(QtCore.QString())
        self.comboBox_image_format.addItem(QtCore.QString())
        self.comboBox_image_format.addItem(QtCore.QString())
        self.comboBox_image_format.addItem(QtCore.QString())
        self.verticalLayout_2.addWidget(self.comboBox_image_format)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_video_webcam = QtGui.QComboBox(self.tab_2)
        self.comboBox_video_webcam.setObjectName("comboBox_video_webcam")
        self.comboBox_video_webcam.addItem(QtCore.QString())
        self.horizontalLayout_3.addWidget(self.comboBox_video_webcam)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_video_flip_left_right = QtGui.QCheckBox(self.groupBox)
        self.checkBox_video_flip_left_right.setObjectName("checkBox_video_flip_left_right")
        self.verticalLayout_3.addWidget(self.checkBox_video_flip_left_right)
        self.checkBox_video_flip_top_bottom = QtGui.QCheckBox(self.groupBox)
        self.checkBox_video_flip_top_bottom.setObjectName("checkBox_video_flip_top_bottom")
        self.verticalLayout_3.addWidget(self.checkBox_video_flip_top_bottom)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(173, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ConfigWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_image_format.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigWindow)

    def retranslateUi(self, ConfigWindow):
        ConfigWindow.setWindowTitle(QtGui.QApplication.translate("ConfigWindow", "Settings - Kamera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ConfigWindow", "Saving Direcory", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigWindow", "Format", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_image_directory.setText(QtGui.QApplication.translate("ConfigWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_image_format.setItemText(0, QtGui.QApplication.translate("ConfigWindow", "bmp", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_image_format.setItemText(1, QtGui.QApplication.translate("ConfigWindow", "jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_image_format.setItemText(2, QtGui.QApplication.translate("ConfigWindow", "png", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_image_format.setItemText(3, QtGui.QApplication.translate("ConfigWindow", "ppm", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_image_format.setItemText(4, QtGui.QApplication.translate("ConfigWindow", "tiff", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_image_format.setItemText(5, QtGui.QApplication.translate("ConfigWindow", "xbm", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_image_format.setItemText(6, QtGui.QApplication.translate("ConfigWindow", "xpm", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("ConfigWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ConfigWindow", "Webcam", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_video_webcam.setItemText(0, QtGui.QApplication.translate("ConfigWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ConfigWindow", "Flipping", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_video_flip_left_right.setText(QtGui.QApplication.translate("ConfigWindow", "Flip Horizontally", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_video_flip_top_bottom.setText(QtGui.QApplication.translate("ConfigWindow", "Flip Vertically", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ConfigWindow", "Video", None, QtGui.QApplication.UnicodeUTF8))

import kamera_rc
