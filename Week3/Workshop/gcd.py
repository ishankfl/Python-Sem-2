M = int(input("Enter a number: "))
N = int(input("Enter second number: "))

while N!=0 and M%N!=0:
    M = N
    N = M%N
print(N)