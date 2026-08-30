import sympy as sp

n = int(input("Enter the size of the matrix: "))

matrix = []

print("Enter the matrix:")
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix.append(row)

A = sp.Matrix(matrix)

rref_matrix, pivot_columns = A.rref()

print("\nReduced Row Echelon Form:")
sp.pprint(rref_matrix)
