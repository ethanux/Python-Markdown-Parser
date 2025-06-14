from core.TokenTypes import InlineType  
from core.DataTokens import InlineToken
import re


class InlineTokenizer:
    def tokenize(self, text: str):
        pattern = r'(\*\*(.*?)\*\*|__(.*?)__|\*(.*?)\*|_(.*?)_|`([^`\s]+)`|`` (.*?) ``)'
        tokens = []
        pos = 0

        for match in re.finditer(pattern, text):
            start, end = match.span()

            # Add text before the match
            if start > pos:
                tokens.append(InlineToken(InlineType.TEXT, text[pos:start]))

            # Determine token type by group
            if match.group(2) or match.group(3):  # **bold** or __bold__
                tokens.append(InlineToken(InlineType.BOLD, match.group(2) or match.group(3)))
            elif match.group(4) or match.group(5):  # *italic* or _italic_
                tokens.append(InlineToken(InlineType.ITALIC, match.group(4) or match.group(5)))
            elif match.group(6):  # `inline code`
                tokens.append(InlineToken(InlineType.CODE, match.group(6)))
            elif match.group(7):  # `` inline code with spaces ``
                tokens.append(InlineToken(InlineType.CODE, match.group(7)))

            pos = end

        # Add any remaining text
        if pos < len(text):
            tokens.append(InlineToken(InlineType.TEXT, text[pos:]))

        return tokens
