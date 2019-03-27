sorular= ['Çakmak kibritten üretilmiştir. [D/Y]', 'Ahtapotların 3 tane kalbi vardır. [D/Y]', 'Altın en iyi iletkendir. [D/Y]',
          'Dünyadaki en kısa savaş 2 saat sürmüştür. [D/Y]', 'Chicago, Barcelona, Roma ve İstanbul, aynı enlem üzerindedir. [D/Y]']
cevaplar= ['D','D','Y','Y', 'D']
puan = 0
cevap = input((sorular[0]))
if cevaplar[0] == cevap.upper():
    print("Doğru!")
    puan += 1
else:
    print("Yanlış!")
cevap = input((sorular[1]))
if cevaplar[1] == cevap.upper():
    print("Doğru!")
    puan += 1
else:
    print("Yanlış!")
cevap = input((sorular[2]))
if cevaplar[2] == cevap.upper():
    print("Doğru!")
    puan += 1
else:
    print("Yanlış! En iyi iletken gümüştür.")
cevap = input((sorular[3]))
if cevaplar[3] == cevap.upper():
    print("Doğru!")
    puan += 1
else:
    print("Yanlış! Tarihin en kısa savaşı 1896 yılında İngiltere ile Zanzibar arasında yapılmıştır. Savaş başladıktan 40 dakika sonra Zanzibar teslim olmuştur. ")
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper():
    print("Doğru!")
    puan += 1
else:
    print("Yanlış!")

print("Testi tamamladınız. Puanınız: "+str(puan*20))
