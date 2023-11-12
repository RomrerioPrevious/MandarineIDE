from PyQt5.QtGui import QColor, QTextCursor
from PyQt5.QtWidgets import QTextEdit, QComboBox
from bin.handlers.code_parser import CodeParser
from bin.models.tokens import *
from bin.handlers.hints import HintParser


class CodeEdit:
    def __init__(self, qedit: QTextEdit, path: str, theme: {str: str}):
        self.code_parser = CodeParser(path)
        self.qedit = qedit
        self.theme = theme
        self.position = 0
        self.document = self.qedit.document()
        self.cursor = QTextCursor(self.document)

    def hints_context_menu(self):
        hints = HintParser(self.code_parser)
        combo_box = QComboBox()
        combo_box.addItems(
            list(map(lambda hint: hint.inserted_code, hints.get_hints("i")))
        )
        combo_box.setEditable(True)
        return combo_box

    def colorize(self):
        self.cursor.setPosition(0)
        self.cursor.select(self.cursor.Document)
        self.cursor.removeSelectedText()
        with open(self.code_parser.path, "r") as file:
            code = file.read()
        self.cursor.insertText(code)
        for tokens in self.code_parser.parse_code():
            self.colorize_string(tokens)

    def colorize_string(self, tokens: [Token]):
        for token in tokens:
            color = self.theme[token.type.name]
            color = list(map(lambda num: int(num), color.split(", ")))
            self.colorize_word(QColor(*color), token)

    def colorize_word(self, color: QColor, token: Token):
        for i in range(len(token.name)):
            self.cursor.setPosition(self.position + i)
            self.cursor.setPosition(self.position + i + 1, self.cursor.KeepAnchor)

            format = self.cursor.charFormat()
            format.setForeground(color)
            self.cursor.setCharFormat(format)
        self.position += len(token.name)
