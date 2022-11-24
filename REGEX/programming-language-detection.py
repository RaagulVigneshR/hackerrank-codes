import sys

src = sys.stdin.read()

if '#include' in src:
    print("C")
elif 'import java' in src:
    print("Java")
else:
    print("Python")
