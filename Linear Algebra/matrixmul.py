import numpy as np

rows = int(input("Enter length of rows: "))
column = int(input("Enter length of column: "))


matrix1 = []
for i in range(rows):
    row = list(map(int , input(f"enter row {i+1}: ").split()))
    if len(row) != column:
        print("invalid")
        exit 
    matrix1.append(row)

matrix2 = []
rows2 = int(input("Enter length of rows: "))
column2 = int(input("Enter length of column: "))

for j in range(rows2):
    row = list(map(int , input(f"enter row {i+1}: ").split()))
    if len(row) != column2:
        print("invalid")
        exit 
    matrix2.append(row)

a = np.dot(matrix1, matrix2)
print(a)   