A =[
    [24,3,6],
    [8,12,18],
    [2,66,7]
]
max_num=A[0][0]
min_num=A[0][0]
for i in range(len(A)):
    for j in range(len(A[i])):
        item = A[i][j]
        if item%2==0 and item %3==0:
            print(item)
        
        if item > max_num:
            max_num = item
print('max_num ',max_num)