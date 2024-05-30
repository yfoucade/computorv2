import unittest

from src.parsing.Scanners import OperatorTokenScanner
from src.parsing.Tokens import OperatorToken


class TestOperatorTokenScanner(unittest.TestCase):

    def test_target_token_class(self):
        a = OperatorTokenScanner()
        self.assertEqual(a.target_token_class, OperatorToken)


if __name__ == "__main__":
    unittest.main()
