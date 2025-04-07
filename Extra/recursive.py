#Example of recursive
# with open("hello.txt", "w") as file:
#     file.write("Hello, World!")

def sum_of_n(n):
    if n == 1:
        return 1
    return n + sum_of_n(n-1)

print(sum_of_n(5)) # Output: 15

stri={'hi':'value','hlow':'pppp'}
stri.popitem()
print(stri)
