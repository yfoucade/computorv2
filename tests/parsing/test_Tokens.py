import unittest

from src.parsing.Tokens import OperatorToken


class TestOperatorToken(unittest.TestCase):

    def test_init_takes_an_argument(self):
        self.assertRaises(TypeError, OperatorToken, )

    def test_init_takes_a_string(self):
        for value in [int(), float(), list(), tuple(), set(), dict()]:
            self.assertRaises(TypeError, OperatorToken, value)
        tmp = OperatorToken('+')
        self.assertEqual(tmp.value, '+')
        tmp = OperatorToken('**')
        self.assertEqual(tmp.value, '**')

    def test_init_takes_no_more_than_one_argument(self):
        self.assertRaises(TypeError, OperatorToken, '+', '-')


if __name__ == '__main__':
    unittest.main()