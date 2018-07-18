
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QMainWindow
from app import sign_in
from management import Manejo
from datashow import ShowData
from transaction import MoneyWindow

class Sign_in(QMainWindow):
    '''This class is used to initialize the Sign in Window'''

    def __init__(self):
        super().__init__()
        self.setupUi()

    def usignin(self):
        '''This function is used to validate the user and show them the appropiate window'''
        users = self.txt_User.toPlainText()
        passwords = self.lineEdit_pass.text()
        cur_user = sign_in(users, passwords)
        if cur_user != False:
            user_type = cur_user.type
            if(cur_user.type == 1):

                self.manageView = Manejo(self)
                self.hide()

                print("SYSTEM INFO: Successfully Logged in")
                print("Type 1 - Admin")
            elif(cur_user.type == 2):
                self.show_data = MoneyWindow(self)
                self.hide()
                
                print("SYSTEM INFO: Successfully Logged in")
                print("Type 2 - Cashier")
            elif(cur_user.type == 3):
                self.show_data = ShowData(self)
                self.hide()
                print("SYSTEM INFO: Successfully Logged in")
                print("Type 3 - Security")
        else:
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Critical)
            infoBox.setText("Error")
            infoBox.setInformativeText("Log-in Error")
            infoBox.setWindowTitle("ERROR")
            infoBox.setDetailedText(
                "Username or Password doesnt't match or doesn't Exist")
            infoBox.setStandardButtons(QMessageBox.Ok)
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()
            pass

    def setupUi(self):
        '''This function is used to set up the User Interface'''
        self.setObjectName("Signin")
        self.resize(414, 395)
        self.centralwidget = QtWidgets.QWidget(self)
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
        self.btn_Continue.clicked.connect(self.usignin)
        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(30, 210, 271, 31))
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setClearButtonEnabled(False)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.setWindowTitle("Sign In")
        self.label.setText("Sign In")
        self.label_2.setText("Username")
        self.label_3.setText("Password")
        self.btn_Continue.setText("Continue")
        self.show()
