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

from PyQt4.QtCore import QDir
from PyQt4.QtCore import QVariant

IMAGE_FORMAT = QVariant("jpg")
VIDEO_FLIP_LEFT_RIGHT = QVariant(True)
VIDEO_FLIP_TOP_BOTTOM = QVariant(False)
IMAGE_DIRECTORY = QVariant(QDir.homePath())
