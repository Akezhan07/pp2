import re

s = input()

snake = re.sub(r'([A-Z])', r'_\1', s).lower()

print(snake)