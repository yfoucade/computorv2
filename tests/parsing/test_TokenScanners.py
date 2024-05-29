import unittest

from src.parsing.Tokens import *
from src.parsing.TokenScanners import *


class TestOperatorTokenScanner(unittest.TestCase):

    def test_target_token_class(self):
        a = OperatorTokenScanner()
        self.assertEqual(a.target_token_class, OperatorToken)


if __name__ == "__main__":
    unittest.main()
