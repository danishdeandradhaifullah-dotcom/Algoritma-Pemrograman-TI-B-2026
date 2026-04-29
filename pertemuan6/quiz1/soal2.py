films = [["Inside Out", 30000], ["Avengers Endgame", 50000], ["The Wild Robot", 40000], ["Knives Out", 45000], ["Up", 35000]]

pembelian = []

while True:

    print("\nDaftar Film")
    for i in range(len(films)):
        print(f"{i+1}. {films[i][0]} - Rp{films[i][1]}")

    print("0. Selesai")

    choice = int(input("Pilih film: "))

    if choice == 0:
        break

    if choice < 1 or choice >  len(films):
        print("Film tidak valid")
        continue

    tickets = int(input("Jumlah tiket: "))

    pembelian.append([films[choice-1][0], tickets, films[choice-1][1]])

print("\n===Daftar Pembelian===")

total = 0

for items in pembelian:
    judul = items[0]
    jumlah = items[1]
    harga = items[2]

    subtotal = harga * jumlah
    total += subtotal

    print(f"{judul} - {jumlah} tiket = Rp {subtotal}")

print(f"Total pembelian: Rp {total}")
