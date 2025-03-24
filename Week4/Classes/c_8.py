# print(list(set(number)))
number = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6] 
unique_list = []
for i in number:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
        