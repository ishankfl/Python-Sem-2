# Prompt the user to enter the number of rows and columns for the matrix
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Initialize an empty list to store the matrix
matrix = []

# Loop through each row index from 0 to (rows - 1)
for i in range(rows):
    inner_list = []  # Create an empty list for the current row
    
    # Loop through each column index from 0 to (columns - 1)
    for j in range(columns):
        if i == j:  # If row index equals column index (diagonal element)
            inner_list.append(1)  # Assign 1 to diagonal elements
        elif i < j:  # If row index is less than column index (upper triangle)
            inner_list.append(1)  # Assign 1 to upper triangular elements
            
        else:  # If row index is greater than column index (lower triangle)
            inner_list.append(3)  # Assign 2 to lower triangular elements
    
    # Add the completed row (inner_list) to the matrix
    matrix.append(inner_list)

# Print the matrix row by row
for each in matrix:
    print(each)
