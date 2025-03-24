# Write a program that takes N numbers as input from a user and puts them in a list. Then the program should find out the sum of all the odd numbers and the sum of all the even numbers from the list and print them out. 

# The program should also print out the count of odd numbers and the count of even numbers.

N = int(input("Enter a number do you want to calculate: "))
numbers = []
for i in range(N):
    numbers.append(int(input("Enter a number: ")))

odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0

# Loop through the list of numbers and check if each number is odd or even. If it's
# odd, add it to the odd_sum and increment the odd_count. If it's even,
# add it to the even_sum and increment the even_count.
for num in numbers:
    if num % 2 == 0:
        even_sum += num
        even_count += 1
    else:
        odd_sum += num
        odd_count += 1

# Print out the sum of odd numbers, the sum of even numbers, the count of odd numbers
# and the count of even numbers.
print("Sum of odd numbers: ", odd_sum)
print("Count of odd numbers: ", odd_count)
print("Sum of even numbers: ", even_sum)
print("Count of even numbers: ", even_count)