films = [["Inside Out", 30000], ["Avengers Endgame", 50000], ["The Wild Robot", 40000], ["Knives Out", 45000], ["Up", 35000]]

for x in range(len(films)):
    print(f"{x+1}. {films[x][0]} - Rp {films[x][1]}")

choice = int(input("Masukkan nomor film yang ingin dipilih: ")) 

if choice >= 1 and choice <= len(films):
    judul = films[choice - 1][0]
    harga = films[choice - 1][1]
    print(f"Film dipilih: {judul}")
    print(f"Harga tiket: {harga}")
else:
    print("Nomor tidak valid")
    