struktur = {
"Skripsi_Aqil": {
"Bab_1": {
"pendahuluan.docx": 45,
"latar_belakang.docx": 62
},
"Bab_2": {
"landasan_teori.docx": 118,
"referensi": {
"paper_A.pdf": 340,
"paper_B.pdf": 210
}
},
"Bab_3": {
"metodologi.docx": 89,
"diagram": {
"flowchart.png": 512,

"erd.png": 278,
"arsitektur": {
"sistem.png": 430
}
}
},
"sidang": {
"presentasi.pptx": 2048,
"catatan_revisi.txt": 15
},
"README.txt": 8
}
}

def total_ukuran(folder: dict) -> int:
    total = 0
    for item in folder.values():
        if type(item) == dict:
            total += total_ukuran(item)
        else:
            total += item

    return total

def hitung_file(folder:dict) -> int:
    hitung = 0
    for item in folder.values():
        if type(item) == dict:
            hitung += hitung_file(item)
        else:
            hitung += 1
    
    return hitung

def cari_terbesar(folder: dict) -> tuple:
    max = 0
    nama_file = ""

    for nama, item in folder.items():
        if type(item) == dict:
            hasil = cari_terbesar(item)

            if hasil[1] > max:
                nama_file = hasil[0]
                max = hasil[1]

        else:
            if item > max:
                nama_file = nama
                max = item
    return(nama_file,max)

def tampilkan_tree(folder:dict, nama: str = "root" , level: int = 0):
    for nama_file, item in folder.items():
        spasi = "  " * level

        if type(item) == dict:
            print(f"{spasi} 📂 {nama_file}")
            tampilkan_tree(item, nama_file, level+1)
        else:
            print(f"{spasi} 🗒️ {nama_file} ({str(item)} KB)")

print(f'Total ukuran skripsi: {total_ukuran(struktur)}')
print(f"Jumlah file: {hitung_file(struktur)}")
print(f'File terbesar: {cari_terbesar(struktur)}')
tampilkan_tree(struktur)