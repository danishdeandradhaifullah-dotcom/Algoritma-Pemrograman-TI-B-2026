import random
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
riwayat = []

def tebak_angka(angka_rahasia, maks_percobaan):
    guesses = maks_percobaan
    while guesses != 0: # program berjalan jika jumlah percobaan belum 0
        guess = int(input("Tebak: "))
        if guess == angka_rahasia:
            print("Benar!")
            guessed = True
            return guessed, guesses
        elif guess < angka_rahasia:
            print('Terlalu Kecil')
            guesses -= 1
        elif guess > angka_rahasia:
            print("Terlalu besar")
            guesses -= 1
    guessed = False
    return guessed,guesses

def hitung_skor(berhasil, sisa_percobaan):
    if berhasil == True:
        return sisa_percobaan * 10 # jika tertebak dapat skor sisa percobaan dikali 10
    else:
        return 0
    
def main_satu_ronde(nama, nomor_ronde):
    print(f'Round {nomor_ronde}')

    angka_rahasia = random.randint(1,100)
    
    hasil, coba = tebak_angka(angka_rahasia, 7)
    skor = hitung_skor(hasil, coba )
        
    return [nama, skor]
    
def tampilkan_riwayat(riwayat):
    print('\n===== RIWAYAT =====')
    if not riwayat: # jika isi riwayat kosong print belum ada riwayat
        print('Belum ada riwayat')
    else:
        for i, (nama,nilai) in enumerate(riwayat, start=1):
            print(f"{i}. {nama} - {nilai}")

def selection_sort_riwayat(riwayat):
    copy_riwayat = riwayat.copy() # ini kita membuat copy riwayat bukan pakai riwayat yang asli
    n = len(copy_riwayat)
    for i in range(n-1):
        max_idx = i
        for j in range(i+1,n):
            if copy_riwayat[j][1] > copy_riwayat[max_idx][1]:
                max_idx = j
        copy_riwayat[i], copy_riwayat[max_idx] = copy_riwayat[max_idx], copy_riwayat[i]
    return copy_riwayat

def tampilkan_leaderboard(riwayat):
    print('\n===== LEADERBOARD =====')
    leaderboard = selection_sort_riwayat(riwayat) # panggil selection sort diatas
    count = 1
    for nama,nilai in leaderboard:
        if count == 1:
            print(f'{count}*. {nama} - {nilai}')
        else:
            print(f'{count}. {nama} - {nilai}')
        count += 1

people = int(input('How many people want to play: '))
for i in range(people):
    print(f'\n=== Player {i+1} ===')
    nama = input('Enter name: ')

    score = main_satu_ronde(nama, i+1)
    riwayat.append(score)

tampilkan_leaderboard(riwayat)
tampilkan_riwayat(riwayat)







