from PyQt5.QtWidgets import QTextEdit
from bin.handlers.code_parser import CodeParser
from bin.models.tokens import *


class Painter:
    def __init__(self, qedit: QTextEdit, path: str, theme: {str: str}):
        self.code_parser = CodeParser(path)
        self.qedit = qedit

    def parse_code(self):
        for tokens in self.code_parser.parse_code():
            ...

    def colorize(self, tokens: [Token]):
        document = self.qedit.document()
        for token in tokens:
            token.type
