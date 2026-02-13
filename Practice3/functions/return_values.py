# Function that returns the sum of two numbers
def add_numbers(a, b):
    # The function calculates the sum
    result = a + b
    
    # Returns the result instead of printing it
    return result

# Calling the function and storing the returned value
sum_value = add_numbers(5, 3)

# Printing the returned result
print(sum_value)



# Function that returns the square of a number
def square(number):
    # Multiply the number by itself
    return number * number

# Call the function and print the returned value directly
print(square(4))
print(square(7))



# Function that returns a formatted greeting message
def create_greeting(name):
    # Create and return a string
    return "Hello, " + name + "!"

# Store returned value in a variable
message = create_greeting("Aman")

# Print the result
print(message)



# Function that checks if a number is even
def is_even(number):
    # If number divided by 2 gives remainder 0,
    # return True, otherwise return False
    if number % 2 == 0:
        return True
    else:
        return False

# Calling the function and printing results
print(is_even(10))
print(is_even(7))