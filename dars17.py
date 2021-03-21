# salom biz bugun while sikli haqida misollar koramiz
# ism = input('Ismingizni kiriting: ')
# savol = f"Salom {ism.title()} yaxshi ko\'rgan kitoblaringizni kiriting "
# savol += 'dasturni tugatmoqchi bo\'lsangiz stop kiriting: '
# kitoblar = []
# while True:
#     kitob = input(savol)
#     if kitob == 'stop':
#         break
#     else:
#         kitoblar.append(kitob.title())
# print('dastur tugani \n',kitoblar)

# Chipta narxini hisoblovchi dasturcha
# soz = ''
# while True:
#     yosh = input('Yoshingizni kiriting: ')
#     if yosh == 'exit' or yosh == "quit": break
#     if yosh.isdigit():
#         yosh = int(yosh)
#         if yosh < 7: soz = '2000'
#         elif yosh >= 7 and yosh <= 18: soz = '3000'
#         elif yosh > 18 and yosh <= 65: soz = '10000'
#         else:
#             print('Sizga bepul:')
#             continue
#         print(f"Sizga chipta narxi {soz} so'm")
#
#     else: print('Notogri qiymat kiritdingiz:')
#     print('Dasturni yopmoqchi bo\'lsangiz exit yoki quit deb kiriting')

# domlaning vazifasi unung kodi

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat.isdigit()<0:
        continue
    elif qiymat.capitalize()=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")