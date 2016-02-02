# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName("SettingDialog")
        SettingDialog.resize(480, 112)
        SettingDialog.setMinimumSize(QtCore.QSize(480, 112))
        SettingDialog.setMaximumSize(QtCore.QSize(480, 112))
        self.label = QtWidgets.QLabel(SettingDialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 461, 20))
        self.label.setToolTip("")
        self.label.setObjectName("label")
        self.keyLine = QtWidgets.QLineEdit(SettingDialog)
        self.keyLine.setGeometry(QtCore.QRect(60, 30, 321, 20))
        self.keyLine.setObjectName("keyLine")
        self.setKeyButton = QtWidgets.QPushButton(SettingDialog)
        self.setKeyButton.setGeometry(QtCore.QRect(390, 30, 81, 23))
        self.setKeyButton.setObjectName("setKeyButton")
        self.applyButton = QtWidgets.QPushButton(SettingDialog)
        self.applyButton.setGeometry(QtCore.QRect(320, 80, 75, 23))
        self.applyButton.setObjectName("applyButton")
        self.okButton = QtWidgets.QPushButton(SettingDialog)
        self.okButton.setGeometry(QtCore.QRect(400, 80, 75, 23))
        self.okButton.setObjectName("okButton")

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

