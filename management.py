
from PyQt5 import QtCore, QtGui, QtWidgets
from delete import Eliminate
from new import NewUser

class Manejo(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__()
        self.setupUi()
        self.parent = parent

    def graphic(self):
        pass
        
    def gocreate(self):
        self.manageview = NewUser(self)
        self.hide()

    def godelete(self):
        self.manageview = Eliminate(self)
        self.hide()

    def goback(self):
        self.close()
        self.parent.show()

    def setupUi(self):
        self.setObjectName("Manejo")
        self.resize(423, 330)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_New = QtWidgets.QPushButton(self.centralwidget)
        self.btn_New.setGeometry(QtCore.QRect(160, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_New.setFont(font)
        self.btn_New.setObjectName("btn_New")
        self.btn_New.clicked.connect(self.gocreate)
        self.btn_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Delete.setGeometry(QtCore.QRect(160, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Delete.setFont(font)
        self.btn_Delete.setObjectName("btn_Delete")
        self.btn_Delete.clicked.connect(self.godelete)
        self.btn_Delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Delete_2.setGeometry(QtCore.QRect(160, 250, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Delete_2.setFont(font)
        self.btn_Delete_2.setObjectName("btn_Delete_2")
        self.btn_Delete_2.clicked.connect(self.goback)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Showgraph = QtWidgets.QPushButton(self.centralwidget)
        self.Showgraph.setGeometry(QtCore.QRect(160, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Showgraph.setFont(font)
        self.Showgraph.setObjectName("Showgraph")
        self.btn_Delete_2.clicked.connect(self.graphic)
        #self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.setWindowTitle("User management")
        self.btn_New.setText("New User")
        self.btn_Delete.setText("Delete User")
        self.btn_Delete_2.setText("Back")
        self.label.setText("User management")
        self.Showgraph.setText("Show Graph")
        self.show()

