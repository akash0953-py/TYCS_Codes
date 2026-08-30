# import numpy as np
# while True:
#     r=int(input("Enter the order of Matrix (2,3):"))
#     matrix = []
#     for i in range (r):
#         row = list(map(int, input(f"Enter row {i+1}: ").split()))
#         matrix.append(row)
#     matrix=np.array(matrix)
#     print("Matrix A = \n",matrix) 
#     determinat = np.linalg.det(matrix)
#     print(int(determinat))
#     if determinat == 0:
#         print("Matrix Is Singular \nA Is Not Invertible \nA Inverse Does Not Exists")
#     else:
#         print("Matrix Is Non-Singular \nA Is Invertible \nA Inverse Exists")  
#         inverse = np.linalg.inv(matrix)  
#         print("A Inverse : ",inverse)


import numpy as np

def fuck_off(e):
    print('Invalid Value ',e)

try:
    while True:
        r=int(input("Enter the length of the Rows for Matrix A :"))
        c1=int(input("Enter the length of the Column for Matrix A :"))

        Matrix1 = []
        for i in range (r):
            rows=[]
            for j in range(c1):
                column = int(input(f"Enter value for A{i+1}{j+1} : "))
                rows.append(column)
            Matrix1.append (rows)
        Matrix1=np.array(Matrix1)
        print("Matrix A = \n",Matrix1) 

        determinat = np.linalg.det(Matrix1)
        print(int(determinat))
        if determinat == 0:
            print("Matrix Is Singular \nA Is Not Invertible \nA Inverse Does Not Exists")
        else:
            print("Matrix Is Non-Singular \nA Is Invertible \nA Inverse Exists")  
            inverse = np.linalg.inv(Matrix1)
            print("A Inverse : ",inverse)

except ValueError as e:
    fuck_off(e)