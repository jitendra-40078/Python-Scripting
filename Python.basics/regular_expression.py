import re

text = "The quick dark coffee"

pattern = r"quick"

match = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match")