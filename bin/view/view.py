from PyQt5 import QtCore, QtGui, QtWidgets
import json


class MainWindow:
    def __init__(self, main_window: QtWidgets.QMainWindow):
        self.theme = self.get_theme()
        main_window.setObjectName("MainWindow")
        main_window.resize(857, 612)
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet(f"background-color: rgb({self.theme['background']});\n"
                                  f"font: 9pt \"Droid Sans\";\n"
                                  f"color: rgb(209, 209, 209);\n"
                                  f"border-radius: 5px;")

        self.setupUi(main_window)

    def get_theme(self) -> {str: str}:
        return {
            "background": "40, 46, 57",
            "work_space": "48, 56, 65",
            "white": "255, 255, 255"
        }

    def setupUi(self, main_window):
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        self.horizontalLayout.setObjectName("horizontalLayout")

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())

        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setAutoFillBackground(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setStyleSheet(f"background-color: rgb({self.theme['background']});\n"
                                      f"alternate-background-color: rgb({self.theme['work_space']});\n"
                                      f"font: 10pt \"Droid Sans\";\n"
                                      f"color: rgb({self.theme['white']});")

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet(f"background-color: rgb({self.theme['background']});\n"
                                     f"alternate-background-color: rgb({self.theme['work_space']});\n"
                                     f"font: 10pt \"Droid Sans\";\n"
                                     f"color: rgb({self.theme['work_space']});")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setStyleSheet(f"background-color: rgb({self.theme['work_space']});\n"
                                    f"color: rgb({self.theme['white']});")
        self.textEdit.setObjectName("textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setStyleSheet(f"background-color: rgb({self.theme['work_space']});\n"
                                      f"color: rgb({self.theme['white']});")
        self.textEdit_2.setObjectName("textEdit_2")

        self.horizontalLayout_3.addWidget(self.textEdit_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setStyleSheet("background-color: rgb(65, 71, 83);\n"
                                             f"selection-background-color: rgb({self.theme['background']});")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.horizontalLayout.addWidget(self.verticalScrollBar)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.create_menu(main_window)
        self.retranslateUi(main_window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def create_menu(self, main_window):
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 24))
        self.menubar.setObjectName("menubar")
        self.menuMandarin = QtWidgets.QMenu(self.menubar)
        self.menuMandarin.setObjectName("menuMandarin")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuBinds")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")

        main_window.setMenuBar(self.menubar)

        self.actionNew = QtWidgets.QAction(main_window)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(main_window)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(main_window)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(main_window)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionUndo = QtWidgets.QAction(main_window)
        self.actionUndo.setObjectName("actionUndo")
        self.actionCut = QtWidgets.QAction(main_window)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(main_window)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(main_window)
        self.actionPaste.setObjectName("actionPaste")
        self.actionRun = QtWidgets.QAction(main_window)
        self.actionRun.setObjectName("actionRun")
        self.actionOpen_Folder = QtWidgets.QAction(main_window)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.menuMandarin.addAction(self.actionNew)
        self.menuMandarin.addAction(self.actionOpen)
        self.menuMandarin.addAction(self.actionOpen_Folder)
        self.menuMandarin.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuRun.addAction(self.actionRun)
        self.menubar.addAction(self.menuMandarin.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mandarine IDE"))

        self.treeWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "MandarinIDE"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Main.py"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Text.md"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

        self.menuMandarin.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.actionNew.setText(_translate("MainWindow", "New Project"))
        self.actionOpen.setText(_translate("MainWindow", "Open Project"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder"))
