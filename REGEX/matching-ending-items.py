Regex_Pattern = r'^[a-zA-Z]*s$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
