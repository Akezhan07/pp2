n = int(input())
a = input().split()

max_value = int(a[0])
max_index = 0


for i in range(n):
    if int(a[i]) > max_value:
        max_value = int(a[i])
        max_index = i
        

print(max_index + 1)