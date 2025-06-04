import unittest
from tokenizer.list_tokenizer import ListTokenizer
from core.TokenTypes import TokenType
from core.DataTokens import DataToken

class TestListTokenizer(unittest.TestCase):

    def setUp(self):
        self.tokenizer = ListTokenizer()

    def test_unordered_list_items(self):
        test_cases = [
            ("- Item one", 1, "Item one"),
            ("-- Nested item", 2, "Nested item"),
        ]
        for line, level, expected_text in test_cases:
            with self.subTest(line=line):
                token = self.tokenizer.tokenize(line)
                self.assertIsNotNone(token)
                self.assertEqual(token.type, TokenType.LIST_ITEM)
                self.assertEqual(token.value, expected_text)
                self.assertEqual(token.meta["level"], level)
                self.assertEqual(token.meta["list_type"], "unordered")

    def test_ordered_list_items(self):
        test_cases = [
            ("1. First item", "First item"),
            ("12. Second item", "Second item"),
            ("3.   With extra spaces", "With extra spaces"),
        ]
        for line, expected_text in test_cases:
            with self.subTest(line=line):
                token = self.tokenizer.tokenize(line)
                self.assertIsNotNone(token)
                self.assertEqual(token.type, TokenType.LIST_ITEM)
                self.assertEqual(token.value, expected_text)
                self.assertEqual(token.meta["level"], 1)
                self.assertEqual(token.meta["list_type"], "ordered")

    def test_invalid_list_items(self):
        invalid_lines = [
            "-",                # No content
            "--",               # Nested but no content
            "1.",               # Ordered, no text
            "-NoSpace",         # Dash with no space
            "1.NoSpace",        # Numbered with no space
            "Random text",      # Not a list at all
        ]
        for line in invalid_lines:
            with self.subTest(line=line):
                token = self.tokenizer.tokenize(line)
                self.assertIsNone(token)

if __name__ == '__main__':
    unittest.main()
