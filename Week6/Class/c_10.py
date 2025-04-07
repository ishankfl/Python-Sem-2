# matrix =[
#     [24,3,6],
#     [8,12,18],
#     [2,66,7]
# ]
# max_sum=matrix[0][0]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j]%2==0 and matrix[i][j]%3==0:
#             print(matrix[i][j])
        
#         if matrix[i][j] > max_sum:
#             max_sum = matrix[i][j]
# print('max_sum ',max_sum)

#2
# N = int(input("Enter a number of students: "))
# marks_student={}
# for i in range(N):
#     name = input(f"Enter the name of {i+1} student: ")
#     marks = int(input (f"Marks of {name}: "))
#     marks_student[name] = marks
# print(marks_student)
# print(marks_student.keys())
# print(marks_student.values())
# for key,value in marks_student.items():
#     print(f"Name: {key} -> Marks {value}")