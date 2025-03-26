# a = 1
# b = 1
# c = 0
# for i in range(10):
#     print(c)
#     c = a + b
#     a = b 
#     b = c

rows = int(input("enter the number of rows: "))
column = int(input("enter the number of cloumn: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(column):
        if i == j:
            row.append(1)
        if i > j:
            row.append(0)
        if j > i:
            row.append(0)
    matrix.append(row)
print(matrix)
for each in matrix:
    print(each)  # print each row of the matrix