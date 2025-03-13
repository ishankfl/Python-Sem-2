# # A Fibonacci sequence is characterized by the fact that every number after the first two is the sum of the two preceding ones. By definition, the first two numbers in the Fibonacci sequence are 1 and 1. 
# # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# # Write a program that generates the first N numbers of the Fibonacci sequence and prints them out. N should be taken as input from the user. (Hint: Use lists)


# N = int(input("Enter the fibonacci number to generate "))

# i = 1
# previous = 1
# list = []

# while(i<N):
#     if i != previous:
#         list.append(previous)
#     list.append (i)
#     # print(i+previous, i, previous)
#     previous = i + previous
#     i = i + previous
#     # previous = i
# print(list)

# 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21

# Get user input
N = int(input("Enter the number of Fibonacci numbers to generate: "))

# Initialize first two Fibonacci numbers
i = 1
previous = 1

# Print the first Fibonacci number
print(previous, end=" ")

# Generate and print the Fibonacci sequence
while N > 1:  # We already printed the first number, so loop N-1 times
    print(i, end=" ")  # Print the current Fibonacci number
    i, previous = previous, i + previous  # Update Fibonacci values
    N -= 1  # Decrease count
