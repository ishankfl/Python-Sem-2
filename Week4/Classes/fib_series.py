# # # a = 0
# # # b = 1
# # # c = 1
# # # N = int(input("Enter a number: "))
# # # for i in range(N):
# # #     print(c)
# # #     c = a+b
# # #     a = b
# # #     b = c
# # a=0  
# # b = 1
# # c = 1
# # for i in range(10):
# #     print(c)
# #     c = a + b
# #     a = b
# #     b = c
# # #
# list1=[2,4,2,1,2,34,2]
# #sort using bubble sort
# for i in range(len(list1)):
#     for j in range(0,len(list1)-i-1):
#         if list1[j]>list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print("List in ascending order: ", list1)

# for i in range(len(list1)):
#     for j in range(0,len(list1)-i-1):
#         if list1[j]<list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print("List is descending order: ", list1)