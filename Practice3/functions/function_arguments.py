# Code 1: Function with one parameter

def my_function(fname):
    # This function takes one parameter: fname (first name)
    # It prints the first name followed by the fixed last name "Refsnes"
    print(fname + " Refsnes")

# Calling the function with different first names
# Each time, the given name is combined with "Refsnes"
my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Code 2: Function with two parameters

def my_function(fname, lname):
    # This function takes two parameters:
    # fname (first name) and lname (last name)
    # It prints them together with a space in between
    print(fname + " " + lname)

# Calling the function with both first and last name
my_function("Emil", "Refsnes")


# Code 3: Function with a default parameter value

def my_function(name="friend"):
    # This function has a default parameter "friend"
    # If no argument is given when calling the function,
    # the value "friend" will be used automatically
    print("Hello", name)

# Calling the function with different arguments
# When a name is provided, it replaces the default value
my_function("Emil")
my_function("Tobias")

# Here no argument is provided,
# so the default value "friend" is used
my_function()

# Again providing a custom name
my_function("Linus")


# Code 4: Another function with a default parameter

def my_function(country="Norway"):
    # The default country is set to "Norway"
    # If no argument is passed, it will print "Norway"
    print("I am from", country)

# Calling the function with specific countries
# These values override the default value
my_function("Sweden")
my_function("India")

# No argument provided → default value "Norway" is used
my_function()

# Providing another custom value
my_function("Brazil")
