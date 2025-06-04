from .header_tokenizer import HeaderTokenizer
from .list_tokenizer import ListTokenizer
from .text_tokenizer import TextTokenizer
from .inline_tokenizer import InlineTokenizer
import re

class MakeToken:
	tokens = []
	header_tokenizer = HeaderTokenizer()
	list_tokenizer = ListTokenizer()
	text_tokenizer = TextTokenizer()
	inline_tokenizer = InlineTokenizer()

	def __init__(self, lines:list):
		self.lines = lines


	def get_tokens(self):
		for line in self.lines :
			if line.startswith("#"):
				token = self.header_tokenizer.tokenize(line)
				if token:
					print(token.value)
					inline_tokens = self.inline_tokenizer.tokenize(token.value)
					if inline_tokens:
						self.tokens.append((token,inline_tokens))
					else:
						self.tokens.append(token)
			elif line.startswith("-"):
				token = self.list_tokenizer.tokenize(line)
				if token:
					inline_tokens = self.inline_tokenizer.tokenize(token.value)
					if inline_tokens:
						self.tokens.append((token,inline_tokens))
					else:
						self.tokens.append(token)
				
			elif re.match(r'^(\d+\.)\s+(.*)',line):
				token = self.list_tokenizer.tokenize(line)
				if token:
					inline_tokens = self.inline_tokenizer.tokenize(token.value)
					if inline_tokens:
						self.tokens.append((token,inline_tokens))
					else:
						self.tokens.append(token)
			else:
				token = self.text_tokenizer.tokenize(line)
				inline_tokens = self.inline_tokenizer.tokenize(token.value)
				if inline_tokens:
					self.tokens.append((token,inline_tokens))
				else:
					self.tokens.append(token)

		return self.tokens if self.tokens else None
