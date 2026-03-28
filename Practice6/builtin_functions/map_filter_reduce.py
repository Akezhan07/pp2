# Initial list of integers from 1 to 8
arr = [1, 2, 3, 4, 5, 6, 7, 8]

# Filter: Creates a new list containing only elements that satisfy the condition (even numbers)
# lambda a: a % 2 == 0 returns True if the number is divisible by 2
x = list(filter(lambda a: a % 2 == 0, arr))

# Iterate through the filtered list and print each element followed by a space
for i in x:
    print(i, end=" ")

print(end="\n")

# Map: Applies a function to every item in the original list
# lambda x: pow(x, 2) squares each number in the list
p = list(map(lambda x: pow(x, 2), arr))

# Iterate through the mapped list (squares) and print each element
for i in p:
    print(i, end=" ")