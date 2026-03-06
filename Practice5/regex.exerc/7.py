import re

s = input()

camel = re.sub(r'_(\w)', lambda m: m.group(1).upper(), s)
print(camel)