arr = [1,2,3,4,5,6,7,8]

x = list(filter(lambda a:a%2==0,arr))

for i in x:
    print(i,end=" ")

print(end="\n")
p = list(map(lambda x: pow(x,2),arr))

for i in p:
    print(i,end=" ")