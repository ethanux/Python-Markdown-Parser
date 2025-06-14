from .header_tokenizer import HeaderTokenizer
from .list_tokenizer import ListTokenizer
from .text_tokenizer import TextTokenizer
from .inline_tokenizer import InlineTokenizer
from .code_tokenizer import CodeTokenizer
import re

class MakeToken:
	
	header_tokenizer = HeaderTokenizer()
	list_tokenizer = ListTokenizer()
	text_tokenizer = TextTokenizer()
	inline_tokenizer = InlineTokenizer()
	code_tokenizer = CodeTokenizer()

	def __init__(self, lines:list):
		self.lines = lines
		self.tokens = []
		self.block_code_open = False
		self.block_code = []

	def process_token(self,token):
		inline_tokens = self.inline_tokenizer.tokenize(token.value)
		if inline_tokens:
			self.tokens.append((token,inline_tokens))
		else:
			self.tokens.append(token)

	def get_tokens(self):
		for line in self.lines :
			if (line == ' ' or line == '' or line =='\n' or not line) and not self.block_code_open :
				pass
			elif line.startswith("#") and not self.block_code_open :
				token = self.header_tokenizer.tokenize(line.strip())
				if token:
					self.process_token(token)
					
			elif re.match(r'^\s*-\s(.*)', line) and not self.block_code_open :
				token = self.list_tokenizer.tokenize(line.strip())
				if token:
					self.process_token(token)
				
			elif re.match(r'^(\d+\.)\s+(.*)',line) and not self.block_code_open :
				token = self.list_tokenizer.tokenize(line.strip())
				if token:
					self.process_token(token)

			

			else:
				token = self.text_tokenizer.tokenize(line.strip())
				self.process_token(token)

		return self.tokens if self.tokens else None
