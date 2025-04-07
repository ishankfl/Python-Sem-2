# N = int(input("Enter a number of total students: "))
# marks_dict={}
# for i in range(N):
#     print(i)
#     key = input(f"Enter the name of {i+1} student: ")
#     value= int(input(f"Marks obtained by {key}: "))
#     marks_dict[key]=value
# print(marks_dict)
# for i,j in marks_dict.items():
#     print(f"Name: {i}: Marks:{j}")
# # print(marks_dict.values())
# print(f"Max marks: ",max(marks_dict.values()))
# print(f"Min marks: ",min(marks_dict.values()))
# sum_of_all = sum(marks_dict.values())
# average=sum_of_all/len(marks_dict.values())
# print(f"Average of all students: {average}")

list_student=[
    ["name", "maths", "english", "physics", "computer", "nepali"],
    ["Rohan", 70, 90, 78, 92, 88],
    ["Aryan", 60, 85, 92, 88, 78],
    ["Aman", 50, 88, 78, 90, 85],
]
for i in range(1,len(list_student)): #0,1,2,3
    marks_sum = 0
    for j in range(1,len(list_student[i])):
        marks_sum+=list_student[i][j]
    print(f"Name: {list_student[i][0]} Average Marks: {marks_sum/len(list_student[i])-1}")