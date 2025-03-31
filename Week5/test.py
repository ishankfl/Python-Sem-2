rows = 4
matrix = []
for i in range(rows):
    rowss=[]
    for j in range(rows):
        if i == j:
            rowss.append(0)
        if i<j:
            rowss.append(1)
        if i > j:
            rowss.append(2)
    matrix.append(rowss)
print(matrix)
for i in matrix:
    print(i)