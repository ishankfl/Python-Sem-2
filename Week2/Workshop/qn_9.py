# 9. Write a program that asks the user to enter two numbers a and b. Then
# write code to swap the values of a and b, and print them out.

# Asking the user to input two numbers
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

# Swapping using Python's tuple unpacking
a, b = b, a  

# Displaying the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)


#another way

a = 20
b = 30
print("Before Swapping")
print("a =", a)
print("b =", b)

a = a+b
b = a-b
a = a-b
print("After swapping:")
print("a =", a)
print("b =", b)