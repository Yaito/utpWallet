
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from app import new_user


class NewUser(QtWidgets.QWidget):
    '''This class is used to initialize the New User Window'''

    def __init__(self, parent):
        super().__init__()
        self.setupUi()
        self.parent = parent

    def goback(self):
        '''This function is used to return to the previous window'''
        self.close()
        self.parent.show()

    def nuevo(self):
        '''This function is used to call new_user() with parameters and to show the pop-ups'''
        user=self.txt_User.toPlainText()
        pas=self.txt_Pass.toPlainText()
        # new_user(test_usr,test_pass,test_type)
        if (self.cbx_Type.currentIndex()==0):
            ty=1
        elif (self.cbx_Type.currentIndex()==1):
            ty=2
        elif (self.cbx_Type.currentIndex()==2):
            ty=3
        var1=new_user(user,pas,ty)
        if(var1==False):
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Critical)
            infoBox.setText("Error")
            infoBox.setInformativeText("System Error")
            infoBox.setWindowTitle("ERROR")
            infoBox.setDetailedText("SYSTEM ERROR: Username already exist")
            infoBox.setStandardButtons(QMessageBox.Ok)
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()
        elif(var1!=False):
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Information)
            infoBox.setText("New User")
            infoBox.setInformativeText("System Info")
            infoBox.setWindowTitle("Successful")
            infoBox.setDetailedText("SYSTEM INFO: New user created successfully")
            infoBox.setStandardButtons(QMessageBox.Ok)
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()

        


    def setupUi(self):
        '''This function is used to set up the User Interface'''
        self.setObjectName("New")
        self.resize(366, 367)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_User = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_User.setGeometry(QtCore.QRect(10, 100, 311, 31))
        self.txt_User.setObjectName("txt_User")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_Pass = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_Pass.setGeometry(QtCore.QRect(10, 160, 311, 31))
        self.txt_Pass.setObjectName("txt_Pass")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cbx_Type = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_Type.setGeometry(QtCore.QRect(10, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbx_Type.setFont(font)
        self.cbx_Type.setObjectName("cbx_Type")
        self.cbx_Type.addItem("")
        self.cbx_Type.addItem("")
        self.cbx_Type.addItem("")
        self.btn_Back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Back.setGeometry(QtCore.QRect(210, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Back.setFont(font)
        self.btn_Back.setObjectName("btn_Back")
        self.btn_Back.clicked.connect(self.goback)
        self.btn_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Submit.setGeometry(QtCore.QRect(50, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Submit.setFont(font)
        self.btn_Submit.setObjectName("btn_Submit")
        self.btn_Submit.clicked.connect(self.nuevo)     
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")


        self.setWindowTitle("New User")
        self.label_2.setText("Username")
        self.label.setText("New User")
        self.label_3.setText("Password")
        self.label_4.setText("Type")
        self.cbx_Type.setItemText(0,"Admin")
        self.cbx_Type.setItemText(1, "Cashier")
        self.cbx_Type.setItemText(2, "Security")
        self.btn_Back.setText("Back")
        self.btn_Submit.setText("Submit")
        self.show()

