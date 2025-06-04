from core.DataTokens import DataToken
from core.TokenTypes import TokenType
import re 


class ListTokenizer:
	def tokenize(self, line:str ):
		if match := re.match(r'^(-{1,2})\s+(.*)',line):
			level = len(match.group(1))
			text = match.group(2).strip()
			return (DataToken(type=TokenType.LIST_ITEM, value=text, meta={'level':level,'list_type':'unordered'}))
		
		elif match := re.match(r'^(\d+\.)\s+(.*)',line):
			level = 1  #int(match.group(1).strip('.'))
			text = match.group(2).strip()
			return (DataToken(type=TokenType.LIST_ITEM, value=text, meta={'level':level,'list_type':'ordered'}))

		return None