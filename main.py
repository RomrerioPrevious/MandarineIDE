from PyQt5 import QtCore, QtGui, QtWidgets
from bin.view.view import MainWindow
import sys
import os


def main():
    path: str = __file__
    path = path.rstrip("main.py")
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)
    ui.setupUi()
    ui.main_window.setWindowIcon(QtGui.QIcon(path + "resources/assets/mandarin.ico"))
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
