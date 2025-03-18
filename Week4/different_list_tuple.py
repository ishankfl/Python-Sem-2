# Comparing Lists and Tuples in Python

# 1. Lists and Tuples both support indexing
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# Accessing elements via index
print("Indexing Example:")
print(my_list[0])  # Output: 1
print(my_tuple[0])  # Output: 1

# 2. Lists and Tuples both support slicing
print("\nSlicing Example:")
print(my_list[1:3])  # Output: [2, 3]
print(my_tuple[1:3])  # Output: (2, 3)

# 3. Lists and Tuples both support concatenation using + operator
print("\nConcatenation Example:")
print(my_list + [4])  # Output: [1, 2, 3, 4]
print(my_tuple + (4,))  # Output: (1, 2, 3, 4)

# 4. Lists and Tuples both support repetition using * operator
print("\nRepetition Example:")
print([1] * 3)  # Output: [1, 1, 1]
print((1,) * 3)  # Output: (1, 1, 1)

# 5. Checking Membership (in) in both Lists and Tuples
print("\nMembership Example:")
print(2 in my_list)  # Output: True
print(2 in my_tuple)  # Output: True

# 6. Length of List and Tuple
print("\nLength Example:")
print(len(my_list))  # Output: 3
print(len(my_tuple))  # Output: 3

# 7. Mutability
# Lists are mutable - you can change their content
print("\nMutable List Example:")
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]

# Tuples are immutable - you cannot change their content
print("\nImmutable Tuple Example:")
# The following line will raise an error:
# my_tuple[0] = 10  # Uncommenting this line will cause a TypeError

# 8. List methods vs Tuple methods
print("\nList and Tuple Methods Example:")
# Lists have more methods like append(), remove(), etc.
my_list.append(4)
print("Updated List:", my_list)  # Output: [10, 2, 3, 4]

# Tuples have only a few methods like count() and index()
print("Tuple count of 2:", my_tuple.count(2))  # Output: 1
print("Tuple index of 3:", my_tuple.index(3))  # Output: 2
