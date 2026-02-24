usernameBenar = "Danish"
passwordBenar = 676869
percobaan = 4

while percobaan > 0:
    try:
        username = input( "Masukkan username: " )
        password = int(input( "Masukkan password (Integer): " ))

        if username == "" :
            raise ValueError( "Username tidak boleh kosong" )

        if username == usernameBenar and password == passwordBenar:
            print( "Login berhasil!" )
            break
        else:
            percobaan -= 1
            print( "Login gagal. Percobaan yang sisa:", percobaan )

    except ValueError :
       print( "Error: Password harus berupa angka dan tidak boleh kosong" )

if percobaan == 0:
    print( "Akun diblokir." )