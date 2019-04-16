import random
kelimeler =(["bursa", "çorum", "diyarbakır", "erzurum", "hatay", "istanbul", "kayseri",
             "yozgat", "çanakkale","konya", "eskişehir", "bolu", "van"])

hak = 5
i=0

secilenKelime=random.choice(kelimeler)
girilenharfler =[]
karakterGosterimi="_"

for kelime in secilenKelime:
    girilenharfler.append(karakterGosterimi)
print(girilenharfler)

while hak>0:
    alinanharf = input("Lütfen bir harf giriniz=").lower()
    if alinanharf in secilenKelime:
        for kontrol in secilenKelime:
            if alinanharf==secilenKelime[i]:
                girilenharfler[i] = alinanharf
            i +=1
        print(girilenharfler)
        i=0

    kontrolEt= alinanharf in secilenKelime
    if kontrolEt == False:
        hak-=1
    print("Kalan can sayınız=", hak)
    i=0

    if hak == 0:
     print("Oyunu kaybettiniz.Doğru kelime '{}' idi.".format(secilenKelime))

     break

    if karakterGosterimi not in girilenharfler:
        print("Tebrikler.Doğru kelimeyi buldunuz")
        break
