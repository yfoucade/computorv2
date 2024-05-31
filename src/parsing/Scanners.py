import abc

from .Tokens import *


class ScannerServer:
    def __init__(self):
        self.token_scanners = [ OperatorTokenScanner(), DelimiterTokenScanner(),
                                ImaginaryUnitTokenScanner(), IdentifierTokenScanner(),
                                RationalNumberTokenScanner(), ]

    def scan_next_token(self, string: str) -> Token | None:
        tokens = [scanner.scan(string) for scanner in self.token_scanners]
        tokens = [t for t in tokens if t is not None]
        if not tokens:
            return None
        if len(tokens) > 1: # pragma: no cover
            raise ValueError("Ambiguous value")
        return tokens[0]


class TokenScanner(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        self.target_token_class = None

    def scan(self, string: str):
        if not isinstance(string, str):
            raise TypeError
        if not string:
            return None

        token = self.get_token(string)

        if token:
            return self.target_token_class(token)
        else:
            return None

    @abc.abstractmethod
    def get_token(self, string: str):
        pass


class OperatorTokenScanner(TokenScanner):
    """
    List of operators:
    '+', '-', '*', '/', '%', '^', '**', '=', '?'
    """
    def __init__(self):
        self.target_token_class = OperatorToken

    def get_token(self, string: str):
        if string.startswith('**'):
            return '**'
        if string[0] in '+-*/%^=?':
            return string[0]
        else:
            return None


class DelimiterTokenScanner(TokenScanner):
    """
    List of delimiters:
    '(', ')', '[', ']', ',', ';'
    """
    def __init__(self):
        self.target_token_class = DelimiterToken

    def get_token(self, string: str):
        if string[0] in '()[];,':
            return string[0]
        else:
            return None


class ImaginaryUnitTokenScanner(TokenScanner):
    """
    Imaginary unit is represented by the letter 'i'.
    """
    def __init__(self):
        self.target_token_class = ImaginaryUnitToken

    def get_token(self, string: str):
        string += '$$'
        if string.startswith('i') and not string[1].isalpha():
            return 'i'
        return None


class IdentifierTokenScanner(TokenScanner):
    """
    Any sequence of aphabetical characters except 'i'.
    """
    def __init__(self):
        self.target_token_class = IdentifierToken

    def get_token(self, string: str):
        i = 0
        while i < len(string) and string[i].isalpha():
            i += 1
        res = string[:i]
        if res not in ('', 'i'):
            return res
        return None


class RationalNumberTokenScanner(TokenScanner):
    """
    An integer, or a number with a decimal separator '.' with at least
    one of integer and fractional parts.
    ex:
        123
        123.
        12.3
        .123
    """
    def __init__(self):
        self.target_token_class = RationalNumberToken

    def get_token(self, string: str):
        i = 0
        if string[i].isdigit():
            while i < len(string) and string[i].isdigit():
                i += 1
            if i < len(string) and string[i] == '.':
                i += 1
            while i < len(string) and string[i].isdigit():
                i += 1
        elif string[i] == '.':
            i = 1
            while i < len(string) and string[i].isdigit():
                i += 1
        res = string[:i]
        if res not in ('', '.'):
            return res
        return None
