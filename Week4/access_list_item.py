# Access List Items using Indexing
list_item = [2, 3, 4, 5, 6, 7]

print(list_item[2])   # Output: 4
print(list_item[-6])  # Output: 2
print(list_item[-1])  # Output: 7 (Last item of the list)


# Using List Comprehension to filter items greater than 5
filtered_list = [i for i in list_item if i > 5]
print(filtered_list)  # Output: [6, 7]

# Using List Slicing
num_list = [1, 2, 3, 4, 5]

print(num_list[1:4])  # Output: [2, 3, 4] (Index 1 to 3)
print(num_list[0:2])  # Output: [1, 2] (Index 0 to 1)

# Using Loop to iterate over a list
for item in num_list:
    print(item)

# Output:
# 1
# 2
# 3
# 4
# 5

# Using range() to iterate with index
for i in range(len(list_item)):
    print(list_item[i])

# Output:
# 2
# 3
# 4
# 5
# 6
# 7
