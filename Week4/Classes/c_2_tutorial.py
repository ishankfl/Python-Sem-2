a = int(input("Enter any number: "))
if a == 2:
    print("The number is prime num")
else:
    i = 2
    is_prime = True
    while(i <= a/2):
        if(a%i == 0):
            print("Not prime")
            is_prime = False
        i=i+1
    if is_prime == False:
        print("The number is not prime num")
    else:
        print("The number is prime num")