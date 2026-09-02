import numpy as np
import matplotlib.pyplot as plt

z1 = complex(3, 4)     # 3 + 4j
z2 = complex(2, -1)    # 2 - 1j
sum_z = z1 + z2

print("Complex Number z1 =", z1)
print("Complex Number z2 =", z2)
print("Addition (z1 + z2) =", sum_z)

conj_z1 = np.conj(z1)
print("Conjugate of z1 =", conj_z1)

numbers = np.array([
    1 + 1j,
    2 + 1j,
    2 + 2j,
    1 + 2j
])

def plot_complex(nums, title, color='blue'):
    plt.figure(figsize=(6, 6))
    for z in nums:
        plt.arrow(
            0, 0,
            z.real, z.imag,
            head_width=0.08,
            length_includes_head=True,
            color=color
        )
        plt.plot(z.real, z.imag, 'o', color=color)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.title(title)
    plt.axis('equal')
    plt.show()

plot_complex(numbers, "Original Complex Numbers")

# Rotation by 90°
rot90 = numbers * np.exp(1j * np.pi/2)

# Rotation by 180°
rot180 = numbers * np.exp(1j * np.pi)

# Rotation by 270°
rot270 = numbers * np.exp(1j * 3*np.pi/2)
plot_complex(rot90, "Rotation by 90°", "red")
plot_complex(rot180, "Rotation by 180°", "green")
plot_complex(rot270, "Rotation by 270°", "purple")

scale_half = numbers * (1/2)
scale_third = numbers * (1/3)
scale_double = numbers * 2

plot_complex(scale_half, "Scaling by a = 1/2", "orange")
plot_complex(scale_third, "Scaling by a = 1/3", "brown")
plot_complex(scale_double, "Scaling by a = 2", "magenta")

user_input = ''
while user_input != "exit":
    user_input = input('Enter (type no to exit): ').lower()
    if (user_input == "no"):
        break 
    while True:
        try:
            real1, imag1 = map(int, input("Enter 1st complex number (real,imag): ").split(","))
            real2, imag2 = map(int, input("Enter 2nd complex number (real,imag): ").split(","))
            break
        except ValueError:
            print("Invalid input! Please enter in format: real,imag (example: 3,4)")
    z1=complex(real1, imag1)
    z2=complex(real2, imag2)
    while True:
        opr = input('Operations (add=1 , conjugate=2, mul=3, subtract=4, multiply_by_its_conjugate=5) s to stop:')
        if opr=="1":
            print("Z1 + Z2: ", z1+z2)
        elif opr=="2":
            print("Conjugate of z1: ",z1.conjugate())
            print("Conjugate of z2: ",z2.conjugate())
        elif opr=="3":
            print("Multiplication: ",z1*z2)
        elif opr=="4":
            print("Subtraction: ", z1-z2)
        elif opr=="5":
            cz1 = z1.conjugate()
            cz2 = z2.conjugate()
            print("Multiplication of z1 conjugate: ",cz1*z1)
            print("Multiplication of z2 conjugate: ",cz2*z2)
        elif opr=="s":
            break
        else:
            print("wrong input")