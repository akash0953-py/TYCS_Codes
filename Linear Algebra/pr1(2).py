import matplotlib.pyplot as plt

# ---------------- SIMPLE PLOT ----------------
def simple_plot(z):
    plt.figure()
    plt.scatter(z.real, z.imag)
    plt.title("Simple Complex Plot")
    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.show()


# ---------------- UPGRADED PLOT ----------------
def upgraded_plot(z):
    x, y = z.real, z.imag

    plt.figure(figsize=(6,6))
    plt.scatter(x, y, color='red', s=50)

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.title("Argand Plane Representation")

    plt.text(x + 0.1, y + 0.1, str(z))

    plt.grid()
    plt.show()


# ---------------- ROTATION SYSTEM ----------------
def rotate_by_angle(z):
    plt.ion()
    plt.figure(figsize=(6,6))

    plt.plot([0, z.real], [0, z.imag], marker='o', label="Original")

    while True:
        print("\n--- ROTATION MENU ---")
        print("1 → 90° Rotation")
        print("2 → 180° Rotation")
        print("3 → 270° Rotation")
        print("4 → 360° Rotation")
        print("5 → Exit Rotation Mode")

        choice = input("Enter choice: ")

        if choice == "1":
            w = z * 1j
            label = "90°"
        elif choice == "2":
            w = z * (-1)
            label = "180°"
        elif choice == "3":
            w = z * (-1j)
            label = "270°"
        elif choice == "4":
            w = z
            label = "360°"
        elif choice == "5":
            break
        else:
            print("Invalid choice")
            continue

        plt.plot([0, w.real], [0, w.imag], marker='o', label=label)
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.grid()
        plt.legend()

        plt.draw()
        plt.pause(0.5)

    plt.ioff()
    plt.show()


# ---------------- CHANGE COMPLEX NUMBER ----------------
def change_complex():
    real = float(input("Enter NEW real part: "))
    imag = float(input("Enter NEW imaginary part: "))
    z = complex(real, imag)
    print("Updated complex number is:", z)
    return z

# ---------------- HALF SCALLING ----------------
def half_scaling(z):
    w = z * 0.5

    print("Half Scaled Complex Number:", w)

    plt.figure()
    plt.plot([0, z.real], [0, z.imag], marker='o', label="Original")
    plt.plot([0, w.real], [0, w.imag], marker='o', label="Half Scaled")

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid()
    plt.legend()
    plt.title("Half Scaling of Complex Number")
    plt.show()

# ---------------- DOUBLE SCALING ----------------
def double_scaling(z):
    w = z * 2

    print("Double Scaled Complex Number:", w)

    plt.figure()
    plt.plot([0, z.real], [0, z.imag], marker='o', label="Original")
    plt.plot([0, w.real], [0, w.imag], marker='o', label="Double Scaled")

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid()
    plt.legend()
    plt.title("Double Scaling of Complex Number")
    plt.show()

# ---------------- ONE - THIRD SCALLING ----------------
def one_third(z):
    w = z * (1/3)
    print("One third scaled complex numbers: ", w)

    plt.figure()
    plt.plot([0, z.real] ,[0 , z.imag], marker='o' , label="Original")
    plt.plot([0, w.real] ,[0 , w.imag], marker='o' , label="One-Third Scaled")

    plt.axhline(0 , color='black')
    plt.axvline(0 , color="black")
    plt.grid()
    plt.legend()
    plt.title("One-Third Scalling of Complex Number")
    plt.show()

# ---------------- MAIN SYSTEM ----------------
def practical_1_QUESTION_2():
    print("\n==============================")
    print("  COMPLEX NUMBER SYSTEM v2   ")
    print("==============================")

    real = float(input("Enter real part: "))
    imag = float(input("Enter imaginary part: "))
    z = complex(real, imag)

    print("\nInitial Complex Number:", z)

    while True:
        print("\n========= MAIN MENU =========")
        print("1 → Simple Plot (Basic View)")
        print("2 → Upgraded Argand Plot")
        print("3 → Rotation System")
        print("4 → Change Complex Number 🔄")
        print("5 → Half Scaling (0.5z)")
        print("6 → Double Scaling (2z)")
        print("7 → One-Third Scaling (z/3)")
        print("8 → Exit Program")

        choice = input("Enter your choice: ")

        if choice == "1":
            simple_plot(z)

        elif choice == "2":
            upgraded_plot(z)

        elif choice == "3":
            rotate_by_angle(z)

        elif choice == "4":
            z = change_complex()   # 🔥 IMPORTANT: updates global z
        
        elif choice == "5":
            half_scaling(z)
        
        elif choice == "6":
            double_scaling(z)
        
        elif choice == "7":
            one_third(z)

        elif choice == "8":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice")


# ---------------- RUN ----------------
practical_1_QUESTION_2()