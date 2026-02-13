# Code 1: Simple function that prints a message
def my_function():
    # This function prints a greeting message to the console
    print("Hello from a function")

# Call the function to execute its code
my_function()


# Code 2: Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # This function takes a temperature in Fahrenheit and converts it to Celsius
    # Formula: (F - 32) * 5 / 9
    return (fahrenheit - 32) * 5 / 9

# Call the function with different Fahrenheit values and print the results
print(fahrenheit_to_celsius(77))  # Convert 77°F to Celsius
print(fahrenheit_to_celsius(95))  # Convert 95°F to Celsius
print(fahrenheit_to_celsius(50))  # Convert 50°F to Celsius


# Code 3: Function that returns a greeting message
def get_greeting():
    # This function returns a greeting string instead of printing it directly
    return "Hello from a function"

# Store the returned message in a variable
message = get_greeting()

# Print the stored message
print(message)


# Code 4: Function that returns a greeting and prints it directly
def get_greeting():
    # This function returns a greeting string
    return "Hello from a function"

# Call the function inside print to directly display the returned string
print(get_greeting())