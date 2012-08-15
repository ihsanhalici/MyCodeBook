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

import opencv
from opencv import highgui
import Image
import ImageQt
from PyQt4 import QtCore
from PyQt4 import QtGui
import signal, sys

class CamThread(QtCore.QThread):
    def run(self):
        camera = highgui.cvCreateCameraCapture(0)
        fps = highgui.cvGetCaptureProperty(camera, highgui.CV_CAP_PROP_FPS)
        highgui.cvSetCaptureProperty(camera, highgui.CV_CAP_PROP_FRAME_WIDTH, 640)
        highgui.cvSetCaptureProperty(camera, highgui.CV_CAP_PROP_FRAME_HEIGHT, 480)
        #30 fps if cam gives no value
        if not fps > 0:
            timeout = 33
        else:
            timeout = 1000 / fps
        while True:
            self.msleep(timeout)
            self.cvimage = highgui.cvQueryFrame(camera)
            self.emit(QtCore.SIGNAL("image"), (self.cvimage))

class OpenCVWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        self.imageLabel = QtGui.QLabel()
        layout.addWidget(self.imageLabel)
        self.setLayout(layout)
        self.camThread = CamThread()
        self.connect(self.camThread, QtCore.SIGNAL("image"), self.updateImage)
        self.camThread.start()

    def updateImage(self, cvimage):
        self.image = ImageQt.ImageQt(opencv.adaptors.Ipl2PIL(cvimage).transpose(Image.FLIP_LEFT_RIGHT))
        self.pixmap = QtGui.QPixmap.fromImage(self.image)
        self.imageLabel.setPixmap(self.pixmap)

    def snapShot(self):
        # Returns current image as QImage
        return self.image

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QtGui.QApplication(sys.argv)
    widget = OpenCVWidget()
    widget.show()
    app.exec_()

if __name__ == "__main__":
    main()
