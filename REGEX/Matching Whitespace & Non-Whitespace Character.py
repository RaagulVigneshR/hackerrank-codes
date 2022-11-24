Regex_Pattern = r"\S\S\s\S\S\s\S\S"


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
