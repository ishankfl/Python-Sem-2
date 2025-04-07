list_student=[
    ["name", "maths", "english", "physics", "computer", "nepali"],
    ["Rohan", 85, 90, 78, 92, 88],
    ["Aryan", 90, 85, 92, 88, 78],
    ["Aman", 92, 88, 78, 90, 85],
]

for i in range(1,len(list_student)):
    summ = 0
    for j in range(0,len(list_student[i])):
        summ+=list_student[i][j]
        print
print(summ)