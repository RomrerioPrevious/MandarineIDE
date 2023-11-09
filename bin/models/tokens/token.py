from bin.models.tokens.token_type import TokenType
from dataclasses import dataclass


@dataclass
class Token:
    name: str
    type: TokenType

    def __hash__(self):
        return self.name.__hash__()
