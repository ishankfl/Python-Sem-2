# Given list with duplicate elements
numbers = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]

# Create an empty list to store unique elements
unique_numbers = []

# Iterate through the original list
for num in numbers:
    if num not in unique_numbers:  # Check if the number is already in unique_numbers
        unique_numbers.append(num)  # Add it if it's not present

# Print the list with unique elements
print("List with unique elements:", unique_numbers)
