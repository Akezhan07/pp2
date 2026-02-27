from math import tan, pi

n = int(input())
s = float(input())

area = (n * s**2) / (4 * tan(pi / n))

print(area)