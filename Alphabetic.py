#Initial Variable#
abjad = 'abcdefghijklmnopqrstuvwxyz'
ans1 = ''
ans = ''

#Variasi Kunci Ganda 1#
kun1 =  'merdkabcfghijlnopqstuvwxyz'
kun2 =  'indoesabcfghjklmpqrtuvwxyz'

#Variasi Kunic Ganda2#
key1 =  'dhimasbcefgjklnopqrtuvwxyz'
key2 =  'aditybcefghjklmnopqrsuvwxz'

#Plain Text
plain = 'belajarkriptografi'

#Proses Pencocokan Huruf
def encrypt(a):
    x = a
    for i in range(len(abjad)):
        xAbjad = abjad[i]
        if xAbjad == x:
            return i

#Proses Enkripsi dengan Kunci Pertama
for i in range(len(plain)):
    xPlain = plain[i]
    pros = encrypt(xPlain)
    ans1 += kun1[pros]

#Proses Enkripsi dengan Kunci Kedua
for z in range(len(ans1)):
    xAns1 = ans1[z]
    proz = encrypt(xAns1)
    ans += kun2[proz]

#Menampilkan Hasil dari Enkripsi
print(ans.upper())

