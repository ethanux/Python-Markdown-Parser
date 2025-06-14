class CodeParser:
	def __init__(self,token):
		self.header = token[0]
		self.inline = token[1]
		

	def html_parser(self):
		code_open_tag = '<pre><code>'
		code_close_tag = '</code></pre>'
		
		
		parsed_token = code_open_tag + self.header.value + code_close_tag
		return parsed_token