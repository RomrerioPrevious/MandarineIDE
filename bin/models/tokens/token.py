from bin.models.tokens.token_type import TokenType
from dataclasses import dataclass


@dataclass
class Token:
    name: str
    type: TokenType

    def __str__(self) -> str:
        return f"Token(name='{self.name}', type={self.type})"
