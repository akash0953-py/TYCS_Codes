#Practical 1
# import numpy as np
# import matplotlib.pyplot as plt

# z1 = complex(3,2)
# z2 = complex(2,3)

# z_90 = z1 * 1j
# plt.scatter(z_90.real , z_90.imag)
# plt.show()

# plt.scatter(z1.real,z1.imag)
# plt.show()

# numbers = np.array([1+1j, 2+1j, 2+2j, 1+2j])

# # Original
# plt.scatter(numbers.real, numbers.imag)
# plt.xlabel("Real")
# plt.ylabel("Imaginary")
# plt.title("Original Complex Numbers")
# plt.grid()
# plt.show()



# practical 2 
# import numpy as np
# u = np.array(list(map(int , input("enter u: ").split())))
# v = np.array(list(map(int , input("Enter v :").split())))
# a = 5
# b = 3

# dot = 0
# scalr = 0
# dot = np.dot(u,v)
# scalr = a*u + b*v

# print( dot , " " ,scalr)



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
# import numpy as np
# r = int(input("Enter the no of rows :"))
# matrix = []
# for i in range(r):
#     row = list(map(int , input(f"enter the row {i + 1} : ").split()))
#     matrix.append(row)

# matrix = np.array(matrix)

# a = int(np.linalg.det(matrix))
# print("determinant :" , a)
# if a == 0:
#     print("invalid")
# else:
#     print("Inverse : " , np.linalg.inv(matrix))



# Practical 6 
# import sympy as sp 

# r = int(input("enter number of columns : "))
# matrix = []
# for i in range(r):
#     row = list(map(int , input(f"Enter the row {i + 1} : ").split()))
#     matrix.append(row)

# a = sp.Matrix(matrix)
# rref , pivot_clm = a.rref()

# print("Rref : " , rref)


# Practical 7 
# import numpy as np
# def projection(a,b):
#     result = (np.dot(a,b)/np.dot(b,b)) * b
#     print("Projection : ",result)

# a = np.array(list(map(int , input("Enter vector a : ").split())))
# b = np.array(list(map(int , input("Enter vector b : ").split())))

# while True:
#     choice = int(input("Enter ur choice \n 1.Projection a on b \n Projection b on b \n Exit on 3 \n"))
#     if choice == 1:
#         projection(a,b)
#     elif choice ==2:
#         projection(b,a)
#     elif choice == 3:
#         break
#     else:
#         print("Invalid")

# practical 10
# import numpy as np

# a = int(input("enter scalar a : "))
# b = int(input("enter scalar b : "))

# u = np.array(list(map(int , input("Enter vctor u :").split())))
# v = np.array(list(map(int , input("Enter vctor v :").split())))

# linear = a*u + b*v
# average = (u+v) / 2
# print(linear)