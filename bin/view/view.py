import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QWidget

from bin import Folder, File, Runner
from bin.handlers.folder_parser import Folder_parser
from bin.view.code_edit import CodeEdit


class MainWindow:
    def __init__(self, main_window: QtWidgets.QMainWindow):
        self.slashes = []
        self.theme = self.get_theme()
        self.tabs = []
        self.layouts = []
        self.text_edits = []
        self.directionsList = []
        self.directonsUsed = []
        self.paths = []
        self.slashes = []
        self.file_working = ""
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

        self.horizontalLayout.addWidget(self.tabWidget)

        self.main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        self.create_menu(self.main_window)
        self.retranslateUi()
        self.init_button_actions()
        self.tabWidget.setCurrentIndex(1)
        self.init_button_actions()
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

    def init_button_actions(self):
        self.actionOpen.triggered.connect(self.open)
        self.actionNew.triggered.connect(self.new)
        self.actionSave.triggered.connect(self.save)
        self.actionOpen_Folder.triggered.connect(self.open_folder)
        self.actionRun.triggered.connect(self.run)

    def add_new_tab(self, name: str, path: str):
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
        painter = CodeEdit(qedit=textEdit, theme=self.theme, path=path)
        painter.colorize()
        self.text_edits.append(textEdit)

        horizontalLayout.addWidget(textEdit)
        self.layouts.append(horizontalLayout)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs[0]),
                                  self.translate("MainWindow", name))

    def open(self):
        file_name = QFileDialog.getOpenFileName(self.centralwidget, 'Выберите файл', '')[0]
        self.paths.append(file_name)
        try:
            self.add_new_tab(file_name, file_name)
        except FileNotFoundError:
            print(f"File {file_name} not")

    def new(self):
        try:
            fname = QFileDialog.getExistingDirectory(self.centralwidget, "Выберите папку", ".")
            rootdir = os.getcwd()
            text, ok = QInputDialog.getText(QWidget(), 'Input Dialog', 'Ведите название файла:')
            if ok:
                file = open(f"{fname}/{str(text)}.py", "w")
                self.file_working = f"{rootdir}/{file.name}"
                self.text_edits[self.tabWidget.tabPosition()].setText(f"print('Hello World')")
        except PermissionError:
            return

    def save(self):
        edit: QtWidgets.QTextEdit = self.text_edits[self.tabWidget.tabPosition()]
        code = edit.toPlainText()
        with open(self.paths[self.tabWidget.tabPosition()], "w") as file:
            file.write(code)
        painter = CodeEdit(edit,
                           self.paths[self.tabWidget.tabPosition()],
                           self.theme)
        painter.colorize()
        code = edit.toPlainText()
        with open(self.paths[self.tabWidget.tabPosition()], "w") as file:
            file.write(code)

    def open_folder(self):
        self.count = 0
        fname = QFileDialog.getExistingDirectory(self.centralwidget, "Выберите папку", ".")
        self.check_all_files(fname)

    def check_all_files(self, fname):
        try:
            for file in os.listdir(fname)[::-1]:
                slashRootCount = fname.count("\\")
                self.slashes.append(slashRootCount)
                direction = os.path.join(fname, file)
                self.directionsList.append(str(direction))
                if os.path.isdir(direction):
                    self.check_all_files(direction)
            for el in self.directionsList:
                if el not in self.directonsUsed:
                    self.directonsUsed.append(el)
                    item = QtWidgets.QTreeWidgetItem(self.treeWidget)
                    _translate = QtCore.QCoreApplication.translate
                    self.treeWidget.topLevelItem(self.count).setText(0, _translate("MainWindow", (
                            "  " * self.slashes[self.directonsUsed.index(el)] + str(os.path.basename(el)))))
                    self.count += 1
        except WindowsError:
            return

    def run(self):
        try:
            Runner.run(Runner(self.file_working))
        except AttributeError:
            return

    def retranslateUi(self):
        self.main_window.setWindowTitle(self.translate("MainWindow", "Mandarine IDE"))

        self.treeWidget.setToolTip(self.translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.treeWidget.headerItem().setText(0, self.translate("MainWindow", "MandarinIDE"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.menuMandarin.setTitle(self.translate("MainWindow", "File"))
        self.menuRun.setTitle(self.translate("MainWindow", "Run"))
        self.actionNew.setText(self.translate("MainWindow", "New Project"))
        self.actionOpen.setText(self.translate("MainWindow", "Open File"))
        self.actionSave.setText(self.translate("MainWindow", "Save"))
        self.actionSave_as.setText(self.translate("MainWindow", "Save as"))
        self.actionRun.setText(self.translate("MainWindow", "Run"))
        self.actionOpen_Folder.setText(self.translate("MainWindow", "Open Folder"))
