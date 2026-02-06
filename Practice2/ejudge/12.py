n = int(input())
a = list(map(int, input().split()))

for x in a:
    x = x * x
    print(x, end = ' ')