numbers = [1, 2, 3, 4, 5]

# map applies the lambda function to every element in the list
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)


names = ["emil", "tobias", "linus"]

# Convert each name to uppercase
upper_names = list(map(lambda name: name.upper(), names))

print(upper_names)


words = ["apple", "banana", "kiwi"]

# Map each word to its length
lengths = list(map(lambda word: len(word), words))

print(lengths)
