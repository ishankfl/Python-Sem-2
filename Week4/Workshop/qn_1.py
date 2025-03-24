# Write a program that takes a number N as input and prints the sum of all the numbers from 1 to N.
N = int(input("Enter a number do you want to caculcate sum: "))

sum = 0

while N>0:
    sum = sum + N
    N = N - 1

print("Sum of all numbers from 1 to", N, "is", sum)