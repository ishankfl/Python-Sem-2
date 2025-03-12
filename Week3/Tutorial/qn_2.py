# Program to find the greatest of three numbers

# Taking three numbers as input from the user
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

# Checking which number is the greatest
if num1 > num2 and num1 > num3:  # If num1 is greater than both num2 and num3
    print("The greatest number is", num1)
elif num2 > num1 and num2 > num3:  # If num2 is greater than both num1 and num3
    print("The greatest number is", num2)
else:  # If both above conditions are false, num3 must be the greatest
    print("The greatest number is", num3)
