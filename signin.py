# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from app import sign_in
from transaction import Ui_MainWindow as bargain
from datashow import Ui_MainWindow as show_info
from management import Ui_MainWindow as admin
class Ui_MainWindow(object):

    def signin(self):
        users= self.txt_User.toPlainText()
        passwords= self.lineEdit_pass.text()
        cur_user= sign_in(users, passwords)
        if cur_user !=False:
            user_type= cur_user.type
            if(cur_user.type == 1):
                self.window= QtWidgets.QMainWindow()
                self.ui= admin()
                self.ui.setupUi(self.window)
                self.window.show()
                MainWindow.close()
                print("SYSTEM INFO: Successfully Logged in")
                print("Type 1 - Admin")
            elif(cur_user.type == 2):
                self.window= QtWidgets.QMainWindow()
                self.ui= bargain()
                self.ui.setupUi(self.window)
                self.window.show()
                MainWindow.close()
                print("SYSTEM INFO: Successfully Logged in")
                print("Type 2 - Cashier")
            elif(cur_user.type == 3):
                self.window= QtWidgets.QMainWindow()
                self.ui= show_info()
                self.ui.setupUi(self.window)
                self.window.show()
                MainWindow.close()
                print("SYSTEM INFO: Successfully Logged in")
                print("Type 3 - Security")
        else:
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Critical)
            infoBox.setText("Error")
            infoBox.setInformativeText("Log-in Error")
            infoBox.setWindowTitle("ERROR")
            infoBox.setDetailedText("Username or Password doesnt't match or doesn't Exist")
            infoBox.setStandardButtons(QMessageBox.Ok)
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()
            pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_User = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_User.setGeometry(QtCore.QRect(30, 140, 271, 31))
        self.txt_User.setObjectName("txt_User")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_Continue = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Continue.setGeometry(QtCore.QRect(140, 290, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Continue.setFont(font)
        self.btn_Continue.setObjectName("btn_Continue")
        self.btn_Continue.clicked.connect(self.signin)
        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(30, 210, 271, 31))
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setClearButtonEnabled(False)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign In"))
        self.label.setText(_translate("MainWindow", "Sign In"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.btn_Continue.setText(_translate("MainWindow", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

