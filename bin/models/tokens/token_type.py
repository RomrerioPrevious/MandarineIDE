from dataclasses import dataclass


@dataclass
class TokenType:
    name: str
    words: [str]

    def __eq__(self, other):
        if not isinstance(other, TokenType):
            raise TypeError(f"Type of object {other} is not TokenType")
        return other.name == self.name
