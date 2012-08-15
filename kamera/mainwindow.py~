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

import os

import opencv
import Image
import ImageQt

from PyQt4 import QtCore
from PyQt4 import QtGui

from opencvwidget import OpenCVWidget, CamThread
from ui_mainwindow import Ui_MainWindow
from configwindow import ConfigWindow
from defaultsettings import IMAGE_DIRECTORY, IMAGE_FORMAT, VIDEO_FLIP_LEFT_RIGHT, VIDEO_FLIP_TOP_BOTTOM
import __init__

class MyOpenCVWidget(OpenCVWidget):
    def __init__(self, label):
        QtGui.QWidget.__init__(self)
        self.imageLabel = label
        self.camThread = CamThread()
        self.connect(self.camThread, QtCore.SIGNAL("image"), self.updateImage)
        self.camThread.start()
        self.settings = QtCore.QSettings()

    def updateImage(self, cvimage):
        try:
            image = opencv.adaptors.Ipl2PIL(cvimage)
            if self.settings.value("video/flip_left_right", VIDEO_FLIP_LEFT_RIGHT).toBool():
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            if self.settings.value("video/flip_top_bottom", VIDEO_FLIP_TOP_BOTTOM).toBool():
                image = image.transpose(Image.FLIP_TOP_BOTTOM)
            self.image = ImageQt.ImageQt(image)
            self.pixmap = QtGui.QPixmap.fromImage(self.image)
            self.imageLabel.setPixmap(self.pixmap)
        except TypeError:
            self.emit(QtCore.SIGNAL("error"), QtGui.QApplication.translate("MainWindow", "No webcam found"))
            self.camThread.terminate()

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.settings = QtCore.QSettings()
        QtCore.QDir.setCurrent(self.settings.value("image/directory", IMAGE_DIRECTORY).toString())
        self.createImageList()
        self.opencvwidget = MyOpenCVWidget(self.label_webcam)
        self.configWindow = ConfigWindow(self)
        self.connect(self.opencvwidget, QtCore.SIGNAL("error"), self.label_webcam.setText)

    def createImageList(self):
        self.imageFiles = [file for file in os.listdir(".") if file.startswith("kamera_")]
        self.imageFiles.sort()
        imageLayout = QtGui.QHBoxLayout()
        self.imageListWidget = QtGui.QWidget()
        self.imageListWidget.setLayout(imageLayout)
        for imageFile in self.imageFiles:
            self.addImage(QtGui.QPixmap(imageFile))
        self.scrollArea_photos.setWidget(self.imageListWidget)

    def addImage(self, pixmap):
        label = QtGui.QLabel(self.imageListWidget)
        label.setPixmap(pixmap.scaledToHeight(100))
        label.setMaximumSize(label.pixmap().size())
        label.setStyleSheet("border-right:2px solid gray;border-bottom:2px solid black")
        self.imageListWidget.layout().insertWidget(0, label)

    @QtCore.pyqtSignature("bool")
    def on_pushButton_save_clicked(self):
        fileextension = self.settings.value("image/format", IMAGE_FORMAT).toString()
        filename = "kamera_%s.%s" % (QtCore.QDateTime.currentDateTime().toString("yyyyMMdd-hhmmss"), fileextension)
        self.opencvwidget.snapShot().save(filename)
        self.addImage(self.opencvwidget.pixmap)

    @QtCore.pyqtSignature("bool")
    def on_pushButton_about_clicked(self):
        title = QtGui.QApplication.translate("MainWindow", "About Kamera")
        text = QtGui.QApplication.translate("MainWindow", "Kamera %1 - webcam photographer\nThis software is released under the terms of GPL v3.\nhttp://kamera.googlecode.com\n\nDeveloper:\nUgur Cetin <ugur.jnmbk at gmail.com>").arg(__init__.__version__)
        QtGui.QMessageBox.about(self, title, text)

    @QtCore.pyqtSignature("bool")
    def on_pushButton_configure_clicked(self):
        self.configWindow.show()
