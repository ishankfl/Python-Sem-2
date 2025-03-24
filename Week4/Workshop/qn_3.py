# Take input from the user for the number of integers they want to enter
N = int(input("Enter the number of integers: "))  

# Initialize an empty list to store the numbers
numbers = []

# Loop N times to take N numbers as input and append them to the list
for i in range(N):
    numbers.append(int(input("Enter a number: ")))

# Print the list of numbers entered by the user
print("The list of numbers is:", numbers)

# Initialize max_number with the first element of the list
max_number = numbers[0]
# Iterate through the list to find the maximum number
for num in numbers:
    if num > max_number:  # If the current number is greater than max_number, update max_number
        max_number = num

# Initialize min_number with the first element of the list
min_number = numbers[0]
# Iterate through the list to find the minimum number
for num in numbers:
    if num < min_number:  # If the current number is smaller than min_number, update min_number
        min_number = num

# Print the maximum and minimum numbers found in the list
print("Max number from the list is:", max_number)
print("Min number from the list is:", min_number)
