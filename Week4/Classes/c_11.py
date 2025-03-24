No = int(input("How many numbers do you want to calculate? "))
numbers = []
for i in range(No):
    a = int(input("enter a number: "))
    numbers.append(a)
print("List ", numbers)
even_sum = 0
odd_sum = 0
for each in numbers:
    # print(each)
    if each % 2 == 0:
        print(f"{each} is even number")
        even_sum += each
    else:
        odd_sum += odd_sum
        
print(f"Even sum {even_sum}, Odd Sum {odd_sum}")