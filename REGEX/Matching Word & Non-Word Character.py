Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
