n = int(input())

is_Prime = True

for i in range(2, n):
    if n % i == 0:
        is_Prime = False
        break

if is_Prime:
    print("YES")
else:
    print("NO")
