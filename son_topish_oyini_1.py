# bu dasturda biz son topish oyinini qilamiz yani kompyuter bilan oynaymiz u oyledi biz topamiz kegin aksincha
# qani kettik bolmasa qadrdonlarim
# birinchi navbatda biz tasodifiy sonlar generatsiyasini vujutga keltiramiz random moduli yordamida

from random import randint
while True:
    son = randint(1,10)
    print("Keling siz bilan son topish o'yini o'ynaymiz!!!")
    print("1 dan 10 gacha oraliqda bitta son o'ylang!!!")
    # endi biz whili funksiyasi yordamida kompyuter oylagan sonni topishga harakat qilamiz
    hisob = 0
    while True:
        son_kirit = int(input(">>"))
        hisob+=1
        if son_kirit == son:
            print(f"TOPDINGIZ!!! {son} sonini o'ylagan edim. {hisob} ta tahmin bilan topdingiz. Tabriklayman!")
            break
        elif son_kirit <= son:
            print("Xato! men o'ylagan son bundan kattaroq, yana harakat qilib ko'ring ")
        else: print("Xato! men o'ylagan son bundan kichikroq, yana harakat qilib ko'ring ")
    # tepadagi metodda biz kompyuter oylagan sonni tokdik
    # endi esa kompyuter biz oylagan sonni topsin

    print("\n1 dan 10 gacha son o'ylang! endi men topishga harakat qilaman")
    print("\nAgar son o'ylagan bo'lsangiz kirish(Enter) tugmasini bosing!!!")
    input()
    hisob2 = 0
    son1 = 1
    son2 = 10
    while True:
        hisob2+=1
        son = randint(son1,son2)
        kirit = input(f"Siz {son} sonini o'yladingiz. "
                      f"to'g'ri (t), men o'ylagan son bundan kattaroq (+) yoki kichikroq (-) ")
        if kirit == 't':
            print(f"Soningizni {hisob2} ta tahmin bilan topdim!!!")
            break
        elif kirit == "+": son1 = son + 1
        else: son2 = son - 1

    # endi biz natijalarni tekshiramiz
    if hisob2 == hisob: print(f"Durrang! Ikkimiz {hisob2} ta tahmin bilan topdik ")
    elif hisob2 > hisob:
        print(f"Tabriklayman siz yutdingiz! Siz {hisob} ta tahminda topdingiz")
    else:  print(f"YUTQAZDINGIZ! Siz {hisob} ta tahminda topdingiz")
    chiqish = int(input("\nYana o'ynaymizmi? ha(1)/yo'q(0) "))
    if chiqish == 0: break
