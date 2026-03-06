import re

s = input()

if re.search(r"[a-z]+_[a-z]+", s):
    print("Match!")
else:
    print("No match!")