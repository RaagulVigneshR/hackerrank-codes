import re

ad = []
for _ in range(int(input())):
    s = input()
    a = re.findall(r"""https?://(?:ww[w2]\.){0,1}([\w\d\-\.]*\.\w+)[/?"]""", s)
    ad.extend(a)

print(';'.join(sorted(set(ad))))
