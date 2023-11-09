from bin.models import TokenType, TokenTypeList, Token


class TokenCreator:
    @staticmethod
    def token_fabric(word: str, previous=None) -> Token:
        if previous is None:
            token_type = TokenCreator.is_type_without_previous_token(word)
        else:
            token_type = TokenCreator.is_type_with_previous_token(previous)
        return Token(word, token_type)

    @staticmethod
    def is_type_without_previous_token(word: str) -> TokenType:
        token_types = TokenTypeList.get_token_types()
        if word in token_types["Reserved Words"].words:
            return token_types["Reserved Words"]
        if word in token_types["Comparisons"].words:
            return token_types["Comparisons"]
        if word in token_types["Special characters"].words:
            return token_types["Special characters"]
        return token_types["Variable"]

    @staticmethod
    def is_type_with_previous_token(previous: str) -> TokenType:
        token_types = TokenTypeList.get_token_types()
        match previous:
            case "def":
                return token_types["Function"]
            case "class":
                return token_types["Class"]
            case _:
                raise KeyError("Is not token")
