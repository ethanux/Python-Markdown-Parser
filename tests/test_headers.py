import unittest
from tokenizer.header_tokenizer import HeaderTokenizer
from core.TokenTypes import TokenType
from core.DataTokens import DataToken

class TestHeaderTokenizer(unittest.TestCase):
    
    def setUp(self):
        self.tokenizer = HeaderTokenizer()

    def test_valid_headers(self):
        test_cases = [
            ("# Heading 1", 1, "Heading 1"),
            ("## Heading 2", 2, "Heading 2"),
            ("### Heading 3", 3, "Heading 3"),
            ("###### Heading 6", 6, "Heading 6"),
        ]
        for line, level, expected_text in test_cases:
            with self.subTest(line=line):
                token = self.tokenizer.tokenize(line)
                self.assertIsNotNone(token)
                self.assertEqual(token.type, TokenType.HEADER)
                self.assertEqual(token.value, expected_text)
                self.assertEqual(token.meta["level"], level)

    def test_invalid_headers(self):
        invalid_cases = [
            "",  # empty string
            "####### Too many hashes",  # more than 6 #
            "#",  # no space or text
            "#NoSpace",  # no space after hash
            "Text only",  # not a header at all
            "##    ",  # header level but no actual text
        ]
        for line in invalid_cases:
            with self.subTest(line=line):
                token = self.tokenizer.tokenize(line)
                self.assertIsNone(token)

    def test_header_with_extra_spaces(self):
        line = "#     Spaced Header   "
        token = self.tokenizer.tokenize(line)
        self.assertIsNotNone(token)
        self.assertEqual(token.value, "Spaced Header")
        self.assertEqual(token.meta["level"], 1)

if __name__ == '__main__':
    unittest.main()
