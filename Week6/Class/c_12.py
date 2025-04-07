# # A =[
# #     [24,3,6],
# #     [8,12,18],
# #     [2,66,7]
# # ]
# # max_num=A[0][0]
# # min_num=A[0][0]
# # for i in range(len(A)):
# #     for j in range(len(A[i])):
# #         # if A[i][j]%2==0 and A[i][j]%3==0:
# #         #     print(A[i][j])
# #         # if i == j:
# #         #     print(A[i][j])
# #         if A[i][j] > max_num:
# #             max_num = A[i][j]
        
# #         if A[i][j]< min_num:
# #             min_num=A[i][j]
# # print("max_num", max_num)
# N = int(input("Enter the number of students: "))
# marks_student={}
# for i in range(N): 
#     name= input(f"Enter a name of {i+1} student: ")
#     marks = int(input(f"Marks obtained by {name}: "))
#     marks_student[name] = marks
# print(marks_student)
# print(marks_student.keys())
# print(marks_student.values())
# for key,value in marks_student.items():
#     print(f"Name: {key} Marks: {value}") 