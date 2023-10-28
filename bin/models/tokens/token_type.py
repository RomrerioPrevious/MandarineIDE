class TokenType:
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.objects = None
        if "words" in kwargs.keys():
            self.objects = filter(lambda a: isinstance(a, str), kwargs["words"])

    def __eq__(self, other):
        if not isinstance(other, TokenType):
            raise TypeError(f"Type of object {other} is not TokenType")
        return other.name == self.name

    def __str__(self):
        return self.name
