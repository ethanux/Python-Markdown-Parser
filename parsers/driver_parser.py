
from tokenizer.make_token import MakeToken
from parsers.header_parser import HeaderParser
from parsers.list_parser import ListParser
from parsers.text_parser import TextParser
from parsers.code_parser import CodeParser
from core.TokenTypes import TokenType 








class DriverParser:

	def __init__(self,tokens):
		self.tokens = tokens

		self.grouped_list = []
		self.cnt = 0
		self.html_content = []

	def html_parser(self):
		for token in self.tokens:	
			print("==="*50)
			print(token)
			print("=="*50)
			if token[0].type == TokenType.HEADER:   # header aprser 
				parser = HeaderParser(token)
				html = parser.html_parser()
				self.html_content.append(html)
			
			elif token[0].type == TokenType.LIST_ITEM and token[0].meta['list_type'] == 'unordered' : ## ORdered list parser 
				 
				self.grouped_list.append(token)
				if self.cnt + 1 < len(self.tokens) and self.tokens[self.cnt+1][0].type == TokenType.LIST_ITEM and self.tokens[self.cnt+1][0].meta['list_type'] == 'unordered':

					pass
				else:
					parser = ListParser(self.grouped_list)
					html = parser.html_parser_unordered_list()
					self.html_content.append(html)
					self.grouped_list = []
			
			elif token[0].type == TokenType.LIST_ITEM and token[0].meta['list_type'] == 'ordered' : # unordered list Parser
				
				self.grouped_list.append(token)
				if self.cnt + 1 < len(self.tokens) and self.tokens[self.cnt+1][0].type == TokenType.LIST_ITEM and self.tokens[self.cnt+1][0].meta['list_type'] == 'ordered':

					pass
				else:
					parser = ListParser(self.grouped_list)
					html = parser.html_parser_ordered_list()
					self.html_content.append(html)
					self.grouped_list = []

			elif token[0].type == TokenType.BLOCK_CODE:
				parser = TextParser(token)
				html = parser.html_parser()
				self.html_content.append(html)

			elif token[0].type == TokenType.TEXT:
				parser = CodeParser(token)
				html = parser.html_parser()
				self.html_content.append(html)
			else:
				print("something went wrong")

			self.cnt += 1 
		self.cnt = 0
		return self.html_content








