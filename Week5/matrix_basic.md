# Python Matrix Comprehension and Operations

## Introduction
A matrix in Python is represented as a list of lists. Instead of using one-liner list comprehensions, we will use explicit loops for better readability.

---

## 1. Creating a Matrix
A matrix is a 2D list where each row is a list. We can create an `m x n` matrix using nested loops.

```python
# Creating a 3x3 matrix filled with zeros
matrix = []
for _ in range(3):
    row = []
    for _ in range(3):
        row.append(0)
    matrix.append(row)

print(matrix)
```

### Output:
```
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## 2. Matrix with Incremental Values
To create a matrix with sequential numbers, use nested loops.

```python
# Creating a 3x3 matrix with incremental values
matrix = []
value = 1
for i in range(3):
    row = []
    for j in range(3):
        row.append(value)
        value += 1
    matrix.append(row)

print(matrix)
```

### Output:
```
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

## 3. Populating a Matrix Dynamically
A matrix can be filled with values based on a formula.

```python
# Creating a 3x3 matrix with row * col values
matrix = []
for row in range(3):
    row_list = []
    for col in range(3):
        row_list.append(row * col)
    matrix.append(row_list)

print(matrix)
```

### Output:
```
[[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

---

## 4. Identity Matrix
An identity matrix has 1s on the diagonal and 0s elsewhere.

```python
size = 3
identity_matrix = []
for row in range(size):
    row_list = []
    for col in range(size):
        if row == col:
            row_list.append(1)
        else:
            row_list.append(0)
    identity_matrix.append(row_list)

print(identity_matrix)
```

### Output:
```
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

---

## 5. Matrix Transposition
Swapping rows and columns of a matrix.

```python
# Transposing a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = []
for i in range(len(matrix[0])):  # Loop over columns
    row = []
    for j in range(len(matrix)):  # Loop over rows
        row.append(matrix[j][i])
    transpose.append(row)

print(transpose)
```

### Output:
```
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

---

## 6. Sum of Two Matrices
Matrix addition involves adding corresponding elements.

```python
# Adding two 3x3 matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []
for i in range(len(matrix1)):  # Loop over rows
    row = []
    for j in range(len(matrix1[0])):  # Loop over columns
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print(result)
```

### Output:
```
[[10, 10, 10], [10, 10, 10], [10, 10, 10]]
```

---

## 7. Conclusion
- We learned how to **create**, **populate**, **transpose**, and **add** matrices.
- Using nested loops instead of one-liner list comprehensions improves readability.
- Matrices are essential in various applications like image processing, machine learning, and scientific computing.

---
