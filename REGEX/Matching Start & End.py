Regex_Pattern = r"^\d\w\w\w\w\.$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
