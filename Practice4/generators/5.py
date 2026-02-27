def count(n):
    for i in range(n + 1):
        yield n - i


n = int(input())
gen = count(n)

for i in gen:
    print(i)