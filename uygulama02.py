__author__="Eslem Aydemir"
#date:08.04.19


sorular=['Pop Art sanat akımı nerede doğmuştur?',
         'Aşağıdakilerden hangisi Rönesans döneminin ''Mahşerin 4 Atlısı'' olarak geçen sanatçılardan biri değildir?',
         'Hangisi ''dünyanın yedi harikası''ndan birisi değildir?',
         ' \'Kaplumbağa Terbiyecisi\' isimli belki de Türk Sanat Tarihi\'nin en meşhur resmi kime aittir?',
         'Aşağıdakilerden hangisi sürrealist bir ressamdır?']

cevapA=['Amerika', 'Raffaello', 'Efes Antik Kenti', 'Osman Hamdi', 'Pablo Picasso']
cevapB=['Hollanda', 'Donatello', 'Babil’in Asma Bahçeleri', 'Levni', 'Salvador Dali']
cevapC=['İngiltere', 'Michelangelo','Rodos Heykeli', 'Kapıdağlı Konstantin', 'Pierre Auguste Renoir']
cevapD=['Belçika', 'Caravaggio', 'Haliskarnas Mozolesi', 'Matrakçı Nasuh', 'Edgar Degas']
cevaplar=['C', 'D', 'A', 'A', 'B']
puan = 0

for i in range(len(sorular)):
    print("Soru " + str(i + 1) + ":" + sorular[i])
    print("A.) " + cevapA[i])
    print("B.) " + cevapB[i])
    print("C.) " + cevapC[i])
    print("D.) " + cevapD[i])
    cevap = input("Cevabınızı giriniz: ")
    if cevaplar[i] == cevap.upper():
        puan += 1
print("Tebrikler! Testi Tamamladınız.")
print("Aldığınız not: " + str(int((puan / len(sorular)) * 100)))
input()
