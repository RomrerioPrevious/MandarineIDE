from bin.models import Hint, TokenTypeList, TokenType
from bin.handlers.code_parser import CodeParser


class HintParser:
    def __init__(self, code_parser: CodeParser):
        self.scope = code_parser.scope
        self.all_hint = []
        for token_type in TokenTypeList.get_token_types().items():
            if token_type[1].words is None:
                continue
            self.all_hint.append(token_type[1].words)

    def get_hints(self, word: str) -> [Hint]:
        result = [*self.get_python_hints(word),
                  *self.get_file_hints(word),
                  ]
        return result

    def get_python_hints(self, word: str) -> [Hint]:
        return self.return_matches(self.all_hint, word, "method")

    def get_file_hints(self, word: str) -> [Hint]:
        result = []
        for i in self.scope.keys():
            words = self.return_matches(list(map(lambda token: token.name, self.scope[i])),
                                        word, i)
            if len(words):
                result.append(*words)
        return result

    @staticmethod
    def return_matches(words: [str], char: str, type: str):
        result = []
        for word in words:
            if char in word:
                result.append(Hint(word, type))
        return result
