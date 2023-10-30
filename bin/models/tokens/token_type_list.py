from bin.models.tokens.token_type import TokenType


class TokenTypeList:
    @staticmethod
    def get_token_types() -> {str, TokenType}:
        return {
            "Reserved Words": TokenType("Reserved Words",
                                        words=["and", "as", "assert", "break", "class", "continue", "def",
                                               "del", "elif", "else", "except", "False", "finally", "for",
                                               "from", "global",
                                               "if", "import", "in", "is", "lambda", "None", "nonlocal",
                                               "not", "or", "pass",
                                               "raise", "return", "True", "try", "with", "while", "yield"]),
            "Comparisons": TokenType("Comparisons",
                                     words=["==", "!=", "!", "<", ">", "<=", ">="]),
            "Special characters": TokenType("Special characters",
                                            words=[".", ",", "/", "*", "-", "+", ":", "=", " ", "(", ")", "\n"]),
            "Variable": TokenType("Variable", words=None),
            "Function": TokenType("Function", words=None),
            "Class": TokenType("Class", words=None)
        }
