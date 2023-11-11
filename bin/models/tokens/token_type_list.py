from bin.models.tokens.token_type import TokenType


class TokenTypeList:
    @staticmethod
    def get_token_types() -> {str, TokenType}:
        return {
            "reserved_words": TokenType("Reserved Words",
                                        words=["and", "as", "assert", "break", "class", "continue", "def",
                                               "del", "elif", "else", "except", "False", "finally", "for",
                                               "from", "global",
                                               "if", "import", "in", "is", "lambda", "None", "nonlocal",
                                               "not", "or", "pass",
                                               "raise", "return", "True", "try", "with", "while", "yield"]),
            "comparisons": TokenType("Comparisons",
                                     words=["==", "!=", "!", "<", ">", "<=", ">="]),
            "special_characters": TokenType("Special characters",
                                            words=[".", ",", "/", "*", "-", "+", ":", "=", " ", "(", ")", "\n"]),
            "variable": TokenType("Variable", words=None),
            "function": TokenType("Function", words=None),
            "class": TokenType("Class", words=None)
        }
