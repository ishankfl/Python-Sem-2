#Creation of empty text file
f = open("text.txt", "w")
f.close()


#create file and add some text there
f = open("text.txt", "w")
f.write("""""
Hello Ishan How are you?
"""
)

#now lets dive into deep: 
# Now we are storing data on textfile
# then access data from file and add those data to 2d array and update data

file = open("2-day-array.txt",'w')
file.write('''Name, Address, Number
Ishan, 123, 1234567890
Suyog, dharan, 9807015312
Geenesh, usa, +099sdf2234''')
file.close()

#we have added above data in txt file now read that data in visualization
#lets read data from file and add those data to 2d array and update data
file = open("2-day-array.txt",'r')
# print(file.readlines()) #using readlines function we can access the data for file after open and read line split the text of file in array by each by each lines
data = file.readlines()
print(data)
#now we have 4 item in array
# for each in data:
#     print(each)
    
#create a new list with empty data
new_data =[]
for each in data:
    new_data.append(each.replace('\n','').split(', ')) #split the data by comma and add to new list
# print(new_data) # this stores the all data on 2d array 

for each in range(len(new_data)):
    for new in range(len(new_data[each])):
        print(new_data[each][new], end='  |')
    print()