# Removing items from a list in different ways

# Using remove() to remove a single item
items = [1, 3, 2, 3, 3, 4, 3]
items.remove(3)  # Removes the first occurrence of 3
print(items)  # Output: [1, 2, 3, 3, 4, 3]

# Note: remove() only accepts one argument, and you can't pass multiple parameters like items.remove(1, 2, 3).
# You can remove multiple occurrences using a loop if needed.
# Example to remove all 3s:
items = [1, 3, 2, 3, 3, 4, 3]
while 3 in items:
    items.remove(3)  # Removes all occurrences of 3
print(items)  # Output: [1, 2, 4]

# Using filter() to remove multiple items based on a condition
items = [1, 3, 2, 3, 3, 4, 3]
items = list(filter(lambda x: x != 3, items))  # Removes all occurrences of 3
print(items)  # Output: [1, 2, 4]

# Using pop() to remove by index
# pop() removes the item at the specified index, or removes the last item if no index is provided
items = [1, 3, 2, 3, 3, 4, 3]
items.pop(0)  # Removes the first item (index 0)
print(items)  # Output: [3, 2, 3, 3, 4, 3]
items.pop()  # Removes the last item
print(items)  # Output: [3, 2, 3, 3, 4]

# Using del() to remove by index
a = [10, 20, 30, 40, 50]
del a[2]  # Removes the element at index 2 (which is 30)
print(a)  # Output: [10, 20, 40, 50]
