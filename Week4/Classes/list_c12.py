# # items = [1,2,3,4,5,"6"]
# # print(items)

# # # for each in items:
# # #     print(each)
# # for i in range(0,len(items)):
# #     # print(i)
# #     print(items[i])

# num = int(input("Enter a total number do you want to calculate: "))
# numbers = []
# for i in range(num):
#     a = int(input(f"Enter {i+1} number: "))
#     numbers.append(a)
# print(numbers) #[1,2,3,5,8]
# even_sum = 0
# odd_sum = 0
# for each in numbers:
#     if each % 2 == 0:
#         print(f"{each} is even")
#         even_sum= even_sum + each
#     else:
#         print(f"{each} is odd")
#         odd_sum = odd_sum + each
        
# print(odd_sum,even_sum)


num = int(input("Enter a total number do you want to calculate: "))
numbers = []
for i in range(num):
    a = int(input(f"Enter {i+1} number: "))
    numbers.append(a)
print(numbers)

max_num = numbers[0]
min_num = numbers[0]

