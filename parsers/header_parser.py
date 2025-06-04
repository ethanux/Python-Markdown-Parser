from .inline_code_parser import InlineParser
class HeaderParser:
	def __init__(self,token):
		self.header = token[0]
		self.inline = token[1]
		

	def html_parser(self):
		header_open_tag = '<h' + f"{( 1 * self.header.meta['level'])}" + '>'
		header_close_tag = '</h' + f"{(1 * self.header.meta['level'])}" + '>'
		
		inline_parser =  InlineParser(self.inline)
		parsed_token = header_open_tag + inline_parser.html_parser() + header_close_tag
		return parsed_token