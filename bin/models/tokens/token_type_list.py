from bin.models.tokens.token_type import TokenType


class TokenTypeList:
    @staticmethod
    def get_token_types() -> {str, TokenType}:
        return {
            "reserved_words": TokenType("reserved_words",
                                        words=["and", "as", "assert", "break", "class", "continue", "def",
                                               "del", "elif", "else", "except", "False", "finally", "for",
                                               "from", "global",
                                               "if", "import", "in", "is", "lambda", "None", "nonlocal",
                                               "not", "or", "pass",
                                               "raise", "return", "True", "try", "with", "while", "yield"]),
            "comparisons": TokenType("comparisons",
                                     words=["==", "!=", "!", "<", ">", "<=", ">="]),
            "special_characters": TokenType("special_characters",
                                            words=[".", ",", "/", "*", "-", "+", ":", "=", " ", "(", ")", "\n"]),
            "variable": TokenType("variable", words=None),
            "function": TokenType("function", words=None),
            "class": TokenType("class", words=None)
        }
