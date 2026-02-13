class Student:
    # Class variable
    school = "ABC School"

s1 = Student()
s2 = Student()

# Both objects access same class variable
print(s1.school)
print(s2.school)




class Student:
    school = "ABC School"

# Change value for entire class
Student.school = "XYZ School"

print(Student.school)




class Person:
    country = "Kazakhstan"  # Class variable

p1 = Person()

# Create instance variable with same name
p1.country = "USA"

print(Person.country)  # Kazakhstan
print(p1.country)      # USA




class Counter:
    count = 0  # Class variable
    
    def __init__(self):
        # Increase counter every time object is created
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)  # 3 objects created
