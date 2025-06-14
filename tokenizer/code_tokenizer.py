from core.TokenTypes import TokenType  
from core.DataTokens import DataToken
import re

class CodeTokenizer:
    def tokenize(self, line: str):
        # Match triple backtick for block code
        match_block = re.match(r'```([^`]*)```', line, re.DOTALL)
        if match_block:
            code = match_block.group(1).strip()
            if code:
                return DataToken(type=TokenType.BLOCK_CODE, value=code)

        else:
            return DataToken(type=TokenType.BLOCK_CODE, value=line)
        
        # Match single backtick for inline code
        
        return None
