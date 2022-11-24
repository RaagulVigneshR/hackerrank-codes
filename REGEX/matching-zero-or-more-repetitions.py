Regex_Pattern = r'^\d\d\d*[a-z]*[A-Z]*$' 
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
