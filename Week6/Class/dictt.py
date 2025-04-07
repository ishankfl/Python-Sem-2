# dict2={
#     "list":[1,2,3,4],
    
# }
# print(dict2['list'])
# dict2['hello']="hi"

N = int(input("Enter the number of students: "))
student_dict = {}
for i in range(N):
    name = input(f"Enter a name of {i+1} student ")
    marks = int(input(f"Enter marks obtained "))
    student_dict[name] = marks
#printing dictionary
print(student_dict)

print("Only Name of student: ")
print(student_dict.keys())