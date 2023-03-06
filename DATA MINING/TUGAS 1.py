def penghitung(kalimat):

    c = 0
    for d in kalimat:     
        if d != " ":
            c +=1
    return c

nama = input('Masukan Nama :')
nim = input('Masukan Nim :')

print()
print('Nama :', nama)
print('Jumlah Karakter :', penghitung(nama),'\n')

print('NIM :', nim)
print('Jumlah Karakter NIM :', penghitung(nim))