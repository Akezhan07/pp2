# Parent class
class Person:
    def greet(self):
        # Method available to child classes
        print("Hello")

# Child class inherits from Person
class Student(Person):
    # No new code, but inherits greet()
    pass

# Create object of Student
s1 = Student()

# Student can use greet() because of inheritance
s1.greet()



class Animal:
    def eat(self):
        print("Eating...")

# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog()

# Dog can use both methods
d.eat()   # Inherited from Animal
d.bark()  # Defined in Dog




class A:
    pass

class B(A):
    pass

obj = B()

# isinstance checks if obj belongs to class A
# True because B inherits from A
print(isinstance(obj, A))





class Person:
    def __init__(self, name):
        self.name = name

# Student does not define its own __init__
class Student(Person):
    pass

# Constructor from Person is used
s = Student("Aman")

print(s.name)
