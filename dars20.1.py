# qiymat qaytaruvchi funksiya tuzamiz
def malumot(ism,familiya,tyili,email = '',tel_raqam = None):
    malumotlar = {
        'ism':ism,
        'familiya':familiya,
        'yil':int(tyili),
        'yoshi':(2021-int(tyili)),
        'email':email,
        'telefon':tel_raqam
    }
    return malumotlar
mijozlar = []
while True:
    print('\nMijozlar haqida malumotlar kiritamiz')
    ism = input('Ismingizni kiriting: ')
    familiya = input('Familiyangizni kiriting: ')
    yili = int(input('Tug`ulgan yilingiz: '))
    email = input('emailingizni kiriting: ')
    telefon = input('Telefon raqam')
    mijozlar.append(malumot(ism,familiya,yili))
    soz = input('Yana mijoz qo`shasizmi (yes/no)')
    if soz == 'no': break

for mijoz in mijozlar:
    print(f"Assalomu alaykum {mijoz['familiya'].title()} {mijoz['ism'].title()}, yoshingiz {mijoz['yoshi']} da")


# # salom takrorlaymiza
# def lugat(ism,familiya,yil,ochestvo=''):
#     ismlar = {
#         'ism':ism,
#         'familiya':familiya,
#         'yil':yil,
#         'ochestvo':ochestvo
#     }
#     return ismlar
# soz = (lugat('Assalom',"Alaykum",1999))
# print(soz['familiya'])