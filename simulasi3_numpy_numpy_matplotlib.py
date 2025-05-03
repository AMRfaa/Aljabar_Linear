import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 

# soal 1 numpy
A = np.array([[2, 3],
              [1, -1]])
b = np.array([7, 1])

solusi_1 = np.linalg.solve(A, b)
print(f"Solusi soal 1 dengan NumPy = x: {solusi_1[0]} y: {solusi_1[1]}")

# Visualisasi untuk soal 1 dengan NumPy
def plot_soal_1_numpy():
    # Definisikan range x
    x_vals = np.linspace(-5, 5, 100)

    # Persamaan garis
    y1_vals = (7 - 2 * x_vals) / 3  # Dari persamaan 2x + 3y = 7
    y2_vals = x_vals - 1           # Dari persamaan x - y = 1

    # Plot garis
    plt.plot(x_vals, y1_vals, label="2x + 3y = 7", color="blue")
    plt.plot(x_vals, y2_vals, label="x - y = 1", color="green")

    # Plot solusi
    plt.scatter(solusi_1[0], solusi_1[1], color="red", label=f"Solusi: ({solusi_1[0]:.2f}, {solusi_1[1]:.2f})")

    # Tambahkan label dan legend
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title("Diagram Soal 1 dengan NumPy")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

# Panggil fungsi untuk menampilkan diagram
plot_soal_1_numpy()

# soal 1 sympy
x, y = sp.symbols('x y')

persamaan1 = sp.Eq(2*x + 3*y, 7)
persamaan2 = sp.Eq(x - y, 1)

solusi_2 = sp.solve((persamaan1, persamaan2), (x, y))
print(f"Solusi soal 1 dengan SymPy = {solusi_2}")

# Visualisasi untuk soal 1 dengan SymPy
def plot_soal_1_sympy():
    # Definisikan range x
    x_vals = np.linspace(-5, 5, 100)

    y1_vals = (7 - 2 * x_vals) / 3  # Dari persamaan 2x + 3y = 7
    y2_vals = x_vals - 1           # Dari persamaan x - y = 1

    # Plot garis
    plt.plot(x_vals, y1_vals, label="2x + 3y = 7", color="blue")
    plt.plot(x_vals, y2_vals, label="x - y = 1", color="green")

    # Plot solusi
    if solusi_2:
        plt.scatter(float(solusi_2[x]), float(solusi_2[y]), color="red", label=f"Solusi: ({float(solusi_2[x]):.2f}, {float(solusi_2[y]):.2f})")

    # Tambahkan label dan legend
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title("Diagram Soal 1 dengan SymPy")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

# Panggil fungsi untuk menampilkan diagram
plot_soal_1_sympy()

# soal 2 numpy
Matriks_A = np.array([[1, 2, 1],
                      [3, -1, 2],
                      [-2, 3, -1]])
Matriks_B = np.array([10, 5, -9])

solusi_3 = np.linalg.solve(Matriks_A, Matriks_B)
print(f"Solusi soal 2 dengan NumPy = x: {solusi_3[0]}, y: {solusi_3[1]}, z: {solusi_3[2]}")

# Visualisasi untuk soal 2
def plot_soal_2():
    # Definisikan range untuk x dan y
    x_vals = np.linspace(-10, 10, 100)
    y_vals = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Definisikan persamaan bidang
    Z1 = (10 - X - 2 * Y)  # Dari persamaan 1x + 2y + 1z = 10
    Z2 = (5 - 3 * X + Y) / 2  # Dari persamaan 3x - 1y + 2z = 5
    Z3 = (-9 + 2 * X - 3 * Y)  # Dari persamaan -2x + 3y - 1z = -9

    # Buat plot 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Plot bidang
    ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100, color='blue', label="1x + 2y + 1z = 10")
    ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100, color='green', label="3x - 1y + 2z = 5")
    ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100, color='red', label="-2x + 3y - 1z = -9")

    # Plot solusi
    ax.scatter(solusi_3[0], solusi_3[1], solusi_3[2], color="black", s=50, label=f"Solusi: ({solusi_3[0]:.2f}, {solusi_3[1]:.2f}, {solusi_3[2]:.2f})")

    # Tambahkan label dan legend
    ax.set_title("Visualisasi Soal 2 dalam 3D")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.legend()
    plt.show()

# Panggil fungsi untuk menampilkan diagram
plot_soal_2()

Matriks_C = sp.Matrix([[1, 2, 1],
              [3, -1, 2],
              [-2, 3, -1]])
Matriks_D = sp.Matrix([10, 5, -9])

if Matriks_C.det() == 0:
    print ("Solusi soal 2 dengan SymPy = Matriks tidak memiliki solusi")
else:
    hasil = Matriks_C.solve(Matriks_D)
    print(f"Solusi soal 2 dengan SymPy = x: {hasil[0]}, y: {hasil[1]}, z: {hasil[2]}")

# Visualisasi untuk soal 2 dengan SymPy
def plot_soal_2_sympy():
    # Definisikan range untuk x dan y
    x_vals = np.linspace(-10, 10, 100)
    y_vals = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Definisikan persamaan bidang
    Z1 = (10 - X - 2 * Y)  # Dari persamaan 1x + 2y + 1z = 10
    Z2 = (5 - 3 * X + Y) / 2  # Dari persamaan 3x - 1y + 2z = 5
    Z3 = (-9 + 2 * X - 3 * Y)  # Dari persamaan -2x + 3y - 1z = -9

    # Buat plot 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Plot bidang
    ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100, color='blue', label="1x + 2y + 1z = 10")
    ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100, color='green', label="3x - 1y + 2z = 5")
    ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100, color='red', label="-2x + 3y - 1z = -9")

    # Plot solusi
    if Matriks_C.det() != 0:
        ax.scatter(float(hasil[0]), float(hasil[1]), float(hasil[2]), color="black", s=50, label=f"Solusi: ({float(hasil[0]):.2f}, {float(hasil[1]):.2f}, {float(hasil[2]):.2f})")

    # Tambahkan label dan legend
    ax.set_title("Visualisasi Soal 2 dengan SymPy dalam 3D")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.legend()
    plt.show()

# Panggil fungsi untuk menampilkan diagram
plot_soal_2_sympy()
