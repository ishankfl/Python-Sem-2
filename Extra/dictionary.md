# Python Dictionary Learning Guide

## 1. Introduction to Dictionaries
A dictionary in Python is a collection of key-value pairs. It is defined using curly braces `{}`.

```python
# Example of a dictionary
dict_example = {"name": "Alice", "age": 25, "city": "New York"}
print(dict_example)
```
**Output:**
```
{'name': 'Alice', 'age': 25, 'city': 'New York'}
```
---

## 2. CRUD Operations in a Dictionary

### Create (C) - Adding Data
```python
store = {}
store["name"] = "ABC Store"
store["location"] = "Kathmandu"
store["products"] = ["Milk", "Bread", "Eggs"]
print(store)
```
**Output:**
```
{'name': 'ABC Store', 'location': 'Kathmandu', 'products': ['Milk', 'Bread', 'Eggs']}
```

### Read (R) - Accessing Data
```python
print(store["name"])  # Output: ABC Store
print(store.get("location"))  # Output: Kathmandu
print(store.get("owner", "Not available"))  # Avoids KeyError
```
**Output:**
```
ABC Store
Kathmandu
Not available
```

### Update (U) - Modifying Data
```python
store["location"] = "Lalitpur"
store["owner"] = "John Doe"
print(store)
```
**Output:**
```
{'name': 'ABC Store', 'location': 'Lalitpur', 'products': ['Milk', 'Bread', 'Eggs'], 'owner': 'John Doe'}
```

### Delete (D) - Removing Data
```python
del store["owner"]
removed_value = store.pop("location")
print(removed_value)  # Output: Lalitpur
store.clear()
print(store)  # Output: {}
```
**Output:**
```
Lalitpur
{}
```
---

## 3. Looping Through a Dictionary

### Iterating Over Keys
```python
for key in store.keys():
    print(key)
```

### Iterating Over Values
```python
for value in store.values():
    print(value)
```

### Iterating Over Key-Value Pairs
```python
for key, value in store.items():
    print(f"{key}: {value}")
```

---

## 4. Common Dictionary Methods with Examples

### Getting Values Safely
```python
print(store.get("owner", "Not available"))
```
**Output:**
```
Not available
```

### Retrieving Keys, Values, and Items
```python
print(store.keys())
print(store.values())
print(store.items())
```
**Output:**
```
dict_keys(['name', 'location', 'products'])
dict_values(['ABC Store', 'Kathmandu', ['Milk', 'Bread', 'Eggs']])
dict_items([('name', 'ABC Store'), ('location', 'Kathmandu'), ('products', ['Milk', 'Bread', 'Eggs'])])
```

### Removing Elements
```python
location = store.pop("location", "Not Found")
print(location)
```
**Output:**
```
Kathmandu
```

### Updating Dictionary
```python
store.update({"owner": "John Doe"})
print(store)
```
**Output:**
```
{'name': 'ABC Store', 'products': ['Milk', 'Bread', 'Eggs'], 'owner': 'John Doe'}
```

### Clearing Dictionary
```python
store.clear()
print(store)
```
**Output:**
```
{}
```

### Setting Default Values
```python
owner = store.setdefault("owner", "Unknown")
print(owner)
```
**Output:**
```
Unknown
```

### Copying Dictionary
```python
store_copy = store.copy()
print(store_copy)
```
**Output:**
```
{}
```

### Removing Last Item
```python
last_item = store.popitem()
print(last_item)
```
**Output:**
```
('products', ['Milk', 'Bread', 'Eggs'])
```

### Creating Dictionary from Keys
```python
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print(new_dict)
```
**Output:**
```
{'a': 0, 'b': 0, 'c': 0}
```

---

## 5. Dictionary Comprehension
```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)
```
**Output:**
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
---

## 6. Nested Dictionaries
```python
students = {
    "Alice": {"age": 25, "grade": "A"},
    "Bob": {"age": 24, "grade": "B"}
}
print(students["Alice"]["grade"])  # Output: A
```
**Output:**
```
A
```
---

This guide covers all essential operations and functions of Python dictionaries! 🚀

