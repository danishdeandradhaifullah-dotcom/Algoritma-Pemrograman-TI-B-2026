def transpose(matriks):
    baris = len(matriks)
    kolom = len(matriks[0])

    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]
    for i in range(baris):
     for j in range(kolom):
      hasil[j][i] = matriks[i][j]
    return hasil

A = [[1, 2, 3],
[4, 5, 6]] # Ukuran 2x3
print('Matriks A (2x3):')
for baris in A:
    print(baris)
T = transpose(A)
print('Transpose A (3x2):')
for baris in T:
    print(baris)