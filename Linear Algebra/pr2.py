def dot_product(u,v):
        dot = 0
        for i in range(len(u)):
            dot += u[i] * v[i]
        print("Dot Product =", dot)
def vector_product(u,v):
        result = []
        a = float(input("Enter value of a: "))
        b = float(input("Enter value of b: "))
        for i in range(len(u)):
            result.append(a * u[i] + b * v[i])
        print("au + bv =", result)
def practical_2():
    u = list(map(float, input("Enter vector u: ").split()))
    v = list(map(float, input("Enter vector v: ").split()))
    while True:
        print("1 → Scalar Product")
        print("2 → Dot Product")
        print("3 → Exit")
        if len(u) != len(v):
            print("Vectors must be of same size!")
        else:
            choice = input("Enter your choice: ")
            if choice == "2":
                dot_product(u,v)
            elif choice == "1":
                vector_product(u,v)
            elif choice == "3":
                print("Exiting program... Goodbye!")
                break  
            else:
                print("Invalid choice")
practical_2()