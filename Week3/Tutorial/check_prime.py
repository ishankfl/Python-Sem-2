# Check if the given number is prime or not
input_num = int(input("Enter a number: "))  # Take input from user
new_var = input_num  # Creating a new variable with the value of input_num
counter = 0  # Initialize counter variable to 0

while new_var > 0:  # Loop runs while new_var is greater than 0
    if input_num % new_var == 0:  # Check if input_num is divisible by new_var
        counter += 1  # Increment the counter if division has no remainder
    new_var -= 1  # Decrease new_var by 1 to check the next number

if counter == 2:  # If the number is prime, it will have exactly 2 divisors (1 and itself)
    print("The given number is prime")
else:  # If counter is not exactly 2, then the number is not prime
    print("The given number is not prime")


"""
This program checks whether a given number is prime using a straightforward approach. First, it takes an integer input from the user and assigns it to both input_num and a new variable new_var. It also initializes a counter to zero. The program then enters a while loop that runs as long as new_var is greater than zero. Inside the loop, it checks if input_num is divisible by new_var without leaving a remainder; if true, it increments the counter. After each iteration, new_var is decremented by one to check the next lower number. The loop continues until new_var reaches zero. Once the loop ends, the program evaluates the counter value—if it is exactly 2, meaning the number has only two divisors (1 and itself), it prints that the number is prime. Otherwise, it prints that the number is not prime.
"""

import math

