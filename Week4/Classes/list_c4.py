#1

N = int(input("Enter total number: "))
list =[]
for i in range(1,N+1):
    number = int(input(f"Enter {i} number : "))
    list.append(number)
print(list) #[2,5,4,5,6]
odd_sum = 0
even_sum = 0
for i in list:
    if i % 2 == 0:
        print(f"{i} is even number")
        even_sum = even_sum + i
    else:
        print(f"{i} is odd number")
        odd_sum = odd_sum + i
print("Even sum", even_sum)
print("Odd sum", odd_sum)