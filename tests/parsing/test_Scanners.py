import unittest

from src.parsing.Scanners import *
from src.parsing.Tokens import OperatorToken


class TestTokenScanner(unittest.TestCase):
    def test_abstract_class(self):
        self.assertRaises(TypeError, TokenScanner)


class TestOperatorTokenScanner(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [int(), float(), bool(), str(), list(), tuple(), set(), dict()]
        self.scanner = OperatorTokenScanner()
        self.target_token_class = OperatorToken
        return super().setUp()

    def test_target_token_class(self):
        a = OperatorTokenScanner()
        self.assertEqual(a.target_token_class, self.target_token_class)

    def test_scan_requires_string_argument(self):
        no_str_values = self.values.copy()
        no_str_values.remove(str())
        for value in no_str_values:
            self.assertRaises(TypeError, self.scanner.scan, value)

    def test_scan_takes_exactly_one_argument(self):
        self.assertRaises(TypeError, self.scanner.scan, )
        self.assertRaises(TypeError, self.scanner.scan, "", "")

    def test_return_none_if_no_operator_at_start(self):
        self.assertEqual(self.scanner.scan(""), None)
        self.assertEqual(self.scanner.scan("123"), None)
        self.assertEqual(self.scanner.scan(" abc"), None)
        self.assertEqual(self.scanner.scan("1+23"), None)
        self.assertEqual(self.scanner.scan(" -abc"), None)

    def test_return_token_on_success(self):
        self.assertEqual(self.scanner.scan('+'), self.target_token_class('+'))
        self.assertEqual(self.scanner.scan('-'), self.target_token_class('-'))
        self.assertEqual(self.scanner.scan('*'), self.target_token_class('*'))
        self.assertEqual(self.scanner.scan('/'), self.target_token_class('/'))
        self.assertEqual(self.scanner.scan('%'), self.target_token_class('%'))
        self.assertEqual(self.scanner.scan('^'), self.target_token_class('^'))
        self.assertEqual(self.scanner.scan('='), self.target_token_class('='))
        self.assertEqual(self.scanner.scan('?'), self.target_token_class('?'))
        self.assertEqual(self.scanner.scan('**'), self.target_token_class('**'))

        self.assertEqual(self.scanner.scan('+123'), self.target_token_class('+'))
        self.assertEqual(self.scanner.scan('---'), self.target_token_class('-'))
        self.assertEqual(self.scanner.scan('*+-'), self.target_token_class('*'))
        self.assertEqual(self.scanner.scan('//'), self.target_token_class('/'))
        self.assertEqual(self.scanner.scan('%%'), self.target_token_class('%'))
        self.assertEqual(self.scanner.scan('^^'), self.target_token_class('^'))
        self.assertEqual(self.scanner.scan('=='), self.target_token_class('='))
        self.assertEqual(self.scanner.scan('??'), self.target_token_class('?'))
        self.assertEqual(self.scanner.scan('***'), self.target_token_class('**'))


class TestDelimiterTokenScanner(unittest.TestCase):
    def setUp(self) -> None:
        self.scanner = DelimiterTokenScanner()
        self.target_token_class = DelimiterToken
        return super().setUp()

    def test_target_token_class(self):
        self.assertEqual(self.scanner.target_token_class, self.target_token_class)

    def test_return_none_if_no_delimiter_at_start(self):
        self.assertEqual(self.scanner.scan(""), None)
        self.assertEqual(self.scanner.scan("1(2)3"), None)
        self.assertEqual(self.scanner.scan(" []abc"), None)
        self.assertEqual(self.scanner.scan("1;23"), None)
        self.assertEqual(self.scanner.scan(" ,abc"), None)

    def test_return_token_on_success(self):
        self.assertEqual(self.scanner.scan('('), self.target_token_class('('))
        self.assertEqual(self.scanner.scan(')'), self.target_token_class(')'))
        self.assertEqual(self.scanner.scan('['), self.target_token_class('['))
        self.assertEqual(self.scanner.scan(']'), self.target_token_class(']'))
        self.assertEqual(self.scanner.scan(';'), self.target_token_class(';'))
        self.assertEqual(self.scanner.scan(','), self.target_token_class(','))

        self.assertEqual(self.scanner.scan('()13'), self.target_token_class('('))
        self.assertEqual(self.scanner.scan(')--+'), self.target_token_class(')'))
        self.assertEqual(self.scanner.scan('[]+-'), self.target_token_class('['))
        self.assertEqual(self.scanner.scan(']/ss'), self.target_token_class(']'))
        self.assertEqual(self.scanner.scan(';;;%'), self.target_token_class(';'))
        self.assertEqual(self.scanner.scan(',,,^'), self.target_token_class(','))


class TestImaginaryUnitTokenScanner(unittest.TestCase):
    def setUp(self) -> None:
        self.scanner = ImaginaryUnitTokenScanner()
        self.target_token_class = ImaginaryUnitToken
        return super().setUp()

    def test_target_token_class(self):
        self.assertEqual(self.scanner.target_token_class, self.target_token_class)

    def test_return_none_if_no_imaginary_unit_at_start(self):
        self.assertEqual(self.scanner.scan(""), None)
        self.assertEqual(self.scanner.scan("1i(2)3"), None)
        self.assertEqual(self.scanner.scan(" i[]abc"), None)
        self.assertEqual(self.scanner.scan("1;23"), None)
        self.assertEqual(self.scanner.scan(" i"), None)

    def test_return_token_on_success(self):
        self.assertEqual(self.scanner.scan('i'), self.target_token_class('i'))

        self.assertEqual(self.scanner.scan('i12'), self.target_token_class('i'))


if __name__ == "__main__":
    unittest.main()
