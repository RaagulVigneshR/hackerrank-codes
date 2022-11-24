Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^\.,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
