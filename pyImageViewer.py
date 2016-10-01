# -*- coding: utf-8 -*-

import sys
import os
import subprocess
from PyQt4 import QtCore
from PyQt4 import QtGui


class Viewer(QtGui.QMainWindow):
    def __init__(self):
        super(Viewer, self).__init__()
        self.initUI()

    def initUI(self):

        self.w = QtGui.QWidget()
        self.w.setWindowTitle('Iris Reflection Removal')
        self.w.setWindowIcon(QtGui.QIcon('./icon.png'))

        self.fpath = './img/'

        self.vbox = QtGui.QVBoxLayout()

        self.hbox1 = QtGui.QHBoxLayout()
        self.addPixArea()

        self.hbox2 = QtGui.QHBoxLayout()
        self.addButton()

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)

        self.w.setLayout(self.vbox)
        self.setCentralWidget(self.w)

        self.setGeometry(100, 100, 512, 512) 

        print "load from:", self.fpath  


    def addPixArea(self):
        self.pixlabel = QtGui.QLabel(self)
        self.pixmap = QtGui.QPixmap(self.fpath + "img1.png")
        self.pixlabel.setPixmap(self.pixmap)
        self.pixlabel.resize(self.pixmap.size())

        self.hbox1.addWidget(self.pixlabel)

    def addButton(self):
        self.b1=QtGui.QRadioButton(u"img1")
        self.b2=QtGui.QRadioButton(u"img2")
        self.b3=QtGui.QRadioButton(u"img3")

        self.b1.toggled.connect(self.b1_clicked) 
        self.b2.toggled.connect(self.b2_clicked) 
        self.b3.toggled.connect(self.b3_clicked) 

        self.hbox2.addWidget(self.b1)
        self.hbox2.addWidget(self.b2)
        self.hbox2.addWidget(self.b3)

    def b1_clicked(self, enabled):
        if enabled:
            self.pixmap = QtGui.QPixmap( self.fpath + "img1.png")
            self.pixlabel.setPixmap(self.pixmap)
            self.pixlabel.resize(self.pixmap.size())

    def b2_clicked(self, enabled):
        if enabled:
            self.pixmap = QtGui.QPixmap( self.fpath + "img2.png")
            self.pixlabel.setPixmap(self.pixmap)
            self.pixlabel.resize(self.pixmap.size())

    def b3_clicked(self, enabled):
        if enabled:
            self.pixmap = QtGui.QPixmap( self.fpath + "img3.png")
            self.pixlabel.setPixmap(self.pixmap)
            self.pixlabel.resize(self.pixmap.size())

if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)

    viewer = Viewer()
    viewer.show()
    sys.exit(app.exec_())
