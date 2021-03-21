# Funksiyalar mavzusi
# foydalanuvchidan ismini soraymiz va yoshini ham funksiya yordamida hisoblaymiz
# def tugulgan_yil(ism, yoshi):
#     """Bu funksiya yordamida siz yoshni kiritish yordamida tugulgan yilni hisoblaydi"""
#     print(f"Assalomu alaykum, {ism.title()} siz {2021 - int(yoshi)} yilda tavallud topgansiz: ")
# ism = input('Ismingizni kiriting: ')
# yosh = int(input('Yoshingiz nechada: '))
# tugulgan_yil(ism,yosh)

# def hisoblash(son):
#     """Sonlarni kvadrati va kubi topuvchi """
#     son = float(son)
#     print(f"{son} sonini kvadrati = {son**2}\n")
#     print(f"{son} sonini kubi = {son ** 3}")
# son = input("Istalgan sonni kiriting: ")
# hisoblash(son)

# def hisoblash(son):
#     """Sonlarni juft yoki toqligini aniqlash """
#     son = int(son)
#     if son%2 == 0:
#         print('juft')
#     else: print('Toq')
# son = input("Istalgan butun sonni kiriting: ")
# hisoblash(son)

# def katta_kichik(son1,son2):
#     """sonlarni kattasini aniqlaydi"""
#     son1 = int(son1)
#     son2 = int(son2)
#     if son1 == son2: print('teng')
#     else: print(max(son1,son2))
# son1 = input('1 chi butun sonni kiriting: ')
# son2 = input('2 chi butun sonni kiriting: ')
# katta_kichik(son1,son2)

# def kvadrat(x,y=2):
#     '''Bu kritilgan sonni darajaga kotaradi'''
#     x = int(x)
#     y = int(y)
#     print(x**y)
# x = input('X ni kiriting ')
# y = input('y ni kiriting')
# kvadrat(x,y)

def qoldiq_topish(son):
    """Sonlarni 2 10 gacha sonlarga bolinishini chiqaradi"""
    son = int(son)
    for i in range(2,11):
        if son%i == 0:
            print(f"{son} soni {i} ga qoldizsiz bo'linadi")
        else: print(f"{son} soni {i} ga bo'linmaydi")
son = input('Istalgan butun son kiriting')
qoldiq_topish(son)