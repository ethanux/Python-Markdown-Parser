from core.TokenTypes import TokenType  
from core.DataTokens import DataToken
import re

class TextTokenizer:
	def tokenize(self, line: str):
		level = 1
		return (DataToken(type=TokenType.TEXT, value=line))
		

