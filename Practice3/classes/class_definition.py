# Define a class named Person
class Person:
    # pass means the class is empty for now
    # It is required if we don't put anything inside
    pass

# Create an object (instance) of the class
p1 = Person()

# Print the type of the object
print(type(p1))  # Shows that p1 is a Person object



# Define a class with class attributes
class Person:
    # These variables belong to the class
    name = "Aman"
    age = 18

# Create an object
p1 = Person()

# Access class attributes using the object
print(p1.name)
print(p1.age)



class Car:
    brand = "Toyota"  # Class attribute

# Create two separate objects
car1 = Car()
car2 = Car()

# Both objects share the same class attribute
print(car1.brand)
print(car2.brand)



class Student:
    name = "Unknown"

s1 = Student()

# This creates an instance attribute for s1 only
# It does NOT change the class attribute
s1.name = "Akezhan"

print(s1.name)        # Akezhan
print(Student.name)   # Still "Unknown"
