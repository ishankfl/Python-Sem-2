# # # list1=[[1,2],[3,4]]
# # # for i in range(len(list1)):
# # #     for j in range(len(list1[i])):
# # #         print(list1[i][j])

# # rows = int(input("Enter the number of rows: "))
# # matrix = []
# # for i in range(rows):
# #     new_rows=[]
# #     for j in range(rows):
# #         if i==j:
# #             new_rows.append(1)
# #         if i<j:
# #             new_rows.append(2)
# #         if i>j:
# #             new_rows.append(3)
# #     matrix.append(new_rows)
# # print("our matrix: ",matrix)
# # for each in matrix:
# #     print(each)

# A = [
#     [2,3,4],
#     [1,5,6],
#     [5,8,5]
# ]
# sumofdiagonal=0
# sumbelowdiagonal=0
# sumabovediagonal=0
# for i in range(len(A)):
#     print(A[i])
#     for j in range(len(A[i])):
#         if i == j:
#             sumofdiagonal += A[i][j]
#         if i < j:
#             sumabovediagonal += A[i][j]
#         if i>j:
#             sumbelowdiagonal+= A[i][j]
            
# print('sumofdiagonal',sumofdiagonal)
# print('sumabovediagonal',sumabovediagonal)
# print('sumbelowdiagonal',sumbelowdiagonal)
    
#bubble sort

# list1= [4,3,2,1]
# for i in range(len(list1)):
#     for j in range(0,len(list1)-1-i):
#         if list1[j]>list1[j+1]: 
#             list1[j], list1[j+1] = list1[j+1],list1[j]
list2=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
] ## 3 X 3
diagonal_sum = 0
below_diagonal_sum = 0
after_diagonal_sum = 0

for i in range(len(list2)):
    for j in range(len(list2[i])):
        if i == j:
            print(list2[i][j])
            diagonal_sum = diagonal_sum + list2[i][j]
print("sum of diagonal ",diagonal_sum)

#2num
matrix=[]
rows = int(input("Enter the size of matrix: "))
for i in range((rows)):
    each_row=[]
    for j in range((rows)):
        if i == j:
            each_row.append(1)
        if i<j:
            each_row.append(2)
        if i>j:
            each_row.append(3)
    print(each_row)