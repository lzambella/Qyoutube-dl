# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Wed Feb  3 12:21:47 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName("SettingDialog")
        SettingDialog.resize(480, 283)
        SettingDialog.setMinimumSize(QtCore.QSize(480, 112))
        SettingDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label = QtWidgets.QLabel(SettingDialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 461, 20))
        self.label.setToolTip("")
        self.label.setObjectName("label")
        self.keyLine = QtWidgets.QLineEdit(SettingDialog)
        self.keyLine.setGeometry(QtCore.QRect(70, 30, 311, 20))
        self.keyLine.setObjectName("keyLine")
        self.setKeyButton = QtWidgets.QPushButton(SettingDialog)
        self.setKeyButton.setGeometry(QtCore.QRect(390, 30, 81, 23))
        self.setKeyButton.setObjectName("setKeyButton")
        self.applyButton = QtWidgets.QPushButton(SettingDialog)
        self.applyButton.setGeometry(QtCore.QRect(320, 250, 75, 23))
        self.applyButton.setObjectName("applyButton")
        self.okButton = QtWidgets.QPushButton(SettingDialog)
        self.okButton.setGeometry(QtCore.QRect(400, 250, 75, 23))
        self.okButton.setObjectName("okButton")
        self.label_2 = QtWidgets.QLabel(SettingDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.directoryLine = QtWidgets.QLineEdit(SettingDialog)
        self.directoryLine.setGeometry(QtCore.QRect(150, 60, 231, 22))
        self.directoryLine.setObjectName("directoryLine")
        self.selectDirButton = QtWidgets.QPushButton(SettingDialog)
        self.selectDirButton.setGeometry(QtCore.QRect(390, 60, 80, 22))
        self.selectDirButton.setObjectName("selectDirButton")

        self.retranslateUi(SettingDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

    def retranslateUi(self, SettingDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingDialog.setWindowTitle(_translate("SettingDialog", "Settings"))
        self.label.setWhatsThis(_translate("SettingDialog", "<html><head/><body><p>A Youtube data API key is required for more advanced features.</p></body></html>"))
        self.label.setText(_translate("SettingDialog", "API Key: "))
        self.setKeyButton.setText(_translate("SettingDialog", "Set Key"))
        self.applyButton.setText(_translate("SettingDialog", "Apply"))
        self.okButton.setText(_translate("SettingDialog", "Ok"))
        self.label_2.setText(_translate("SettingDialog", "Download Directory:"))
        self.selectDirButton.setText(_translate("SettingDialog", "..."))

