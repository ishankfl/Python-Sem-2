# # print(list(set(items)))
# items = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]
# unique_list = []
# for i in items:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)



items = [1,2,3,4,5,6]
reverse_ = []
for i in range(len(items)-1,-1, -1):
    # print(i)
    print(items[i])
    reverse_.append(items[i])