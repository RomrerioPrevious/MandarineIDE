from bin.models.tokens.token_type import TokenType


class TokenTypeList:
    @staticmethod
    def get_token_types() -> [TokenType]:
        return {
            "Reserved Words": TokenType("Reserved Words",
                                        words=["and", "as", "assert", "break", "class", "continue", "def",
                                               "del", "elif", "else", "except", "False", "finally", "for",
                                               "from", "global",
                                               "if", "import", "in", "is", "lambda", "None", "nonlocal",
                                               "not", "or", "pass",
                                               "raise", "return", "True", "try", "with", "while", "yield"]),
            "Variable": TokenType("Variable"),
            "Method": TokenType("Method"),
            "Class": TokenType("Class")
        }
