# soal 1 (2 var)
# Numpy 
import numpy as np

# Matriks koefisien
A = np.array([[2, 3],
              [1, -1]])

# Matriks hasil
b = np.array([7, 1])

# Menyelesaikan sistem persamaan
solusi_1 = np.linalg.solve(A, b)
print(f"Solusi soal 1 dengan NumPy = x: {solusi_1[0]} y: {solusi_1[1]}")

# sympy
import sympy as sp

# Mendefinisikan variabel simbolik
x, y = sp.symbols('x y')

# Membuat sistem persamaan
persamaan1 = sp.Eq(2*x + 3*y, 7)
persamaan2 = sp.Eq(x - y, 1)

# Menyelesaikan secara simbolik
solusi_2 = sp.solve((persamaan1, persamaan2), (x, y))
print(f"Solusi soal 1 dengan SymPy = {solusi_2}")

# soal 2 (3 var)
import numpy as np

Matriks_A = np.array([[1, 2, 1],
                      [3, -1, 2],
                      [-2, 3, -1]])
Matriks_B = np.array([10, 5, -9])

solusi_3 = np.linalg.solve(Matriks_A, Matriks_B)
print(f"Solusi soal 2 dengan NumPy = x: {solusi_3[0]}, y: {solusi_3[1]}, z: {solusi_3[2]}")

# sympy 3 var
import sympy as sp

Matriks_A = sp.Matrix([[1, 2, 1],
              [3, -1, 2],
              [-2, 3, -1]])
Matriks_B = sp.Matrix([10, 5, -9])

if Matriks_A.det() == 0:
    print ("Solusi soal 2 dengan SymPy = Matriks tidak memiliki solusi")
else:
    hasil = Matriks_A.solve(Matriks_B)
    print(f"Solusi soal 2 dengan SymPy = x: {hasil[0]}, y: {hasil[1]}, z: {hasil[2]}")
