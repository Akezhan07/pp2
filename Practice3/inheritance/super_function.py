class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, age):
        # Call parent's __init__ to set name
        super().__init__(name)
        # Add new attribute
        self.age = age

s = Student("Aman", 20)

print(s.name)
print(s.age)



class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        # First call parent method
        super().speak()
        # Then add extra behavior
        print("Woof!")

d = Dog()
d.speak()





class A:
    def __init__(self):
        print("Constructor A")

class B(A):
    def __init__(self):
        # Call parent constructor
        super().__init__()
        print("Constructor B")

b = B()




class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        # Call original method
        super().show()
        # Add extra functionality
        print("Child method")

c = Child()
c.show()
