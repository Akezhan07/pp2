numbers = [5, 2, 9, 1]

# Sort numbers in ascending order
sorted_numbers = sorted(numbers, key=lambda x: x)

print(sorted_numbers)



words = ["apple", "kiwi", "banana"]

# Sort words by their length
sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)



students = [("Aman", 3.5), ("Bob", 4.0), ("Charlie", 2.8)]

# Sort students by GPA (second element in tuple)
sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)
