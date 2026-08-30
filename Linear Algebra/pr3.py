import numpy as np
def input_matrix(rows, cols):
    while True:
        try:
            matrix = []
            for i in range(rows):
                row = list(map(int, input(f"Enter row {i+1}: ").split()))
                if len(row) != cols:
                    raise ValueError(f"Please enter exactly {cols} values.")
                matrix.append(row)
            return np.array(matrix)
        except Exception as e:
            print("\nError:", e)
            print("Please enter the matrix again.\n")
def practical_3():
    while True:
        try:
            rows = int(input("Enter the length of rows: "))
            if rows <= 0:
                raise ValueError(f"Invalid Input")
            cols = int(input("Enter the length of column: "))
            if cols <= 0:
                raise ValueError(f"Invalid Input")
            matrix = input_matrix(rows,cols)
        except Exception as e:
            print("\nError:", e)
            print("Please enter the lengths again.\n")
            continue
        while True:
            print("\n========= MAIN MENU =========")
            print("1 → Print Matrix")
            print("2 → Print rows of Matrix")
            print("3 → Print columns of Matrix")
            print("4 → Print Transpose of Matrix")
            print("5 → Scalar Multiplication on matrix")
            print("6 → Enter Matrix Again")
            print("7 → Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("Matrix : ")
                print(matrix)
            elif choice == "2":
                print("Rows:")
                for i in range(rows):
                    print(f"Rows {i+1} : {matrix[i]}")
            elif choice == "3":
                print("Columns:")
                for i in range(cols):
                    print(f"Column {i+1}: {matrix[:, i]}")
            elif choice == "4":
                print("Transpose:")
                print(matrix.T)
            elif choice =="5":
                scalar = int(input("Enter scalar value: "))
                print("MATRIX : ")
                print(matrix*scalar)
            elif choice == "6":
                break
            elif choice == "7":
                print("Exiting program... Goodbye!")
                return
            else:
                print("Invalid choice")         
practical_3()