from PyQt5 import QtCore, QtGui, QtWidgets
from bin.view.view import MainWindow
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
