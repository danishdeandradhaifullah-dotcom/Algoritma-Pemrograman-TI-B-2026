def jumlah_digit(n):
    if n == 0:
        return 0
    
    return (n % 10) + jumlah_digit(n // 10) 
'''
n % 10 = mengambil digit terakhir dari sebuah bilangan
misalnya 1234 % 10 = 4
         1567 % 10 = 7
n // 10 = menghapus digit terakhir lalu melakukan rekursi
misalnya 1234 // 10 = 123
         1567 // 10 = 156
jadi hasilnya seperti
return 4 + jumlah_digit(123)
return 4 + 3 + jumlah_digit(123)
dst
'''

angka = 1234
hasil = jumlah_digit(angka)

print(hasil)
