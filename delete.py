
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from app import del_user,usr_validation


class Eliminate(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__()
        self.setupUi()
        self.parent = parent

    def goback(self):
        self.close()
        self.parent.show()

    def dele(self):
        userid=self.txt_UserID.toPlainText()

        if(usr_validation(userid)==True):
            del_user(userid)
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Information)
            infoBox.setText("Delete User")
            infoBox.setInformativeText("System Info")
            infoBox.setWindowTitle("Successful")
            infoBox.setDetailedText("SYSTEM INFO: User with ID "+userid+" deleted successfully")
            infoBox.setStandardButtons(QMessageBox.Ok)
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()

        else:
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Critical)
            infoBox.setText("Error")
            infoBox.setInformativeText("System Error")
            infoBox.setWindowTitle("ERROR")
            infoBox.setDetailedText("SYSTEM ERROR: User doesn't exist")
            infoBox.setStandardButtons(QMessageBox.Ok)
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()



    def setupUi(self):
        self.setObjectName("Delete")
        self.resize(345, 251)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_UserID = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_UserID.setGeometry(QtCore.QRect(10, 100, 311, 31))
        self.txt_UserID.setObjectName("txt_UserID")
        self.btn_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Delete.setGeometry(QtCore.QRect(40, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Delete.setFont(font)
        self.btn_Delete.setObjectName("btn_Delete")
        self.btn_Delete.clicked.connect(self.dele)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_Back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Back.setGeometry(QtCore.QRect(200, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Back.setFont(font)
        self.btn_Back.setObjectName("btn_Back")
        self.btn_Back.clicked.connect(self.goback)
        #self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        #self.setStatusBar(self.statusbar)

        self.setWindowTitle("Delete User")
        self.label.setText("Delete User")
        self.btn_Delete.setText("Delete")
        self.label_2.setText("User ID")
        self.btn_Back.setText("Back")

        self.show()

