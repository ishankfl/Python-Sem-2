# Write a program that takes N numbers as input from a user and puts them in a list. Then the program should find out the sum of all the odd numbers and the sum of all the even numbers from the list. 


# Take input for the number of elements
N = int(input("Enter the total number of elements: "))

# Initialize an empty list to store user inputs
numbers = []

# Get N numbers from the user
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))  # Take each number as input
    numbers.append(num)  # Store the number in the list

# Initialize sum variables
even_sum = 0  # Sum of even numbers
odd_sum = 0   # Sum of odd numbers

# Iterate through the list and calculate sums
for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        even_sum += num
    else:  # If the number is odd
        odd_sum += num

# Print the results
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
