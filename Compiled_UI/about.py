# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Files/about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(401, 117)
        About.setMinimumSize(QtCore.QSize(401, 117))
        About.setMaximumSize(QtCore.QSize(401, 117))
        self.buttonBox = QtWidgets.QDialogButtonBox(About)
        self.buttonBox.setGeometry(QtCore.QRect(10, 80, 381, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(0, 20, 401, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 401, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(About)
        self.buttonBox.clicked['QAbstractButton*'].connect(About.close)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.label.setText(_translate("About", "Qyoutube-dl created by Luke Zambella (https://github.com/lzambella)"))
        self.label_2.setText(_translate("About", "youtube-dl created by Ricardo Garcia (https://rg3.name/)"))

