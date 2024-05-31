from typing import TypeVar


Self = TypeVar("Self", bound="Token")


class Token:
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError("value should be of type str.")
        self.value = value

    def __eq__(self, other: Self):
        return isinstance(other, type(self)) and self.value == other.value


class OperatorToken(Token): pass
class DelimiterToken(Token): pass
class ImaginaryUnitToken(Token): pass
class IdentifierToken(Token): pass
class RationalNumberToken(Token): pass