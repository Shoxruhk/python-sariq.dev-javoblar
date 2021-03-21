# Bu dasturda biz tub sonlari aniqlaymiz
def tub_son(son):
    k = 0
    q = 0
    son = int(son)
    for i in range(son+1):
        w = 0
        for j in range(2,i+1):
            if i%j == 0:
                w+=1
        if w==1:
            print(i, end=" ")
            k += 1
        if k == 30 and True:
            print()
            k = 0
            q += 1
    print('Jami', k+q*30, 'ta tubson bor')
son = input('Qaysi songacha tub sonlar royhatini kormoqchisiz: ')
tub_son(son)
# k = 0
# son = int(son)
# for bolunuvchi in range(3,son+1):
#     s = 0
#     for boluvchi in range(2,son):
#         if bolunuvchi%boluvchi==0:
#             s += 1
#     if s == 1:
#         print(bolunuvchi)
#         k += 1
# print()
# print(k)