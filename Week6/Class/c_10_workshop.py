list_student=[
    ["name", "maths", "english", "physics", "computer", "nepali"],
    ["Rohan", 1, 2, 3, 4, 5],
    ["Aryan", 0, 5, 2, 8, 8],
    ["Aman", 0, 8, 8, 0, 5],
]
sum = 0
for i in range(1,len(list_student)):
    sum = 0
    for j in range(1,len(list_student[i])):
        # print(list_student[i][j])
        sum+=list_student[i][j]
    print(list_student[i][0],sum/(len(list_student[i])-1))