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


import sys,httplib,socket
from PyQt4 import QtCore,QtGui
from mainwindow import Ui_MainWindow
from about import Ui_Dialog as Ui_About

class About_Window(QtGui.QDialog, Ui_About):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.setWindowTitle("About")
		
class MainWindow(QtGui.QMainWindow,Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.setWindowTitle("HttpMethod Finder")
		self.connectActions()
		QtCore.QObject.connect(self.findmethods,QtCore.SIGNAL("clicked()"),self.findmethods_function)
		self.Ui_About=About_Window()
	def findmethods_function(self):
		try:
			host = unicode(self.server_text.text())
			port = int(unicode(self.port_text.text()))
			
			methods = ["GET","POST","HEAD","TRACE","PUT","DELETE","CONNECT","LINK",
					   "CHECKOUT","SHOWMETHOD","UNLINK","CHECKIN","TEXTSEARCH",
				       "SPACEJUMP","SEARCH"]
			
			self.result.append("Host Name : %s\n" % host)   
			for test in range(len(methods)):
				conn=httplib.HTTPConnection(host,port)
				conn.request(methods[test],"/")
				res=conn.getresponse()
				self.result.append("%s = %s %s" % (methods[test],res.status,res.reason))
			self.label3.setText("Finished!")
			self.result.append("\n-------------------------------------------------------------")
		except ValueError:
			self.label3.setText("Port should be an integer")
		except socket.gaierror:
			self.label3.setText("Host couldn't find")
	def connectActions(self):
		self.actionExit.triggered.connect(QtGui.qApp.quit)
		self.actionAbout.triggered.connect(self.about_function)
	def about_function(self):
		self.Ui_About.exec_()
def main():
	app = QtGui.QApplication(sys.argv)
	httpmethod = MainWindow()
	httpmethod.show()
	return app.exec_()
	
if __name__ == "__main__":
	main()