# membuat matriks menggunakan list
print('-'*70)
matriks_list = ([ 2,  1, -1],
                [-3, -1,  2],
                [-2,  1,  2])

print ("ini adalah matriks dari list:")
for list in matriks_list:
    print(list)

print('-'*70)
print("Elemen baris pertama kolom pertama dari matriks tersebut adalah : ",matriks_list[0][0])
print("Elemen baris kedua   kolom pertama dari matriks tersebut adalah :", matriks_list[1][0])
print("Elemen baris keriga  kolom pertama dari matriks tersebut adalah :", matriks_list[2][0])
print('-'*70)
print("Elemen baris pertama kolom kedua   dari matriks tersebut adalah : ",matriks_list[0][1])
print("Elemen baris kedua   kolom kedua   dari matriks tersebut adalah :", matriks_list[1][1])
print("Elemen baris ketiga  kolom kedua   dari matriks tersebut adalah : ",matriks_list[2][1])
print('-'*70)
print("Elemen baris kedua   kolom ketiga  dari matriks tersebut adalah : ",matriks_list[1][2])
print("Elemen baris ketiga  kolom ketiga  dari matriks tersebut adalah : ",matriks_list[2][2])
print("Elemen baris pertama kolom ketiga  dari matriks tersebut adalah :", matriks_list[0][2])
print('-'*70)

import numpy as np
# Membuat matriks menggunakan Array
matriks_array = ([[2, 1, -1], 
                  [-3,-1, 2],
                  [-2, 1, 2]])
print("ini adalah matriks array")
for array in matriks_array:
    print(array)

print('-'*70)
print("Elemen baris pertama kolom pertama dari matriks tersebut adalah : ",matriks_array[0][0])
print("Elemen baris kedua   kolom pertama dari matriks tersebut adalah :", matriks_array[1][0])
print("Elemen baris keriga  kolom pertama dari matriks tersebut adalah :", matriks_array[2][0])
print('-'*70)
print("Elemen baris pertama kolom kedua   dari matriks tersebut adalah : ",matriks_array[0][1])
print("Elemen baris kedua   kolom kedua   dari matriks tersebut adalah :", matriks_array[1][1])
print("Elemen baris ketiga  kolom kedua   dari matriks tersebut adalah : ",matriks_array[2][1])
print('-'*70)
print("Elemen baris kedua   kolom ketiga  dari matriks tersebut adalah : ",matriks_array[1][2])
print("Elemen baris ketiga  kolom ketiga  dari matriks tersebut adalah : ",matriks_array[2][2])
print("Elemen baris pertama kolom ketiga  dari matriks tersebut adalah :", matriks_array[0][2])
print('-'*70)
