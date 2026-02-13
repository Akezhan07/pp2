class Person:
    # __init__ is a constructor
    # It runs automatically when we create an object
    def __init__(self, name):
        # self refers to the current object
        # We store the passed name inside the object
        self.name = name

# Create object and pass argument
p1 = Person("Aman")

# Access instance attribute
print(p1.name)



class Student:
    def __init__(self, name, age):
        # Store both values inside object
        self.name = name
        self.age = age

s1 = Student("Bob", 20)

print(s1.name)
print(s1.age)




class Circle:
    def __init__(self, radius):
        self.radius = radius
        
        # Calculate area during object creation
        self.area = 3.14 * radius * radius

c1 = Circle(5)

print(c1.area)




class Person:
    def __init__(self, name="Unknown"):
        # If no name is provided, default is used
        self.name = name

p1 = Person()
p2 = Person("Aman")

print(p1.name)  # Unknown
print(p2.name)  # Aman
