#     | 24  3  6 |
# A = | 8  12 18 |
#     | 2  66  7 |


listA=[
    [24,3,6],
    [8,12,18],
    [2,66,7]
]

for i in range(len(listA)):
    print(listA[1])

    # print(listA[1])  # Output: [8, 12, 18]
    # print(listA[0])  # Output: [24, 3, 6
    # print(listA[2])  # Output: [2, 66, 7

for i in range(len(listA)):
    for j in range(len(listA[i])):
        print(listA[i][j])
        
        #output

        # print(listA[0][0]) #output 24
        # print(listA[0][1]) #output 3
        # print(listA[0][2]) #output 6
        # print(listA[1][0]) #output 8
        # print(listA[1][1]) #output 12
        # print(listA[1][2]) #output 18
        # print(listA[2][0]) #output 2
        # print(listA[2][1]) #output 66
        # print(listA[2][2]) #output 7
        
        
        # use below code for find the number if only divisible by 2 and 3
        number = listA[i][j]
        if number % 2 == 0 and number % 3 == 0:
            print(number)
        # if 