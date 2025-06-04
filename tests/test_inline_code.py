import unittest
from tokenizer.inline_tokenizer import InlineTokenizer
from core.TokenTypes import InlineType
from core.DataTokens import InlineToken

class TestInlineTokenizer(unittest.TestCase):

    def setUp(self):
        self.tokenizer = InlineTokenizer()

    def assertTokensEqual(self, actual_tokens, expected_tokens):
        self.assertEqual(len(actual_tokens), len(expected_tokens), "Token count mismatch.")
        for actual, expected in zip(actual_tokens, expected_tokens):
            self.assertEqual(actual.type, expected.type)
            self.assertEqual(actual.value, expected.value)

    def test_plain_text(self):
        text = "Just simple text"
        expected = [InlineToken(InlineType.TEXT, "Just simple text")]
        result = self.tokenizer.tokenize(text)
        self.assertTokensEqual(result, expected)

    def test_italic_tokens(self):
        cases = [
            ("This is *italic*", [InlineToken(InlineType.TEXT, "This is "), InlineToken(InlineType.ITALIC, "italic")]),
            ("This is _italic_", [InlineToken(InlineType.TEXT, "This is "), InlineToken(InlineType.ITALIC, "italic")]),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                result = self.tokenizer.tokenize(text)
                self.assertTokensEqual(result, expected)

    def test_bold_tokens(self):
        cases = [
            ("This is **bold**", [InlineToken(InlineType.TEXT, "This is "), InlineToken(InlineType.BOLD, "bold")]),
            ("This is __bold__", [InlineToken(InlineType.TEXT, "This is "), InlineToken(InlineType.BOLD, "bold")]),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                result = self.tokenizer.tokenize(text)
                self.assertTokensEqual(result, expected)

    def test_mixed_inline_tokens(self):
        text = "Mixing _italic_ and **bold** text"
        expected = [
            InlineToken(InlineType.TEXT, "Mixing "),
            InlineToken(InlineType.ITALIC, "italic"),
            InlineToken(InlineType.TEXT, " and "),
            InlineToken(InlineType.BOLD, "bold"),
            InlineToken(InlineType.TEXT, " text"),
        ]
        result = self.tokenizer.tokenize(text)
        self.assertTokensEqual(result, expected)

    def test_multiple_and_nested_cases(self):
        text = "This is _italic_ and this is **bold**, and this is just text"
        expected = [
            InlineToken(InlineType.TEXT, "This is "),
            InlineToken(InlineType.ITALIC, "italic"),
            InlineToken(InlineType.TEXT, " and this is "),
            InlineToken(InlineType.BOLD, "bold"),
            InlineToken(InlineType.TEXT, ", and this is just text"),
        ]
        result = self.tokenizer.tokenize(text)
        self.assertTokensEqual(result, expected)

    def test_unmatched_delimiters(self):
        text = "This is *not closed and this is **also not closed"
        expected = [InlineToken(InlineType.TEXT, text)]
        result = self.tokenizer.tokenize(text)
        self.assertTokensEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
