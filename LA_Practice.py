# practical 2 
# u = list(map(float , input("enter u: ").split()))
# v = list(map(float , input("Enter v :").split()))
# a = 5
# b = 3

# dot = 0
# for i in range(len(u)):
#     dot += u[i] * v[i]

# for i in range(len(v)):
#     scalr += a*u[i] + b*v[i]

# Practical 3
# import numpy as np
# r = int(input("Enter no of rows of matrix: "))
# c = int(input("Enter no of columns of matrix: "))

# matrix = []
# for i in range(r):
#     row = list(map(int , input(f"enter row {i+1} : ").split()))
#     matrix.append(row)
# matrix = np.array(matrix)
# for i  in range(r):
#     print(matrix[i])
# for i in range(c):
#     print(matrix[:,i])
# print(matrix.T)
# scalar = 9
# print(scalar * matrix)

# Practical 4
# import numpy as np
# v = list(map(int , input("enter the vector : ").split()))
# c = int(input("Enter no of cols: "))
# matrix = []
# for i in range(len(v)):
#     r = list(map(int ,input(f"enter row {i+1} : ").split()))
#     matrix.append(r)

# print("vector X matrix")
# print(np.dot(v ,matrix))

# c1 = int(input("enter no of columns"))
# matrix1 = []
# for i in range(c):
#     r = list(map(int , input(f"enter row {i+1} :").split()))
#     matrix1.append(r)

# print("matrix x matrix")
# print(np.dot(matrix,matrix1))

# Practical 5
import numpy as np
r = int(input("Enter the no of rows :"))
matrix = []
for i in range(r):
    row = list(map(int , input(f"enter the row {i + 1} : ").split()))
    matrix.append(row)

matrix = np.array(matrix)

a = int(np.linalg.det(matrix))
print("determinant :" , a)
if a == 0:
    print("invalid")
else:
    print("Inverse : " , np.linalg.inv(matrix))