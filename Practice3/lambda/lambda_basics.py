# Lambda function that adds two numbers
# lambda arguments: expression
add = lambda a, b: a + b

# Call the lambda function
print(add(5, 3))


# Lambda function that returns the square of a number
square = lambda x: x * x

print(square(4))
print(square(7))


# Lambda function used directly without storing in a variable
print((lambda x: x * 2)(10))  # Multiply 10 by 2