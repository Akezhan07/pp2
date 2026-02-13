class Person:
    # Method inside class
    def greet(self):
        # self is required for instance methods
        print("Hello!")

p1 = Person()

# Call method using object
p1.greet()



class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        # Access object attribute
        print(self.name, "says Woof!")

d1 = Dog("Rex")
d1.bark()



class Calculator:
    def add(self, a, b):
        # Return result instead of printing
        return a + b

calc = Calculator()

result = calc.add(5, 3)
print(result)



class Person:
    def greet(self):
        return "Hello"
    
    def introduce(self, name):
        # Call another method using self
        message = self.greet()
        print(message, name)

p = Person()
p.introduce("Aman")
