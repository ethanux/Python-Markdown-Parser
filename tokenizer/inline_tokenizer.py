from core.TokenTypes import InlineType  
from core.DataTokens import InlineToken
import re

class InlineTokenizer:

	def tokenize(self,text: str):
	    pattern = r'(_([^_]+)_|\*([^*]+)\*)'
	    tokens = []
	    pos = 0

	    for match in re.finditer(pattern, text):
	        start, end = match.span()

	        # Add text before match
	        if start > pos:
	            tokens.append(InlineToken(InlineType.TEXT, text[pos:start]))

	        if match.group(2):  # _italic_
	            tokens.append(InlineToken(InlineType.ITALIC, match.group(2)))
	        elif match.group(3):  # *bold*
	            tokens.append(InlineToken(InlineType.BOLD, match.group(3)))

	        pos = end

	    # Add remaining text
	    if pos < len(text):
	        tokens.append(InlineToken(InlineType.TEXT, text[pos:]))

	    return tokens