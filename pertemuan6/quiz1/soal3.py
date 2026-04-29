totalPembelian = int(input("Total pembelian: "))
uangDibayar = int(input("Uang dibayar: "))

while uangDibayar < totalPembelian:
    print("Uang bayar tidak cukup")
    uangDibayar = int(input("Total membayar: "))

kembalian = uangDibayar - totalPembelian

print("==RINGKASAN==")
print(f"Total pembelian : {totalPembelian}")
print(f"Uang dibayar : {uangDibayar}")
if kembalian == 0:
    print("Uang pas, tidak ada kembalian")
else:
    print(f"Kembalian anda : Rp{kembalian}")