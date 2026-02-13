class A:
    def method_a(self):
        print("Method from A")

class B:
    def method_b(self):
        print("Method from B")

# C inherits from both A and B
class C(A, B):
    pass

c = C()

# Can access methods from both parents
c.method_a()
c.method_b()



class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

# Child inherits Father first
class Child(Father, Mother):
    pass

c = Child()

# Python chooses Father.skills() because of MRO
c.skills()




class X:
    def show(self):
        print("X")

class Y:
    def show(self):
        print("Y")

class Z(X, Y):
    pass

z = Z()

# X method is used because it appears first
z.show()




class A:
    def hello(self):
        print("Hello from A")

class B:
    def hello(self):
        print("Hello from B")

class C(A, B):
    def greet(self):
        # Call hello() based on MRO
        self.hello()

c = C()
c.greet()
