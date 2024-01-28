# Input the dimensions of the matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Input the elements of the first matrix
print("Enter elements of the first matrix:")
matrix1 = [[int(input(f"Element at position ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

# Input the elements of the second matrix
print("Enter elements of the second matrix:")
matrix2 = [[int(input(f"Element at position ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

# Addition of matrices
sum_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

# Subtraction of matrices
difference_matrix = [[matrix1[i][j] - matrix2[i][j] for j in range(cols)] for i in range(rows)]

# Print the results
print("\nMatrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nAddition Result:")
for row in sum_matrix:
    print(row)

print("\nSubtraction Result:")
for row in difference_matrix:
    print(row)
