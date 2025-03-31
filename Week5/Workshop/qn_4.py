# # 4. Write a program that takes as input the names and marks obtained on a
# # certain subject of N students. Then the data must be stored in a dictionary
# # with the names as keys and marks as values. Then find out the highest,
# # lowest and average marks obtained and print them out.

# student_number = int(input("Enter the number of students: "))
# student_marks=[]
# for i in range(student_number):
#     student_name = input(f"Enter the name of {i+1} student: ")
#     marks= int(input(f"Enter marks of {student_name}: "))
#     dictionary={student_name:marks}
#     student_marks.append(dictionary)
# print(student_marks)
# higest_marks = 0
# lowest_marks = 0
# sum_totalmarks=0
# average_marks = 0
# for each in student_marks:
#     print(each)
#     if each['Ishan'] > higest_marks:
#         higest_marks = each['Ishan']
    
#     if each['Ishan'] < lowest_marks:
#         lowest_marks = each['Ishan']
#     sum_totalmarks += each['Ishan']

# average_marks = sum_totalmarks/student_number

# print("Higest Marks: ", higest_marks)
# print("Lowest Marks: ", lowest_marks)
# print("Average marks: ", average_marks)
"""""""""'""""""""""""'""""""""""""'""""""""""""'""""""""""""'""""""""""""'""""""""""""'"""

    
# Get the number of students
num_students = int(input("Enter the number of students: "))

# Dictionary to store student marks
student_marks = {}

# Taking input from the user
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))  # Allow float for decimal marks
    student_marks[name] = marks  # Store in dictionary

# Calculate highest, lowest, and average marks
highest_marks = max(student_marks.values())  # Maximum marks
lowest_marks = min(student_marks.values())   # Minimum marks
average_marks = sum(student_marks.values()) / num_students  # Average marks

# Display results
print("\nStudent Marks:", student_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", round(average_marks, 2))  # Rounded to 2 decimal places
