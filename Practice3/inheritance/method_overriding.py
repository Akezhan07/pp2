class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    # Override parent's method
    def sound(self):
        print("Woof!")

d = Dog()

# Child version is executed
d.sound()



class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        print("Hi, I am a student")

s = Student()
s.greet()



class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        # Custom implementation
        return 4 * 4

sq = Square()
print(sq.area())




class A:
    def show(self):
        print("A method")

class B(A):
    def show(self):
        # Use parent method
        super().show()
        print("B method")

b = B()
b.show()
