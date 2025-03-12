# Program to calculate the factorial of a non-negative integer using a while loop

# Taking input from the user
N = int(input("Enter a non-negative integer: "))

# Initializing factorial result to 1
factorial = 1

# Using a while loop to calculate factorial
while N > 0:
    factorial *= N  # Multiply factorial by N
    N -= 1  # Decrease N by 1

# Displaying the result
print("The factorial is:", factorial)
