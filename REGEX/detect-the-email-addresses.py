import re

ad = []
for _ in range(int(input())):
  s = input()

  a = re.findall(r"\b[\w\.]+@(?:\w+\.)+\w+\b", s)

  ad.extend(a)

print(';'.join(sorted(set(ad))))
