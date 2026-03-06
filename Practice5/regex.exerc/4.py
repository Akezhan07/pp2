import re

s = input()

if re.search(r"[A-Z][a-z]+", s):
    print("Match!")
else:
    print("No match!")