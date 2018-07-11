# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'management.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 278)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_New = QtWidgets.QPushButton(self.centralwidget)
        self.btn_New.setGeometry(QtCore.QRect(130, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_New.setFont(font)
        self.btn_New.setObjectName("btn_New")
        self.btn_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Delete.setGeometry(QtCore.QRect(130, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Delete.setFont(font)
        self.btn_Delete.setObjectName("btn_Delete")
        self.btn_Delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Delete_2.setGeometry(QtCore.QRect(130, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Delete_2.setFont(font)
        self.btn_Delete_2.setObjectName("btn_Delete_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User management"))
        self.btn_New.setText(_translate("MainWindow", "New User"))
        self.btn_Delete.setText(_translate("MainWindow", "Delete User"))
        self.btn_Delete_2.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "User management"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

