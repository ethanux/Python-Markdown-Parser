import unittest
from tokenizer.text_tokenizer import TextTokenizer
from core.TokenTypes import TokenType
from core.DataTokens import DataToken

class TestTextTokenizer(unittest.TestCase):

    def setUp(self):
        self.tokenizer = TextTokenizer()

    def test_basic_text(self):
        line = "This is a normal text line."
        token = self.tokenizer.tokenize(line)
        self.assertIsInstance(token, DataToken)
        self.assertEqual(token.type, TokenType.TEXT)
        self.assertEqual(token.value, line)

    def test_empty_string(self):
        line = ""
        token = self.tokenizer.tokenize(line)
        self.assertIsInstance(token, DataToken)
        self.assertEqual(token.type, TokenType.TEXT)
        self.assertEqual(token.value, "")

    def test_text_with_symbols(self):
        line = "Text with symbols! @#$%^&*()"
        token = self.tokenizer.tokenize(line)
        self.assertEqual(token.type, TokenType.TEXT)
        self.assertEqual(token.value, line)

    def test_whitespace_only(self):
        line = "     "
        token = self.tokenizer.tokenize(line)
        self.assertEqual(token.type, TokenType.TEXT)
        self.assertEqual(token.value, line)

if __name__ == "__main__":
    unittest.main()
