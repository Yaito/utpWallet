
from PyQt5 import QtCore, QtGui, QtWidgets
from app import Payment, balance_check
from app import Topup
from PyQt5.QtWidgets import QMessageBox
from app import showInfo, get_acc
import sys


class MoneyWindow(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__()
        self.setupUi()
        self.parent = parent

    def goback(self):
        self.close()
        self.parent.show()

    def tran(self):
        if (self.cbx_Type.currentIndex()==0):
            #Topup(get_acc(test_id),topup_credit)
            amount=float(self.txt_ID_2.toPlainText())
            #print(amount)
            studid=self.txt_ID.toPlainText()

            if(get_acc(studid)!=False):
                Topup(get_acc(studid),amount)
                infoBox = QMessageBox()
                infoBox.setIcon(QMessageBox.Information)
                infoBox.setText("Top-Up")
                infoBox.setInformativeText("Successful Top-up")
                infoBox.setWindowTitle("Confirmation")
                infoBox.setDetailedText("Top-up Transaction Successfully Done\n ${0:.2f} added to your account".format(amount))
                infoBox.setStandardButtons(QMessageBox.Ok)
                infoBox.setEscapeButton(QMessageBox.Close)
                infoBox.exec_()

            else:
                infoBox = QMessageBox()
                infoBox.setIcon(QMessageBox.Critical)
                infoBox.setText("Error")
                infoBox.setInformativeText("Indentification Error")
                infoBox.setWindowTitle("ERROR")
                infoBox.setDetailedText("Account not in database")
                infoBox.setStandardButtons(QMessageBox.Ok)
                infoBox.setEscapeButton(QMessageBox.Close)
                infoBox.exec_()

        elif(self.cbx_Type.currentIndex()==1):
            amount=float(self.txt_ID_2.toPlainText())
            studid=self.txt_ID.toPlainText()

            if(balance_check(get_acc(studid),amount))==True:
                Payment(get_acc(studid),amount)
                infoBox = QMessageBox()
                infoBox.setIcon(QMessageBox.Information)
                infoBox.setText("Payment")
                infoBox.setInformativeText("Successful Payment")
                infoBox.setWindowTitle("Confirmation")
                infoBox.setDetailedText("Payment Transaction Successfully Done\n ${0:.2f} deducted from your account".format(amount))
                infoBox.setStandardButtons(QMessageBox.Ok)
                infoBox.setEscapeButton(QMessageBox.Close)
                infoBox.exec_()               

            else:
                infoBox = QMessageBox()
                infoBox.setIcon(QMessageBox.Critical)
                infoBox.setText("Error")
                infoBox.setInformativeText("Payment Error")
                infoBox.setWindowTitle("ERROR")
                infoBox.setDetailedText("Payment Error: Not Enough Money")
                infoBox.setStandardButtons(QMessageBox.Ok)
                infoBox.setEscapeButton(QMessageBox.Close)
                infoBox.exec_()               


            


    def setupUi(self):
        self.setObjectName("transaction")
        self.resize(364, 295)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 0, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cbx_Type = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_Type.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbx_Type.setFont(font)
        self.cbx_Type.setObjectName("cbx_Type")
        self.cbx_Type.addItem("")
        self.cbx_Type.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_ID = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_ID.setGeometry(QtCore.QRect(10, 170, 331, 31))
        self.txt_ID.setObjectName("txt_ID")
        self.btn_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Exit.setGeometry(QtCore.QRect(210, 230, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Exit.setFont(font)
        self.btn_Exit.setObjectName("btn_Exit")
        self.btn_Exit.clicked.connect(self.goback)
        self.btn_Ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Ok.setGeometry(QtCore.QRect(70, 230, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Ok.setFont(font)
        self.btn_Ok.setObjectName("btn_Ok")
        self.btn_Ok.clicked.connect(self.tran)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_ID_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_ID_2.setGeometry(QtCore.QRect(140, 100, 201, 31))
        self.txt_ID_2.setObjectName("txt_ID_2")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        
        self.setWindowTitle("Transaction")
        self.label.setText("Transaction")
        self.label_3.setText("Type")
        self.cbx_Type.setItemText(0, "Top-up")
        self.cbx_Type.setItemText(1, "Payment")
        self.label_4.setText("Student ID")
        self.btn_Exit.setText("Exit")
        self.btn_Ok.setText("OK")
        self.label_5.setText("Amount")
        self.show()
