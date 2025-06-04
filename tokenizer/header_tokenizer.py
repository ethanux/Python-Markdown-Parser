from core.TokenTypes import TokenType  
from core.DataTokens import DataToken
import re

class HeaderTokenizer:
	def tokenize(self, line: str):
		match = re.match(r'^(#{1,6})\s+(.*)',line)
		if match:
			level = len(match.group(1))
			text = match.group(2).strip()
			return (DataToken(type=TokenType.HEADER, value=text,meta={'level':level}))
		return None

