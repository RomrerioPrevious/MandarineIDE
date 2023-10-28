class TokenType:
    def __init__(self, name, **kwargs):
        self.name = name
        self.objects = filter(lambda a: isinstance(a, str), kwargs["words"])

    @classmethod
    def is_type(cls):
        ...

    def __eq__(self, other):
        if not isinstance(other, TokenType):
            raise TypeError(f"Type of object {other} is not TokenType")
        return other.name == self.name
