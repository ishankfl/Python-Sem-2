# # # list = [8,10, 4,5,7,8,2]
# # # for i in range(len(list)):
# # # 	for j in range(0, len(list)-i-1):
# # # 		if list[j] > list[j+1]:
# # # 			list[j], list[j+1] = list [j+1],list[j]
# # # print(list)

# # # lists=[34,2,3,1,2,3,4,10,34]
# # # for i in range(len(lists)):
# # #     for j in range(len(lists)-1):
# # #         if lists[j]> lists[j+1]:
# # #             lists[j],lists[j+1]=lists[j+1],lists[j]
# # # print(lists)

# # list = [10,1,2,3,4,1,1]
# # for i in range(1,len(list)):
# #     for j in range(i-1):
# #         if list[j] 

# #insertion sort
# list = [10, 1, 2, 3, 4, 1, 1]

# for i in range(1, len(list)):  # Start from the second element
#     for j in range(i, 0, -1):  # Compare the current element with previous elements
#         if list[j] < list[j - 1]:  # If current element is smaller than the previous one
#             list[j], list[j - 1] = list[j - 1], list[j]  # Swap the elements
#         else:
#             break  # No need to check further if the elements are in order

# print("Sorted list:", list)

def second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two numbers."
    
    first = second = float('-inf')  # Initialize first and second largest as negative infinity
    print(first,second)
    # print(first<-1000)
    for num in numbers:
        if num > first:
            second = first  # Update second largest
            print(second)
            first = num  # Update first largest
        elif num > second and num != first:
            second = num  # Update second largest if it's smaller than first but greater than second
    
    return second if second != float('-inf') else "No second largest number found."

# Example usage
numbers = [10, 5, 8, 20, 15]
print("Second largest number is", second_largest(numbers))
