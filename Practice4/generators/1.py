def squr(n):
    for i in range(1, n+1):
        yield i**2

n = int(input())
squar = squr(n)

for i in squar:
    print(i)