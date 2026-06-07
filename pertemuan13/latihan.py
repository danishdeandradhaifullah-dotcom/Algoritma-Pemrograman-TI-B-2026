import os

while True:
    print("\n[1]. Read File")
    print("[2]. Write file")
    print("[3]. Delete file")
    print("[0]. Exit")

    choose = input("Pilih menu: ")

    if choose == "1":
        directory = "C:\\Users\\VICTUS\\Algoritma-Pemrograman-TI-B-2026\\pertemuan13\\latihan"
        files = os.listdir(directory)
        for i, file in enumerate(files):
            print(f"[{i+1}]. {file}")
            
        choice = input("Pilih file (nomor): ")
        if choice == "1": 
            with open(directory.files(0), "r") as c:
                print(c.read())

 