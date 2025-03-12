# Program to find the GCD of two numbers using the Euclidean algorithm

# Taking two numbers as input from the user
M = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

# Using the Euclidean algorithm with a while loop
while n != 0:
    remainder = M % n  # Find the remainder
    M = n  # Assign n to M
    n = remainder  # Assign remainder to n

# When n becomes 0, M contains the GCD
print("The GCD of the given numbers is:", M)
