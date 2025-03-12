# Write a program that takes a number as input and prints out whether it is an odd or an even number.
# Write a program that takes 3 numbers as input and outputs the greater of the 3 numbers.
# Write a program that takes two numbers as input and finds out the GCD (greatest common divisor) of the two numbers using the Euclidean algorithm. (Use while loop)
# The factorial of a non-negative integer N, denoted by N!, is the product of all positive integers less than or equal to N. 
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# Write a program that takes a non-negative integer N as input and prints out its factorial. (Use while loop)
     	
#1

number = input("Enter any one number: ")
if int(number) % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
#2
# # Take three numbers as input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Check if the first number is greater than the second number
if num1 > num2:
    # If num1 is greater than num2, we still need to compare it with num3
    if num1 > num3:
        # If num1 is also greater than num3, then num1 is the greatest
        print("The greatest number is first:", num1)
    else:
        # If num3 is greater than num1, then num3 is the greatest
        print("The greatest number is third:", num3)

# If num1 is not greater than num2, then check if num2 is greater than num3
elif num2 > num3:
    # If num2 is greater than num3, then num2 is the greatest
    print("The greatest number is second:", num2)
else:
    # If neither num1 nor num2 is the greatest, then num3 must be the greatest
    print("The greatest number is third:", num3)


#>> Qn3
input_first = int(input("Enter the first number: "))
input_second = int(input("Enter the second number: "))

# # Check which number is greater and swap if the second one is greater
if input_first > input_second:
    temp = input_first
    input_first = input_second
    input_second = temp
# # Now, the greater number is stored in input_first, and the smaller one is stored in input_second

# # Find the remainder
remainder = input_first % input_second  # The % operator is used to find the remainder

while remainder > 0:
    # Swap the value of n to m and r to n according to the Euclidean algorithm
    input_first = input_second
    input_second = remainder
    remainder = input_first % input_second
# # According to the algorithm, when the remainder becomes 0, the GCD is stored in input_second
# # So, our output is:
print("The GCD of the two numbers is:", input_second)

