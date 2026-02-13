# Function that accepts an arbitrary number of arguments
# All passed values are stored inside a tuple called "kids"
def my_function(*kids):
    # kids is a tuple
    # Index 2 means the third element (counting starts from 0)
    print("The youngest child is " + kids[2])

# Passing three arguments
# They will be stored as: ("Emil", "Tobias", "Linus")
my_function("Emil", "Tobias", "Linus")



# Function that accepts any number of arguments
def my_function(*args):
    # args is automatically a tuple
    print("Type:", type(args))          # Shows that args is a tuple
    print("First argument:", args[0])   # Access first element
    print("Second argument:", args[1])  # Access second element
    print("All arguments:", args)       # Print entire tuple

# Calling function with three arguments
my_function("Emil", "Tobias", "Linus")



# Function that takes one normal parameter (greeting)
# and then any number of additional names
def my_function(greeting, *names):
    # Loop through all names passed after greeting
    for name in names:
        # Print greeting with each name
        print(greeting, name)

# "Hello" becomes greeting
# The rest become part of names tuple
my_function("Hello", "Emil", "Tobias", "Linus")



# Function that accepts any number of numeric arguments
def my_function(*numbers):
    total = 0  # Initialize total sum
    
    # Loop through each number in the tuple
    for num in numbers:
        # Add each number to total
        total += num
    
    # Return the final sum
    return total

# Calling the function with different amounts of numbers
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))