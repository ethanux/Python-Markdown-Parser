from enum import Enum

class TokenType(Enum):
	HEADER 		= "HEADER"
	BOLD 		= "BOLD"
	ITALIC 		= "ITALIC"
	LIST_ITEM 	= "LIST_ITEM"
	TEXT 		= "TEXT"
	INLINE_CODE = "INLINE_CODE"
	

class InlineType(Enum):
    TEXT = 'TEXT'
    ITALIC = 'ITALIC'
    BOLD = 'BOLD'