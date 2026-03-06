import re

s = input()

parts = re.split(r'(?=[A-Z])', s)

print(parts)