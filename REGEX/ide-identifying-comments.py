import re
import sys

s = sys.stdin.read()

p = r'(/\*.*?\*/|//.*?$)'

for i in re.findall(p, s, re.DOTALL | re.MULTILINE):
    for j in re.split(r'\n', i):
        print(j.strip())
