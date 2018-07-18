
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from app import showInfo, get_acc
from signin import sign_in

class ShowData(QtWidgets.QWidget):
    '''This class is used to initialize the Search Student Data Window'''
    def __init__(self, parent):
        super().__init__()
        self.setupUi()
        self.parent = parent

    def goback(self):
        '''This function is used to return to the previous window'''
        self.close()
        self.parent.show()

    def accessinf(self):
        '''This function is used to show the data related to de student id and to show the pop-ups'''
        id= self.txt_ID.toPlainText()
        account=showInfo(get_acc(id))
        if account != False:
            self.txt_Nombre.setPlainText(account.first_name)
            self.txt_Apellido.setPlainText(account.last_name)
            self.txt_Facultad.setPlainText(account.faculty)
            self.txt_Carrera.setPlainText(account.career)
            #print(account.account_ID)
        else:
            infoBox = QMessageBox()
            #print("Im here")
            infoBox.setIcon(QMessageBox.Critical)
            infoBox.setText("Error")
            infoBox.setInformativeText("Indentification Error")
            infoBox.setWindowTitle("ERROR")
            infoBox.setDetailedText("Account not in database")
            infoBox.setStandardButtons(QMessageBox.Ok)
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()
        return 0

    def setupUi(self):
        '''This function is used to set up the User Interface'''
        self.setObjectName("self")
        self.resize(502, 486)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_ID = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_ID.setGeometry(QtCore.QRect(30, 80, 291, 31))
        self.txt_ID.setObjectName("txt_ID")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_Search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Search.setGeometry(QtCore.QRect(340, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Search.setFont(font)
        self.btn_Search.setObjectName("btn_Search")
        self.btn_Search.clicked.connect(self.accessinf)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_Nombre = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_Nombre.setGeometry(QtCore.QRect(30, 170, 291, 31))
        self.txt_Nombre.setObjectName("txt_Nombre")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_Apellido = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_Apellido.setGeometry(QtCore.QRect(30, 240, 291, 31))
        self.txt_Apellido.setObjectName("txt_Apellido")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 290, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_Facultad = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_Facultad.setGeometry(QtCore.QRect(30, 310, 401, 31))
        self.txt_Facultad.setObjectName("txt_Facultad")
        self.txt_Carrera = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_Carrera.setGeometry(QtCore.QRect(30, 380, 401, 31))
        self.txt_Carrera.setObjectName("txt_Carrera")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 360, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_Back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Back.setGeometry(QtCore.QRect(190, 430, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Back.setFont(font)
        self.btn_Back.setObjectName("btn_Back")
        self.btn_Back.clicked.connect(self.goback)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 120, 501, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.setWindowTitle("Student Info")
        self.label.setText("Student ID")
        self.btn_Search.setText("Search")
        self.label_2.setText("Nombre")
        self.label_3.setText("Apellido")
        self.label_4.setText("Facultad")
        self.label_5.setText("Carrera")
        self.btn_Back.setText("Back")
        self.label_6.setText("Student Info")

        self.show()


