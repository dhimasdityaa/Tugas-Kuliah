#Initial Variable#
abjad = 'abcdefghijklmnopqrstuvwxyz'

#Variasi Kunci Ganda 1#
kun1 =  'merdkabcfghijlnopqstuvwxyz'
kun2 =  'indoesabcfghjklmpqrtuvwxyz'

#Variasi Kunic Ganda2#
key1 =  'dhimasbcefgjklnopqrtuvwxyz'
key2 =  'aditybcefghjklmnopqrsuvwxz'

#Plain Text
plain = 'belajarkriptografi'

def encrypt(a):
    x = a
    for i in range(len(abjad)):
        xAbjad = abjad[i]
        if xAbjad == x:
            return i
        
def process(text,key):
    sentence = ''
    for i in range(len(text)):
        xText = text[i]
        pros = encrypt(xText)
        sentence += key[pros]
        return sentence


for i in range(len(plain)):
    step1 = process(plain[i],kun1)
    for z in range(len(step1)):
        step2 = process(step1[z],kun2)
    print(step2.upper(),end='')
