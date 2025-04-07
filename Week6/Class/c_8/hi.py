A =[
    ['name','maths', 'english','physics','computer','nepali'],
    ['john', 88, 86, 76, 66, 76],
    ['peter', 92, 90, 80, 70, 80],
    ['anna', 88, 86, 76, 66, 76],
]
for i in range(1,len(A)):
    name = A[i][0]
    sum = 0
    for j in range(1,len(A[i])):
        sum = sum + A[i][j]
    average = sum / (len(A[i])-1)
    print(f"Marks obtained by {name} is {average}")