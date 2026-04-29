hari = int(input("Masukkan jumlah hari: "))
film = int(input("Masukkan jumlah film: "))

data = []

for i in range(hari):
    baris = []
    print(f"\nHari ke {i+1}")

    for j in range(film):
        tiket = int(input(f"Jumlah tiket film {j+1}: "))
        baris.append(tiket)

    data.append(baris)

print('\n===Matriks Penjualan===')

for i in range(hari):
    total_hari = sum(data[i])
    print(f"Hari {i+1}: {total_hari}")

print("\nTotal tiket per film:")

for j in range(film):
    total_film = 0
    for i in range(hari):
        total_film += data[i][j]

    print(f"Film {j+1}: {total_film}")