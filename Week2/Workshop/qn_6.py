# 6. Write a program that asks the user to input the radius of a circle. The program
# should calculate the area of the circle A = πr and print it out.

# Asking the user to input the radius
radius = float(input("Enter the radius of the circle: "))

# Using an approximate value of π
pi = 3.1416

# Calculating the area using the formula A = πr²
area = pi * (radius ** 2)

# Displaying the result
print("The area of the circle is:", area)
