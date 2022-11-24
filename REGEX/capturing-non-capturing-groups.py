Regex_Pattern = r'(?:ok){3,}
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
