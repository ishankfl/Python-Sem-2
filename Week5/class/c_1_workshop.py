# matrix =[
#     [11,12,13],
#     [4,5,6],
#     [7,8,9]
# ]
# sum_of_diagonal=0
# for i in range(len(matrix)):
#     # print(matrix[i])
#     for j in range(len(matrix[i])):
#         # print(matrix[i][j])
#         if i == j:
#             sum_of_diagonal+= matrix[i][j]
#             # print(matrix[i][j],end=' ')
#         # if i<j:
#         #     print(matrix[i][j],end=' ')
#         # if i>j:
#         #     print(matrix[i][j],end=' ')
# print(sum_of_diagonal)

length_of_matrix = int(input("enter the length of rows: "))
matrix =[]
for i in range(length_of_matrix):
    # print(i)
    rows=[]
    for j in range(length_of_matrix):
        if i == j:
            rows.append(1)
        if i<j:
            rows.append(2)
        if j < i:
            rows.append(3)
    # print(rows)
    matrix.append(rows)

print(matrix)