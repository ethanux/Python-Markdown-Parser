from dataclasses import dataclass 
from .TokenTypes import InlineType ,TokenType 
# this is a dataclass to store token data 
# so we can treat them as objects not loose data types 

@dataclass
class DataToken:
	type : TokenType  			# Can either be : HEADER, LIST , PARAGRAGH, BOLD, ITALIC
	value : str				# Hedding text, List text, Bold text ...so on
	meta : dict = None		# meta data (Level : 1 , Level : 2 )

@dataclass
class InlineToken:
    type: InlineType
    value: str

