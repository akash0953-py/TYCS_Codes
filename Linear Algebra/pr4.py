import numpy as np
def vector_matrix_multiplication(v, cols):
    while True:
        try:
            matrix = []
            print(f"\nEnter the matrix ({len(v)} x {cols}):")
            for i in range(len(v)):
                row = list(map(int, input(f"Enter row {i + 1}: ").split()))
                if len(row) != cols:
                    raise ValueError(f"Please enter exactly {cols} values.")
                matrix.append(row)
            return np.array(matrix)
        except Exception as e:
            print("\nError:", e)
            print("Please enter the matrix again.\n")
def practical_5():
    while True:
        try:
            v = list(map(int, input("Enter vector: ").split()))
            if len(v) == 0:
                raise ValueError("Vector cannot be empty.")
            cols = int(input("Enter the number of columns of the matrix: "))
            if cols <= 0:
                raise ValueError("Columns must be greater than 0.")
            matrix = vector_matrix_multiplication(v, cols)
        except Exception as e:
            print("\nError:", e)
            print("Please enter the data again.\n")
            continue
        while True:
            print("\n========= MAIN MENU =========")
            print("1 → Vector × Matrix Multiplication")
            print("2 → Matrix matrix multiplication")
            print("3 → Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                result = np.dot(v, matrix)
                print("\nVector:")
                print(np.array(v))
                print("\nMatrix:")
                print(matrix)
                print("\nResult (Vector × Matrix):")
                print(result)
            elif choice == "2":
                try:
                    cols2 = int(input("Enter the number of columns for the second matrix: "))
                    matrix2 = []
                    print(f"\nEnter the second matrix ({cols} x {cols2}):")
                    for i in range(cols):
                        row = list(map(int, input(f"Enter row {i+1}: ").split()))
                        if len(row) != cols2:
                            raise ValueError(f"Please enter exactly {cols2} values.")
                        matrix2.append(row)
                    matrix2 = np.array(matrix2)
                    result = np.dot(matrix, matrix2)
                    print("\nFirst Matrix:")
                    print(matrix)
                    print("\nSecond Matrix:")
                    print(matrix2)
                    print("\nResult (Matrix × Matrix):")
                    print(result)
                except Exception as e:
                    print("\nError:", e)
            elif choice == "3":
                print("Exiting program... Goodbye!")
                return
            else:
                print("Invalid choice.")
practical_5()