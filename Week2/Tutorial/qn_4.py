
# Taking values for x and y to evaluate the expression: x³ + 3x²y + 3xy² + y³
x = float(input("Enter value of x: "))  # User enters value of x
y = float(input("Enter value of y: "))  # User enters value of y

# Calculating the given mathematical expression
expression_result = (x ** 3) + (3 * (x ** 2) * y) + (3 * x * (y ** 2)) + (y ** 3)

# Displaying the result of the expression
print("Result of the expression (x³ + 3x²y + 3xy² + y³):", expression_result)
