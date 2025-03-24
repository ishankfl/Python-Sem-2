N = int(input("Enter a number: "))

if N ==2:
    print([1,1])
else:
    fib_series = [1,1]
    for i in range(N-2):
        fib_series.append(fib_series[-1]+fib_series[-2])
print(fib_series)