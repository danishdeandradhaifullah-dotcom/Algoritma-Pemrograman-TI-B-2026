def pangkat_rekursif(a, b):
    if b == 0: # jika b sudah sama dengan nol rekursi akan berhentu
        return 1
    
    return a * pangkat_rekursif(a, b - 1) # akan melakukan pangkat a sebanyak b 

a = 2
b = 5
hasil = pangkat_rekursif(a, b)

print(hasil)
