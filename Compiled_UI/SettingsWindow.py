# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Files/settings.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName("SettingDialog")
        SettingDialog.resize(441, 621)
        SettingDialog.setMinimumSize(QtCore.QSize(0, 0))
        SettingDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget = QtWidgets.QTabWidget(SettingDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 421, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 391, 321))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 371, 21))
        self.label_3.setToolTip("")
        self.label_3.setObjectName("label_3")
        self.age_limit = QtWidgets.QLineEdit(self.groupBox_3)
        self.age_limit.setGeometry(QtCore.QRect(120, 20, 71, 20))
        self.age_limit.setObjectName("age_limit")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 371, 21))
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.min_views = QtWidgets.QLineEdit(self.groupBox_3)
        self.min_views.setGeometry(QtCore.QRect(120, 50, 71, 20))
        self.min_views.setObjectName("min_views")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 371, 21))
        self.label_5.setToolTip("")
        self.label_5.setObjectName("label_5")
        self.max_views = QtWidgets.QLineEdit(self.groupBox_3)
        self.max_views.setGeometry(QtCore.QRect(120, 80, 71, 20))
        self.max_views.setObjectName("max_views")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 371, 21))
        self.label_6.setToolTip("")
        self.label_6.setObjectName("label_6")
        self.record_file = QtWidgets.QLineEdit(self.groupBox_3)
        self.record_file.setGeometry(QtCore.QRect(120, 110, 71, 20))
        self.record_file.setObjectName("record_file")
        self.select_record_file_button = QtWidgets.QPushButton(self.groupBox_3)
        self.select_record_file_button.setGeometry(QtCore.QRect(200, 110, 31, 21))
        self.select_record_file_button.setObjectName("select_record_file_button")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 521))
        self.groupBox.setObjectName("groupBox")
        self.overwriteCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.overwriteCheckBox.setGeometry(QtCore.QRect(10, 20, 371, 18))
        self.overwriteCheckBox.setObjectName("overwriteCheckBox")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.quietCheckBox = QtWidgets.QCheckBox(self.tab_5)
        self.quietCheckBox.setGeometry(QtCore.QRect(10, 10, 371, 18))
        self.quietCheckBox.setObjectName("quietCheckBox")
        self.ignoreCheckBox = QtWidgets.QCheckBox(self.tab_5)
        self.ignoreCheckBox.setGeometry(QtCore.QRect(10, 70, 371, 18))
        self.ignoreCheckBox.setObjectName("ignoreCheckBox")
        self.warningsCheckBox = QtWidgets.QCheckBox(self.tab_5)
        self.warningsCheckBox.setGeometry(QtCore.QRect(10, 50, 371, 18))
        self.warningsCheckBox.setObjectName("warningsCheckBox")
        self.verboseCheckBox = QtWidgets.QCheckBox(self.tab_5)
        self.verboseCheckBox.setGeometry(QtCore.QRect(10, 30, 371, 18))
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.tabWidget.addTab(self.tab_5, "")
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingDialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 590, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(SettingDialog)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.rejected.connect(SettingDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

    def retranslateUi(self, SettingDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingDialog.setWindowTitle(_translate("SettingDialog", "Settings"))
        self.groupBox_3.setTitle(_translate("SettingDialog", "Video Settings"))
        self.label_3.setText(_translate("SettingDialog", "Age limit: "))
        self.label_4.setText(_translate("SettingDialog", "Minimum views:"))
        self.label_5.setText(_translate("SettingDialog", "Maximum views: "))
        self.label_6.setText(_translate("SettingDialog", "Save files to:"))
        self.select_record_file_button.setText(_translate("SettingDialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SettingDialog", "Video Selection"))
        self.groupBox.setTitle(_translate("SettingDialog", "Filesystem Options"))
        self.overwriteCheckBox.setText(_translate("SettingDialog", "Prevent file overwrite"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("SettingDialog", "Filesystem Options"))
        self.quietCheckBox.setText(_translate("SettingDialog", "Quiet mode"))
        self.ignoreCheckBox.setText(_translate("SettingDialog", "Ignore errors"))
        self.warningsCheckBox.setText(_translate("SettingDialog", "No warnings"))
        self.verboseCheckBox.setText(_translate("SettingDialog", "Verbose Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("SettingDialog", "Verbosity"))

