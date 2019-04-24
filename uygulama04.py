metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[:19])
#soru 1

liste = (["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"])

for i in liste:
    print(i)
#soru 2

sozluk = {"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }
a= input("Bir meyve giriniz")
a= a.capitalize()

if a in sozluk:
    print(sozluk[a])
else:
    print("Başka bir meyve deneyiniz.")
#soru 3
