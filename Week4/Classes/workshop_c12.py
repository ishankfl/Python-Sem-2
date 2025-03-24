# Write a program that takes N number of integers as input and puts them in a list. Then it should find out the maximum and minimum number from the list and print them out. The whole list must also be printed out. 
# (Hint: Assume that the first element of the list is maximum/minimum element, then iterate through the list comparing the assumed value with every other element to find the maximum and minimum value)

# Take input for the number of elements
N = int(input("Enter the total number of elements: "))

# Initialize an empty list
numbers = []
# Get N numbers from the user
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))  # Improved input prompt
    numbers.append(num)  # Add number to the list
# Print the full list
print("\nYour list of numbers:", numbers)
# Assume the first element is both the maximum and minimum
max_num = numbers[0]
min_num = numbers[0]
# Iterate through the list to find the actual max and min
for num in numbers:
    if num > max_num:  
        max_num = num  # Update max if a larger number is found
    if num < min_num:  
        min_num = num  # Update min if a smaller number is found
# Display the results
print("\nMaximum number:", max_num)
print("Minimum number:", min_num)

  