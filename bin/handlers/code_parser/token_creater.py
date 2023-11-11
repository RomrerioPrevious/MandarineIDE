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
        if word in token_types["reserved_words"].words:
            return token_types["reserved_words"]
        if word in token_types["comparisons"].words:
            return token_types["comparisons"]
        if word in token_types["special_characters"].words:
            return token_types["special_characters"]
        return token_types["variable"]

    @staticmethod
    def is_type_with_previous_token(previous: str) -> TokenType:
        token_types = TokenTypeList.get_token_types()
        match previous:
            case "def":
                return token_types["function"]
            case "class":
                return token_types["class"]
            case _:
                raise KeyError("Is not token")
