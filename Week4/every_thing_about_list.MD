# List in Python

A **list** in Python is a collection of ordered, mutable (changeable) elements. Lists allow duplicate values and can store different types of data (integers, strings, floating-point numbers, etc.).

## Creating a List

```python
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

## Accessing List Elements

### Using Indexing
```python
print(my_list[0])  # Output: 1
print(my_list[-1]) # Output: 5 (Last element)
```

### Using Slicing
```python
print(my_list[1:4])  # Output: [2, 3, 4]
print(my_list[:3])   # Output: [1, 2, 3]
print(my_list[2:])   # Output: [3, 4, 5]
```

## Modifying Lists

### **Updating Elements**
```python
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]
```

### **Appending Elements**
```python
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]
```

### **Inserting Elements**
```python
my_list.insert(2, 99)
print(my_list)  # Output: [1, 2, 99, 10, 4, 5, 6]
```

### **Removing Elements**
#### Using `remove()` (Removes first occurrence of a value)
```python
my_list.remove(10)
print(my_list)  # Output: [1, 2, 99, 4, 5, 6]
```

#### Using `pop()` (Removes and returns element at a specific index)
```python
removed_element = my_list.pop(3)
print(removed_element)  # Output: 4
print(my_list)          # Output: [1, 2, 99, 5, 6]
```

#### Using `del` (Deletes an element or the entire list)
```python
del my_list[2]  # Deletes the third element
print(my_list)   # Output: [1, 2, 5, 6]

del my_list  # Deletes the entire list
```

## List Operations

### **Concatenation**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]
```

### **Repetition**
```python
repeated_list = [1, 2] * 3
print(repeated_list)  # Output: [1, 2, 1, 2, 1, 2]
```

### **Checking Membership**
```python
print(3 in my_list)  # Output: True
print(7 in my_list)  # Output: False
```

## Useful List Functions

### **Finding Maximum and Minimum Values**
```python
numbers = [5, 10, 2, 8, 3]
print(max(numbers))  # Output: 10
print(min(numbers))  # Output: 2
```

### **Sorting a List**
#### Using `sort()` (Modifies the original list)
```python
numbers.sort()
print(numbers)  # Output: [2, 3, 5, 8, 10]
```

#### Using `sorted()` (Returns a new sorted list)
```python
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [10, 8, 5, 3, 2]
```

### **Reversing a List**
```python
numbers.reverse()
print(numbers)  # Output: [10, 8, 5, 3, 2]
```

## Iterating Through a List

### **Using a `for` Loop**
```python
for num in numbers:
    print(num)
```

### **Using List Comprehension**
```python
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64, 100]
```

## Copying a List

```python
original = [1, 2, 3]
copied = original.copy()
print(copied)  # Output: [1, 2, 3]
```

## Clearing a List
```python
numbers.clear()
print(numbers)  # Output: []
```

## Conclusion
Lists are one of the most versatile and widely used data structures in Python. Understanding how to manipulate lists efficiently will greatly improve your coding skills. Mastering list operations, methods, and comprehension allows you to write more efficient and readable Python code!

