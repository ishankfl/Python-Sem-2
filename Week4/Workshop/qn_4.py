# Initialize the first two numbers of the Fibonacci sequence
a = 0  # First number in the sequence (not printed)
b = 1  # Second number in the sequence
c = 1  # Third number in the sequence (used for calculations)

# Ask the user for the number of terms they want to generate
N = int(input("How many numbers? "))

# Print the Fibonacci sequence
print("Fibonacci sequence:")
for i in range(N):  # Loop N times to generate N terms
    print(c)  # Print the current Fibonacci number
    c = a + b  # Calculate the next Fibonacci number
    a = b  # Move 'a' one step forward
    b = c  # Move 'b' one step forward

