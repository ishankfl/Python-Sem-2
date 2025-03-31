# list1=[2,4,5,1]
# for i in range(len(list1)):
#     for j in range(0,len(list1)-1):
#         if list1[j]>list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print(list1)

list1 = [
    [1,2,3],
    [7,8,9],
    [10,12,13]
]
sum_of_diagonal=0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i == j:
            sum_of_diagonal+=list1[i][j]
        #     print(list1[i][j])
        # if i>j:
        #     print(list1[i][j])
    # print("row complete")
print(sum_of_diagonal)