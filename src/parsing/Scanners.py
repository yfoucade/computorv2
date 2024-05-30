from . import Tokens

class OperatorTokenScanner:
    def __init__(self):
        self.target_token_class = Tokens.OperatorToken