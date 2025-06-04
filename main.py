
from tokenizer.make_token import MakeToken







lines = []
with open('README.md', 'r') as f:
	lines = f.readlines()
	

tokenizer = MakeToken(lines)

tokens = tokenizer.get_tokens()

print(tokens)
print("===========================================")
for token in tokens:
	print(token)