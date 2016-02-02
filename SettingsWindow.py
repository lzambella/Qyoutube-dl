# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 112)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 461, 20))
        self.label.setToolTip("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 321, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 30, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 80, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.buttonCancel = QtWidgets.QPushButton(Dialog)
        self.buttonCancel.setGeometry(QtCore.QRect(400, 80, 75, 23))
        self.buttonCancel.setObjectName("buttonCancel")

        self.retranslateUi(Dialog)
        self.buttonCancel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setWhatsThis(_translate("Dialog", "<html><head/><body><p>A Youtube data API key is required for more advanced features.</p></body></html>"))
        self.label.setText(_translate("Dialog", "API Key: "))
        self.pushButton.setText(_translate("Dialog", "Set Key"))
        self.pushButton_2.setText(_translate("Dialog", "Apply"))
        self.pushButton_3.setText(_translate("Dialog", "Ok"))
        self.buttonCancel.setText(_translate("Dialog", "Cancel"))

