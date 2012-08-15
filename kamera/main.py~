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

import signal
import sys

from PyQt4 import QtCore
from PyQt4 import QtGui
from mainwindow import MainWindow
import kamera_rc

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtGui.QApplication(sys.argv)

    app.setApplicationName("kamera")
    app.setOrganizationName("kamera")

    locale = QtCore.QLocale.system().name()
    translator = QtCore.QTranslator()
    translator.load(":/kamera_%s.qm" % locale)
    app.installTranslator(translator)

    mainWindow = MainWindow()
    mainWindow.show()

    return app.exec_()

if __name__ == "__main__":
    main()
