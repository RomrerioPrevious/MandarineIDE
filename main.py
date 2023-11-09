from PyQt5 import QtCore, QtGui, QtWidgets
from bin.view.view import Ui_MainWindow


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "main":
    main()
