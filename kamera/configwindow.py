#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under GPL v3
# Copyright 2008, Ugur Cetin
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

from PyQt4 import QtCore
from PyQt4 import QtGui

from ui_configwindow import Ui_ConfigWindow
from defaultsettings import IMAGE_FORMAT, IMAGE_DIRECTORY, VIDEO_FLIP_TOP_BOTTOM, VIDEO_FLIP_LEFT_RIGHT

class ConfigWindow(QtGui.QDialog, Ui_ConfigWindow):
    def __init__(self, parent=0):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        self.settings = QtCore.QSettings()
        self.loadSettings()
        self.connect(self, QtCore.SIGNAL("accepted()"), self.saveSettings)

    def show(self):
        self.loadSettings()
        QtGui.QDialog.show(self)

    def loadSettings(self):
        self.checkBox_video_flip_top_bottom.setChecked(self.settings.value("video/flip_top_bottom", VIDEO_FLIP_TOP_BOTTOM).toBool())
        self.checkBox_video_flip_left_right.setChecked(self.settings.value("video/flip_left_right", VIDEO_FLIP_LEFT_RIGHT).toBool())
        self.lineEdit_image_directory.setText(self.settings.value("image/directory", IMAGE_DIRECTORY).toString())
        self.comboBox_image_format.setCurrentIndex(self.comboBox_image_format.findText(self.settings.value("image/format", IMAGE_FORMAT).toString()))

    def saveSettings(self):
        self.settings.setValue("video/flip_top_bottom", QtCore.QVariant(self.checkBox_video_flip_top_bottom.isChecked()))
        self.settings.setValue("video/flip_left_right", QtCore.QVariant(self.checkBox_video_flip_left_right.isChecked()))
        self.settings.setValue("image/directory", QtCore.QVariant(self.lineEdit_image_directory.text()))
        self.settings.setValue("image/format", QtCore.QVariant(self.comboBox_image_format.currentText()))
        QtCore.QDir.setCurrent(self.settings.value("image/directory", IMAGE_DIRECTORY).toString())
        self.parent().createImageList()

    @QtCore.pyqtSignature("bool")
    def on_pushButton_image_directory_clicked(self):
        self.lineEdit_image_directory.setText(QtGui.QFileDialog.getExistingDirectory(self,
            QtGui.QApplication.translate("ConfigWindow", "Select Image Directory"),
            self.settings.value("image/directory", IMAGE_DIRECTORY).toString()))
