gajiPokok = int(input('Masukan Gaji Pokok :'))
hariLembur = int(input('Masukan Total Hari Lembur : '))

lembur = 150000
tunjangan = gajiPokok * (20/100)
uangLembur = hariLembur * lembur
pajak = gajiPokok * (5/100)
kredit = 300000

totalGaji = gajiPokok + tunjangan + uangLembur - pajak - kredit

print('+------------------------------------------+')
print('|-------------- RINCIAN GAJI --------------|')
print('+------------------------------------------+')
print('| Gaji Pokok : Rp.', gajiPokok, '                |')
print('| Uang Lembur Bulanan : Rp.', uangLembur, '       |')
print('| Tunjangan Bulanan : Rp.', tunjangan, '        |')
print('| Pajak Pendapat : Rp.', pajak, '           |')
print('| Total Kredit di bayarkan : Rp.', kredit, '   |')
print('| Total Gaji : Rp.', totalGaji, '              |')
print('+------------------------------------------+')
