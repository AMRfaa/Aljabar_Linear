import numpy as np

# Matriks P dan Q
Matriks_P = np.array([[11, 12, 13],
                      [14, 15, 16],
                      [17, 18, 19]])

Matriks_Q = np.array([[20, 21, 22],
                      [23, 24, 25],
                      [26, 27, 28]])

# Cetak Matriks
print('Matriks P:')
print(Matriks_P)
print('\nMatriks Q:')
print(Matriks_Q)

# Operasi penjumlahan dan pengurangan
penjumlahan = Matriks_P + Matriks_Q
pengurangan = Matriks_P - Matriks_Q
print('\nHasil penjumlahan Matriks P dan Q adalah:')
print(penjumlahan)
print('\nHasil pengurangan Matriks P dan Q adalah:')
print(pengurangan)

# Perkalian dot
perkalian_dot = np.dot(Matriks_P, Matriks_Q)
print('\nHasil perkalian dot Matriks P dan Q adalah:')
print(perkalian_dot)

# Transpose
transpose_P = Matriks_P.T
transpose_Q = Matriks_Q.T
print('\nTranspose Matriks P:')
print(transpose_P)
print('\nTranspose Matriks Q:')
print(transpose_Q)
