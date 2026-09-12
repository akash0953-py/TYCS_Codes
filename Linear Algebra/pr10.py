import numpy as np
try:
    l = int(input("Enter length: "))
    v = np.array([int(input(f"Enter v[{i+1}]: ")) for i in range(l)])
    u = np.array([int(input(f"Enter u[{i+1}]: ")) for i in range(l)])
    a = int(input("Enter scalar a: "))
    b = int(input("Enter scalar b: "))
    linear_combination = a*u + b*v
    average = (u + v) / 2
    print("Linear Combination:", linear_combination)
except Exception as e:
    print(e)