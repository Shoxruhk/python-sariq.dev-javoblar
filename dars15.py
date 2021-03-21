# =============================================================================
# # izohli lugat yaratamiz
# python_izohli_lugati = {
#     "float":'haqiqiy son',
#     'int':'butun son', 'string':'satrli ma\'lumot',
#     'tuple':'ozgarmas ro\'yhat', 'bool':'mantiqiy qiymat',
#     'title':'Sozni bosh harfini kattalashtiradi',
#     "set":'tartiblash royhatlar chiqaradi',
#     'import':'kutubxona chaqiradi',
#     'for':'takrorlanish hosil qiladi',
#     'if':'tarmoqlanuvchi'
# }
# for kalit in sorted(python_izohli_lugati):
#     print(f"{kalit} - {python_izohli_lugati[kalit]}")
# =============================================================================
#  DAVLATLAR lugatini yaratamiz
davlatlar = {
    'AQSH':'Washington','Uzbekistan':'Tashkent','Kazakistan':'Astana',
    'Angilya':'London', 'Spaniya':'Madrid', "Fransiya":'Parij',
    'Turkiya':'Anqara','Kirgigistan':'Bishkek'
}
# print('bizni bazada bor davlatlar\n')
# for i in sorted(davlatlar):
#     print(i)
# print('\nDavlatlar poytahtlari\n')
# for i  in sorted(davlatlar.values()):
#     print(i)

# soz = input('Qaysi davlatni poytaxtni bilmoqchisiz: \n>>>>>')
# if soz == 'aqsh' or soz == 'Aqsh':
#     soz = 'AQSH'
# else:
#     soz = soz.title()
# print(soz)
# print(davlatlar.get(soz,'Bunday davlat haqida malumot yoq'))

# restoran menu lugatini tuzamiz
# =============================================================================
# restoran_menu = {
#     'osh':20000, 'manti':10000, 'kabob':15000,
#     'non':3000, 'bishteks':25000, 'norin':30000,
#     'tandir':35000, "free":18000, "cola":7000,
#     'choy':2000, "mastava":10000
# }
# taomlar = []
# for i in range(4):
#     taom = input(f"Buyurtma bermoqchi bo'lgan {i+1} taomingiz yozing: ")
#     taom = taom.lower()
#     taomlar.append(taom)
# print("\n")
# for menu in taomlar:
#     if menu in restoran_menu.keys():
#         print(f"{menu.capitalize()} {restoran_menu[menu]} so'm")
#     else:
#         print(f"Kechirasiz bizda {menu} yo'q")
# =============================================================================
shaharlar = []
print('Siz qaysi 3ta shaharlaga bormoqchisiz:')
for i in range(3):
    shahar = input(f'{i+1} shahar nomini kiriting: ')
    shaharlar.append(shahar)
for shaxar in davlatlar.values():
    if shaxar in shaharlar:
        print(f"Siz bormoqchi bo'lgan {shaxar} shahri {davlatlar.items()} poytahti")

for davlat in davlatlar:
    if davlat in shaharlar:
        print(davlatlar[davlat])