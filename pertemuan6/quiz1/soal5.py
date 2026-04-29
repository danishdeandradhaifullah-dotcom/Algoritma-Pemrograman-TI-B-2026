class Film:
    def __init__(self, judul, harga):
        self.judul = judul
        self.harga = harga

    def tampilkan(self):
        print(f"{self.judul} - Rp{self.harga}")

class Transaksi:
    def __init__(self):
        self.total = 0  

    def tambah(self, film, jumlah):
        self.total += film.harga * jumlah

    def struk(self):
        print(f"Total pembelian: Rp {self.total}")

film1 = Film("Hoppers", 30000)
film2 = Film("Marty Supreme", 60000)
film3 = Film("Sinners", 50000)

daftar_film = [film1, film2, film3]

print("===Daftar Film===")

for i in range(len(daftar_film)):
    print(f"{i+1}.", end="")
    daftar_film[i].tampilkan()

transaksi = Transaksi()

Judul = int(input("Judul film: "))
Jumlah = int(input("Jumlah tiket: "))

film_diplih = daftar_film[Judul-1]

transaksi.tambah(film_diplih, Jumlah)

print("\nStruk Pembelian")
transaksi.struk()