from bin.models.tokens import *
from bin.handlers.code_parser.token_creater import TokenCreator


class CodeParser:
    def __init__(self, path: str):
        self.path = path
        self.scope = {"function": set(),
                      "variable": set(),
                      "class": set()}

    def parse_code(self) -> [Token]:
        with open(self.path, mode="r", encoding="UTF8") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                yield self.parse_code_from_line(line)

    def parse_code_from_line(self, line: str) -> [Token]:
        words = CodeParser.split(line)
        tokens = [TokenCreator.token_fabric(words[0])]
        if len(words) != 1:
            tokens.append(TokenCreator.token_fabric(words[1]))
        for i in range(2, len(words), 1):
            word = words[i]
            token = TokenCreator.token_fabric(word)
            if words[i - 2] in ["def", "class"]:
                token = TokenCreator.token_fabric(word, words[i - 2])
            elif i + 1 != len(words):
                if words[i + 1] == "(":
                    token = TokenCreator.token_fabric(word, "def")
            tokens.append(token)
            if token.type.name in self.scope.keys():
                self.scope[token.type.name].add(token)
        return tokens

    @staticmethod
    def split(line: str) -> [str]:
        result = []
        special = TokenTypeList.get_token_types()["special_characters"].words
        word = ""
        for char in line:
            if char in special:
                if word:
                    result.append(word)
                result.append(char)
                word = ""
            else:
                word += char
        if word:
            result.append(word)
        return result
