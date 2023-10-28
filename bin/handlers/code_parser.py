from bin.models.tokens import *


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
        words = line.replace("\n", "").split()
        tokens = [Token.token_fabric(words[0], None)]
        for i in range(1, len(words), 1):
            word = words[i]
            if words[i - 1] in ["def", "class"]:
                tokens.append(Token.token_fabric(word, words[i - 1]))
            else:
                tokens.append(Token.token_fabric(word, None))
        return tokens
