list =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in list:
    print(i)
sum_of_diagonal=0
for i in range(len(list)):
    for j in range(len(list[i])):
        if i == j:
            print(list[i][j],end=" ")
            sum_of_diagonal+=list[i][j]
print(sum_of_diagonal)
    # print()