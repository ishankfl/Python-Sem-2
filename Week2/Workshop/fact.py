number = int(input("Hello number: "))
fact = 1
while(number > 0):
    # print(number)
    fact = fact * number
    number = number - 1
    # print(number)
print(fact)