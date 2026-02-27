def isEven(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())
Even = isEven(n)

print(*Even, sep = ',')