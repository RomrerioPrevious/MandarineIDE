from bin.models.tokens.token_type import TokenType
from bin.models.tokens.token_type_list import TokenTypeList


class Token:
    def __init__(self, name: str, type: TokenType):
        self.name = name
        self.type = type

    @staticmethod
    def token_fabric(word: str, previous):
        if previous is None:
            token_type = Token.is_type_without_previous_token(word)
        else:
            token_type = Token.is_type_with_previous_token(previous)
        return Token(word, token_type)

    @staticmethod
    def is_type_without_previous_token(word) -> TokenType:
        token_types = TokenTypeList.get_token_types()
        if word in token_types["Reserved Words"].objects:
            return token_types["Reserved Words"]
        if word in token_types["Comparisons"].objects:
            return token_types["Comparisons"]
        return token_types["Variable"]

    @staticmethod
    def is_type_with_previous_token(previous) -> TokenType:
        token_types = TokenTypeList.get_token_types()
        match previous.name:
            case "def":
                return token_types["Function"]
            case "class":
                return token_types["Class"]
            case _:
                raise KeyError("Is not token")

    def __str__(self) -> str:
        return f"Token(name={self.name}, type={self.type})"
