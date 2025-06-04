from .inline_code_parser import InlineParser
class ListParser:
	def __init__(self,token):
		self.token_list = token
		self.parsed_list_item = []

	def html_parser_unordered_list(self):
		unordered_list_open_tag = "<ul>"
		unordered_list_close_tag = "</ul>"
		list_item_open_tag = "<li>"
		list_item_close_tag = "</li>"

		
		for token in self.token_list:
			inline_parser = InlineParser(token[1])

			item = list_item_open_tag + inline_parser.html_parser() + list_item_close_tag
			self.parsed_list_item.append(item)

		result = " ".join(self.parsed_list_item)
		return unordered_list_open_tag + result + unordered_list_close_tag

	def html_parser_ordered_list(self):
		unordered_list_open_tag = "<ol>"
		unordered_list_close_tag = "</ol>"
		list_item_open_tag = "<li>"
		list_item_close_tag = "</li>"

		
		for token in self.token_list:
			inline_parser = InlineParser(token[1])
			item = list_item_open_tag +  inline_parser.html_parser() + list_item_close_tag
			self.parsed_list_item.append(item)

		result = " ".join(self.parsed_list_item)
		return unordered_list_open_tag + result + unordered_list_close_tag