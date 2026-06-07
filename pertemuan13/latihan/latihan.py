import os

while True:
    print("\n[1]. Read File")
    print("[2]. Write file")
    print("[3]. Delete file")
    print("[0]. Exit")

    choose = input("Pilih menu: ")

    if choose == "1":
        count = 1
        files = os.listdir()
        for file in os.listdir('.'):
            if file.endswith('.py'):
                continue
            else:
                print(f"[{count}]. {file}")
                count += 1
        try:
            choice = int(input("Pilih file (nomor): "))
            with open(files[choice - 1],"r") as c:
                print(c.read())
        except:
            print("Nomor tidak valid atau bukan nomor")
        
    
    if choose == "2":
        count = 1
        files = os.listdir()
        for file in os.listdir('.'):
            if file.endswith('.py'):
                continue
            else:
                print(f"[{count}]. {file}")
                count += 1

        while True:
            print("\n1. Old")
            print("2. Make new")

            choice = int(input("Pilih: "))
            if choice == 1:
                choose = int(input("File mana: "))
                with open(files[choose - 1],"w") as c:
                    c.write(input())
            elif choice == 2:
                newfile = input("New file name: ")
                with open(newfile, "w") as c:
                    c.write(input())

    if choose == "3":
        count = 1
        files = os.listdir()
        for file in os.listdir('.'):
            if file.endswith('.py'):
                continue
            else:
                print(f"[{count}]. {file}")
                count += 1       

        choice = int(input("Pilih file (nomor): "))
        if os.path.exists(files[choice -1]):
            os.remove(files[choice - 1])

    if choose == "0":
        break