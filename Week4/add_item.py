# Adding Items to a List in Python

# 1. Using `append()`: Adds a single element to the end of the list.
items = [1, 2, 3]
items.append(4)  # Adds 4 to the end of the list
print(items)  # Output: [1, 2, 3, 4]

# 2. Using `insert()`: Inserts an item at a specific index.
items = [1, 2, 3]
items.insert(1, 4)  # Inserts 4 at index 1
print(items)  # Output: [1, 4, 2, 3]

# 3. Using `extend()`: Adds multiple items (another list) to the end of the list.
items = [1, 2, 3]
items.extend([4, 5])  # Adds all elements from the list [4, 5]
print(items)  # Output: [1, 2, 3, 4, 5]

# 4. Using List Concatenation: Adds items by concatenating lists.
items = [1, 2, 3]
items = items + [4]  # Adds 4 to the list
print(items)  # Output: [1, 2, 3, 4]

# 5. Using List Comprehension: Adds elements based on conditions or logic.
items = [1, 2, 3]
items = [item * 2 for item in items]  # Multiply each element by 2 and create a new list
print(items)  # Output: [2, 4, 6]

# Example: Adding an item using append
items = [1, 2, 3]
new_item = 4
items.append(new_item)  # Adds 4 to the list
print(items.count(items))  # Output: [1, 2, 3, 4]
