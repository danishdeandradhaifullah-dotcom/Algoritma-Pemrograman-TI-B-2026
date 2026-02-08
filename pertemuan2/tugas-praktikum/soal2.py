def bilangan_prima(n):
    bilPrima = []

    for num in range(2, n+1): # range dari 2 karena 1 bukan bilangan prima
        is_bilPrima = True # membuat sama number dari range 2 sampai n+1 bilangan prima

        for x in range(2, num):
            if num % x == 0: # sekarang mengecek jika x bisa membagi number secara penuh
                is_bilPrima = False # jika iya number, itu bukan prima
                break

        if is_bilPrima:
            bilPrima.append(num) # semua bilangan prima yang tersisa akan di append dalam list bilPrima
        
    return bilPrima # akan mengembalikan bilangan prima

hasil = bilangan_prima(50)

print(hasil)    
