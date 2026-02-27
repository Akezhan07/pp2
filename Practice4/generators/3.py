def isDiv(n):
    for i in range(n+1):
        if i % 3 and i % 4 == 0:
            yield i


n = int(input())
gen = isDiv(n)

for i in gen:
    print(i)