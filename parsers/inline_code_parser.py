from core.TokenTypes import InlineType 

class InlineParser:
	def __init__(self,token):
		self.tokens = token
		self.parsed_token = []


	def html_parser(self):
		for token in self.tokens:

			if token.type == InlineType.TEXT:
				self.parsed_token.append(token.value)

			elif token.type == InlineType.BOLD :
				bold = f'<b>{token.value}</b>'
				self.parsed_token.append(bold)

			elif token.type == InlineType.ITALIC :
				italic = f'<i>{token.value}</i>'
				self.parsed_token.append(italic)

			elif token.type == InlineType.CODE :
				code = f'<code>{token.value}</code>'
				self.parsed_token.append(code)
		
		return "".join(self.parsed_token)