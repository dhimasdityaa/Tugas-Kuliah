# Studi Case Ini Menggunakan Nilai Awal 0 dan Nilai kedua 1
a = 0
b = 1
c = 0

l = int(input('Masukan banyak suku yang akan di hitung :'))

# valu 10 pada range banyaknya printah akan di looping
for i in range(l):
    print(a)
    c = a + b
    a = b
    b = c
