#!/usr/bin/python3
#coding:utf-8

from PyQt5.QtWidgets import *
import sys
import wxPython


class Querry(QDialog):
    def __init__(self, parent=None):
        super(Querry, self).__init__(parent)
        usr = QLabel("所要查询的接口：")
        self.usrLineEdit = QLineEdit()

        gridLayout = QGridLayout()
        gridLayout.addWidget(usr, 0, 0, 1, 1)
        gridLayout.addWidget(self.usrLineEdit, 0, 1, 1, 3)

        okBtn = QPushButton("确定")
        cancelBtn = QPushButton("取消")
        btnLayout = QHBoxLayout()

        btnLayout.setSpacing(60)
        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(cancelBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40, 40, 40, 40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)

        self.setLayout(dlgLayout)
        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.reject)
        self.setWindowTitle("登录")
        self.resize(300, 200)

    def accept(self):
        if self.usrLineEdit.text().strip() == "1":
            super(Querry, self).accept()
        else:
            QMessageBox.warning(self,"警告","该接口不存在，重新输入！",QMessageBox.Yes)
            self.usrLineEdit.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Querry()
    dlg.show()
    dlg.exec_()
    print("TEST OK")
    app.exit()

