# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_Demo2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(160, 200, 75, 23))
        self.ok_btn.setObjectName("ok_btn")
        self.api_input = QtWidgets.QTextEdit(Dialog)
        self.api_input.setGeometry(QtCore.QRect(160, 80, 141, 31))
        self.api_input.setObjectName("api_input")
        self.api_rows = QtWidgets.QLabel(Dialog)
        self.api_rows.setGeometry(QtCore.QRect(130, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.api_rows.setFont(font)
        self.api_rows.setObjectName("api_rows")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
        self.api_rows.setText(_translate("Dialog", "API"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Ui_Dialog()
    dlg.show()
    dlg.exec_()
    app.exit()


