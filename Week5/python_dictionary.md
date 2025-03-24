# Introduction to Python Dictionaries

## What is a Dictionary in Python?
A dictionary in Python is an unordered collection of key-value pairs. It is defined using curly braces `{}` and allows fast lookups, insertions, and deletions.

### Syntax:
```python
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
```

## Creating Dictionaries
You can create dictionaries in several ways:

### Using Curly Braces `{}`:
```python
person = {"name": "Alice", "age": 30}
```

### Using the `dict()` Constructor:
```python
person = dict(name="Alice", age=30)
```

### Creating an Empty Dictionary:
```python
empty_dict = {}
```

### Creating a Dictionary with `zip()`:
```python
keys = ["name", "age", "city"]
values = ["Bob", 28, "Chicago"]
person = dict(zip(keys, values))
```

## Accessing Values
You can access dictionary values using keys.

```python
print(person["name"])  # Output: Alice
```

Using `get()` to avoid errors:
```python
print(person.get("age", "Not Found"))  # Output: 30
print(person.get("gender", "Not Found"))  # Output: Not Found
```

Using `setdefault()` to set a default value if a key does not exist:
```python
person.setdefault("gender", "Unknown")  # Adds "gender": "Unknown" if not present
```

## Modifying Dictionaries

### Adding New Key-Value Pairs:
```python
person["gender"] = "Female"
```

### Updating Existing Keys:
```python
person["age"] = 31
```

### Removing Items:
```python
del person["age"]
age = person.pop("name")  # Removes and returns the value
```

## Dictionary Methods

| Method | Description |
|--------|-------------|
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns all key-value pairs |
| `update(dict2)` | Updates dictionary with another dictionary |
| `pop(key)` | Removes and returns value of given key |
| `popitem()` | Removes and returns last inserted key-value pair |
| `clear()` | Removes all elements from dictionary |
| `copy()` | Returns a shallow copy of the dictionary |
| `fromkeys(keys, value)` | Creates a dictionary from keys with a common value |

### Example Usage:
```python
d = {"a": 1, "b": 2, "c": 3}
print(d.keys())    # Output: dict_keys(['a', 'b', 'c'])
print(d.values())  # Output: dict_values([1, 2, 3])
print(d.items())   # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
```

## Dictionary Comprehension
You can create dictionaries dynamically using dictionary comprehension.

```python
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Filtering in Dictionary Comprehension:
```python
even_squares = {x: x*x for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

## Nested Dictionaries
Dictionaries can contain other dictionaries.

```python
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}
print(students["Alice"]["grade"])  # Output: A
```

## Iterating Over Dictionaries

### Iterating Over Keys:
```python
for key in person.keys():
    print(key)
```

### Iterating Over Values:
```python
for value in person.values():
    print(value)
```

### Iterating Over Key-Value Pairs:
```python
for key, value in person.items():
    print(f"{key}: {value}")
```

## Dictionary Comparison
Dictionaries can be compared using equality operators:
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(dict1 == dict2)  # Output: True (order doesn't matter)
```

## Merging Dictionaries

### Using `update()`:
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Using `|` Operator (Python 3.9+):
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## Conclusion
Python dictionaries are powerful data structures that provide fast and flexible mappings of keys to values. They support various operations and methods, making them essential in Python programming. Mastering dictionaries can help you write efficient and effective code.

