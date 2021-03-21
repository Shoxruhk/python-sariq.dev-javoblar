# bugungi dasturda biz soz topish dasturini yaratamiz kompyuter oylagan sozni topamiz
# buning uchun bizga sozlar royhati kerak boladi buni dasturimizga yuklab olamiz
# kompyuter son tanlashi uchun ham random funksiyasini chaqirib olamiz
from uzwords import words
from random import choice
# kompyuter oylagan sozni topishga urinuvchi funksiya yaratamiz
def soz_top(tasodifiy_soz = choice(words)):
    """bu funksiya kompyuter oylagan sonni topish funksiyasi"""
    print("Keling bir o'yin o'ynaymiz. Men so'z o'yladim, siz toping")
    soz_uzunligi = len(tasodifiy_soz)
    tasodifiy_soz.lower()
    print(f"\nMen {soz_uzunligi} ta harfli so'z o'yladim. Topishga haraqat qiling")
    print("_" * soz_uzunligi)
    topilgan_harflar = []
    kiritilgan_harflar = []
    urunishlar_soni = 0

    for i in range(soz_uzunligi): topilgan_harflar.append("_")
    while True:
        harf = input("\nКирил алифбосида харф киритинг: ".lower())
        if harf in tasodifiy_soz:
            print(f"Qoyil {harf.upper()} harfi to'g'ri ")
        else:
            print("Kechirasiz so'zimizda bunday harf mavjut emas!!!")
        if harf not in kiritilgan_harflar:
            kiritilgan_harflar.append(harf)
            for k_harf in kiritilgan_harflar:
                aniqlik = 0

                for t_harf in tasodifiy_soz:
                    if t_harf == k_harf:
                        topilgan_harflar[aniqlik]=t_harf
                    aniqlik+=1
            print(f"Topilgan harflar: ",end="")
            for i in topilgan_harflar:
                print(i.upper(),end="")
            print("\nKiritgan harflar:",end="")
            for i in kiritilgan_harflar: print(i.upper(),end="")
            urunishlar_soni+=1

        else: print(f"Siz {harf.upper()} harfini oldin kiritgansiz boshqa harf kiriting: ")
        if "_" not in topilgan_harflar: break
    return urunishlar_soni

def play():
    while True:
        soz = choice(words)
        urinishlar = soz_top(soz)
        print(f"\nTabriklayman. Siz {soz.upper()} so'zini {urinishlar} ta urinishda topdingiz!!")
        savol = int(input("Yana o'ynaymizmi ha(1)/yo'q(0)"))
        if savol == 0: break
play()

