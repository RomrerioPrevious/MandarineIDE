from bin.models import Hint, TokenTypeList, TokenType


class HintParser:
    def __init__(self):
        self.all_hint = []
        for token_type in TokenTypeList.get_token_types().items():
            if token_type.words is None:
                continue
            self.all_hint.append(token_type.words)

    def get_hints(self, word: str) -> [Hint]:
        words = list(filter(lambda char: char in word, self.all_hint))
        result = []
        for i in words:
            result = Hint(i, "method")
        return None
