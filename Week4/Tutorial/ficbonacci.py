number = 10

if number <= 1:
    print ([1])

else:
    next_number = 1
    fibonacci_series = [1,1]
    while fibonacci_series[-1] + fibonacci_series[-2] < number:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)
    print(fibonacci_series)