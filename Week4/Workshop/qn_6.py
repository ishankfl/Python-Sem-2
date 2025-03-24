# Write a program creates and prints a new list with the elements of an existing list in reverse order.
# [1, 2, 3, 4, 5, 6] -> [6, 5, 4, 3, 2, 1]

A = [1, 2, 3, 4, 5, 6]
A_reversed = []

for i in range(len(A) - 1, -1, -1):  # Loop backward through the list
    A_reversed.append(A[i])

print(A_reversed)
