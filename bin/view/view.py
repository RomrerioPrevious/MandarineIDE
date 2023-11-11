from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow:
    def __init__(self, main_window: QtWidgets.QMainWindow):
        self.theme = self.get_theme()
        self.tabs = []
        self.layouts = []
        self.text_edits = {}
        self.translate = QtCore.QCoreApplication.translate
        self.main_window = main_window
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(1200, 800)
        self.main_window.setAutoFillBackground(False)
        self.main_window.setStyleSheet(f"background-color: rgb({self.theme['background']});\n"
                                       f"font: 9pt \"Droid Sans\";\n"
                                       f"color: rgb(209, 209, 209);\n"
                                       f"border-radius: 5px;")

        self.setupUi()

    def get_theme(self) -> {str: str}:
        return {
            "background": "40, 46, 57",
            "work_space": "48, 56, 65",
            "white": "255, 255, 255",
            "reserved_words": "235, 55, 55",
            "comparisons": "235, 55, 55",
            "special_characters": "255, 255, 255",
            "variable": "255, 255, 255",
            "function": "130, 239, 20",
            "class": "255, 255, 255"
        }

    def setupUi(self):
        self.create_basic_widgets()
        self.create_file_menu()

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.create_tabs()
        self.add_new_tab("1")
        self.add_new_tab("2")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.create_scroll_bar()

        self.main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        self.create_menu(self.main_window)
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def create_tabs(self):
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet(f"background-color: rgb({self.theme['background']});\n"
                                     f"alternate-background-color: rgb({self.theme['work_space']});\n"
                                     f"font: 10pt \"Droid Sans\";\n"
                                     f"color: rgb({self.theme['work_space']});")

    def create_basic_widgets(self):
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

    def create_scroll_bar(self):
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setStyleSheet("background-color: rgb(65, 71, 83);\n"
                                             f"selection-background-color: rgb({self.theme['background']});")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)

    def create_file_menu(self):
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

    def add_new_tab(self, name: str):
        if not len(self.tabs):
            self.tabWidget.setObjectName("tabWidget")
        else:
            self.tabWidget.addTab(self.tabs[-1], "")
        tab = QtWidgets.QWidget()
        tab.setObjectName(name)
        self.tabs.append(tab)

        horizontalLayout = QtWidgets.QHBoxLayout(tab)
        horizontalLayout.setObjectName(f"horizontalLayout")

        textEdit = QtWidgets.QTextEdit(tab)
        textEdit.setStyleSheet(f"background-color: rgb({self.theme['work_space']});\n"
                               f"color: rgb({self.theme['white']});")
        textEdit.setObjectName("textEdit")
        self.text_edits[name] = textEdit

        horizontalLayout.addWidget(textEdit)
        self.layouts.append(horizontalLayout)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs[0]),
                                  self.translate("MainWindow", name))

    def retranslateUi(self):
        self.main_window.setWindowTitle(self.translate("MainWindow", "Mandarine IDE"))

        self.treeWidget.setToolTip(self.translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.treeWidget.headerItem().setText(0, self.translate("MainWindow", "MandarinIDE"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, self.translate("MainWindow", "Main.py"))
        self.treeWidget.topLevelItem(1).setText(0, self.translate("MainWindow", "Text.md"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.menuMandarin.setTitle(self.translate("MainWindow", "File"))
        self.menuEdit.setTitle(self.translate("MainWindow", "Edit"))
        self.menuRun.setTitle(self.translate("MainWindow", "Run"))
        self.actionNew.setText(self.translate("MainWindow", "New Project"))
        self.actionOpen.setText(self.translate("MainWindow", "Open Project"))
        self.actionSave.setText(self.translate("MainWindow", "Save"))
        self.actionSave_as.setText(self.translate("MainWindow", "Save as"))
        self.actionUndo.setText(self.translate("MainWindow", "Undo"))
        self.actionCut.setText(self.translate("MainWindow", "Cut"))
        self.actionCopy.setText(self.translate("MainWindow", "Copy"))
        self.actionPaste.setText(self.translate("MainWindow", "Paste"))
        self.actionRun.setText(self.translate("MainWindow", "Run"))
        self.actionOpen_Folder.setText(self.translate("MainWindow", "Open Folder"))
