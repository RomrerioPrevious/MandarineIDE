from bin.models.tokens import *
from bin.handlers.code_parser.token_creater import TokenCreator


class CodeParser:
    def __init__(self, path: str):
        self.path = path

    def parse_code(self) -> [[Token]]:
        tokens = []
        with open(self.path, mode="r", encoding="UTF8") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                tokens.append(self.parse_code_from_line(line))
        return tokens

    @staticmethod
    def parse_code_from_line(line: str) -> [Token]:
        words = CodeParser.split(line)
        tokens = [TokenCreator.token_fabric(words[0], None)]
        for i in range(1, len(words), 1):
            word = words[i]
            if words[i - 1] in ["def", "class"]:
                tokens.append(TokenCreator.token_fabric(word, words[i - 1]))
            else:
                tokens.append(TokenCreator.token_fabric(word, None))
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
