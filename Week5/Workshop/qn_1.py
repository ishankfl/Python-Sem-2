# Original list with duplicate elements
list_ = [0, 1, 3, 2, 1, 2, 3, 4, 6, 3, 5, 6, 1, -100]

# Convert list to a set to remove duplicate elements, then back to a list
list_ = list(set(list_))

# Bubble Sort Algorithm to sort the list in descending order
for i in range(len(list_) - 1):  # Outer loop for passes
    for j in range(len(list_) - 1 - i):  # Inner loop for swapping
        if list_[j] < list_[j + 1]:  # Swap if the next element is larger
            list_[j], list_[j + 1] = list_[j + 1], list_[j]

# Print the sorted list in descending order
print("Sorted Unique List (Descending):", list_)

# =============================================
# Sorting Another List in Descending Order
# =============================================

items = [1, 2, 4, 3, 2, 1, 5, 6]

for i in range(len(items)):  
    for j in range(0, len(items) - i - 1): 
        if items[j] <  items[j + 1]: 
            items[j], items[j + 1] = items[j + 1], items[j]

print("Sorted Items (Descending):", items)
