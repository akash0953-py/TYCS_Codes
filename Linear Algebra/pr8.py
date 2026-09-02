import numpy as np
def projection(a, b):
    result = (np.dot(a, b) / np.dot(b, b)) * b
    print("Projection =", result)
a = np.array(list(map(int, input("Enter vector A: ").split())))
b = np.array(list(map(int, input("Enter vector B: ").split())))
print("Vector A:", a)
print("Vector B:", b)
while True:
    choice = int(input("\n1. Projection of A on B" "\n2. Projection of B on A" "\n3. Exit""\nEnter: "))
    if choice == 1:
        projection(a, b)
    elif choice == 2:
        projection(b, a)
    elif choice == 3:
        break
    else:
        print("Invalid choice")