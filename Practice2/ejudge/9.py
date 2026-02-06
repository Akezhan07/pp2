n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

max_element = a[0]
min_element = a[0]

for i in range(n):
    if a[i] > max_element:
        max_element = a[i]

    if a[i] < min_element:
        min_element = a[i]


for i in range(n):
    if a[i] == max_element:
        a[i] = min_element
        
print(*a)