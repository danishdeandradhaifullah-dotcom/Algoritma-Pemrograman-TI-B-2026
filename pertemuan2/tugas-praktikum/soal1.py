def rata_rata(nilai):
    hitung = 0
    if len(nilai) == 0: # jika data yang kita input = 0, maka akan mengembalikan data kosong
        return "Data Kosong"
    
    total = sum(nilai) # jika tidak akan menghitung total dari nilai yang diinput
    rata = total/len(nilai) # dan menghitung rata-ratanya dengan membagi total dengan panjang data
    return rata # mengembalikan rata-rata

data = [80, 75, 90, 60, 85]
hasil = rata_rata(data)


print(hasil)