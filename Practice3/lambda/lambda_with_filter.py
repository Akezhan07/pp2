numbers = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)



numbers = [-5, 3, -1, 7, -2]

# Keep only positive numbers
positives = list(filter(lambda x: x > 0, numbers))

print(positives)



words = ["apple", "cat", "banana", "dog"]

# Keep words longer than 4 characters
long_words = list(filter(lambda word: len(word) > 4, words))

print(long_words)
