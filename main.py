
from tokenizer.make_token import MakeToken
from parsers.driver_parser import DriverParser


lines = []
with open('README.md', 'r') as f:
	lines = f.readlines()
	

tokenizer = MakeToken(lines)

tokens = tokenizer.get_tokens()



driver = DriverParser(tokens)


content = "\n".join(driver.html_parser())

html = f"""
	<html>
	<title>Markdown parser</title>
	<body>
		{content   }
	</body>
	</html>
"""
with open("html/markdown.html", "w") as f:
	f.write(html)
print(content)