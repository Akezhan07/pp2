n = int(input())
a = input().split()

max_value = int(a[0])

for i in range(n):
    if int(a[i]) > max_value:
        max_value = int(a[i])

print(max_value)