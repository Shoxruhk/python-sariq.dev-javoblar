# bu darsda buyurtmalar bilan ishlaymiza
buyurtmalar = ['olma', 'non', 'yog', 'gosht', 'guruch', 'meva', 'piyoz', 'sabzi']
# while True:
#     buyurtma = input('Nima buyurtma berasiz: ')
#     buyurtmalar.append(buyurtma)
#     test = input("Yana buyurtma berasizmi (ha/yo'q)")
#     if test == "yo'q": break
# print('Buyurtmalaringiz')
# for i in buyurtmalar:
#     print(i)

# Elektron bozor lugatini yaratamiz
# e_bozor = {}
# while True:
#     ism = input('Mahsulot nomi: ')
#     narx = int(input(f"{ism.title()}ning narxi: "))
#     e_bozor[ism] = narx
#     shart = input('Yana malulot kiritasizmi (ha/yoq) >>>>')
#     if shart != 'ha':
#         print()
#         break
# for ism, narx in e_bozor.items():
#     if ism in buyurtmalar:
#         print(f"{ism.title()} ni narxi {narx}")
#     else: print(f"Kechirasiz bizda {ism} mahsuloti yo'q")
a=1
bozorliklar = {}
while buyurtmalar:
    a+=1
    info = buyurtmalar.pop()
    bozorliklar[info] = 0
print(bozorliklar.items())