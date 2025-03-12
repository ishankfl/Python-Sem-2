# Program to check whether a number is even or odd
# - Takes user input as an integer.
# - Finds the remainder when divided by 2 using number % 2.
# - Uses an if-else statement to determine whether the number is even or odd.
# - Prints the result clearly.


# Taking input from the user and converting it to an integer
number = int(input("Enter a number: "))

# Finding the remainder when divided by 2
remainder = number % 2  

# Checking if the remainder is 0
if remainder == 0:
    print(number, "is an even number")  # If remainder is 0, the number is even
else:
    print(number, "is an odd number")  # If remainder is not 0, the number is odd
