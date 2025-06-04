from .inline_code_parser import InlineParser

class TextParser:
	def __init__(self,token):
		self.text = token[0]
		self.inline = token[1]

	def html_parser(self):
		text_open_tag = '<p>'
		text_close_tag = '</p>'
		inline_parser = InlineParser(self.inline)
		parsed_token = text_open_tag + inline_parser.html_parser() + text_close_tag
		return parsed_token