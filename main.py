import sys
from signin import Sign_in
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Sign_in()
    sys.exit(app.exec_())
