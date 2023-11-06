from bin.models.tokens import *
from bin.handlers.code_parser.token_creater import TokenCreator


class CodeParser:
    def __init__(self, path: str):
        self.path = path
        self.scope = {"Function": set(),
                      "Variable": set(),
                      "Class": set()}

    def parse_code(self):
        with open(self.path, mode="r", encoding="UTF8") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                yield self.parse_code_from_line(line)

    def parse_code_from_line(self, line: str) -> [Token]:
        words = CodeParser.split(line)
        tokens = [TokenCreator.token_fabric(words[0], None)]
        for i in range(1, len(words), 1):
            word = words[i]
            if words[i - 1] in ["def", "class"]:
                token = TokenCreator.token_fabric(word, words[i - 1])
            else:
                token = TokenCreator.token_fabric(word)
            tokens.append(token)
            if token.type.name in self.scope.keys():
                self.scope[token.type.name].add(token)
        return tokens

    @staticmethod
    def split(line: str) -> [str]:
        result = []
        special = TokenTypeList.get_token_types()["Special characters"].words
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
