# nesting darsiga oid mashqlar
# Adabiyot fanida yutuqqa erish insonlar haqida lugat yaratob olamiz
adabiyot1 = {
    'ism':'alisher navoiy',
    'yonalishi':'shoir',
    'yoshi':65,
    'asar':'ruboiylar toplami'
}
adabiyot2 = {
    'ism':'zahiriddin muhammad bobur',
    'yonalishi':'Buyuk sarkarda, shoir',
    'yoshi':45,
    'asar':'boburnoma'
}
adabiyot3 = {
    'ism':'mirzo ulu\'ug\'bek',
    'yonalishi':'astronomiya',
    'yoshi':50,
    'asar':'ko\'rogoniy jadvali'
}
adabiyot4 = {
    'ism':'muhammad al xorazimiy',
    'yonalishi':'astronomiya va matematika',
    'yoshi':48,
    'asar':'fanga 0 ni kiritagan algoritmni tushunchsini yaratgan'
}
adabiyotlar = [adabiyot1, adabiyot2, adabiyot3, adabiyot4]
# for adabiyot in adabiyotlar:
#     print(f"Buyuk alloma {adabiyot['ism'].title()},"
#           f" ijodkorligi {adabiyot['yonalishi']},"
#           f" {adabiyot['yoshi']} yil umr ko'rgan, "
#           f"hozirda eng buyuk asarlaridan biri {adabiyot['asar'].upper()}")
adabiyot1['asar'] = ['ruboiylar to\'plami','Farhod va Shirin', 'Ramoe va Julyeta']
adabiyot2['asar'] = ['boburnoma', 'urush sahnalari', 'samolar jangi', 'tobutdagi odam']
adabiyot3['asar'] = ['korogoniy jadvali', 'samolar', 'yulduzlar jangi', 'mehr ko\'zda']
adabiyot4['asar'] = ['algoritm tushunchasi', '0 dan 9 gacha raqamlar', 'informatika asoschisi']

# for adabiyot in adabiyotlar:
#     print(f"{adabiyot['ism'].title()} ning eng mashxur asarlari")
#     for asari in adabiyot['asar']:
#         print(asari.capitalize())
#     print()

# kinolar nomi lugat yaratamiz va dostlarni sevimli kinolarini shaklalantiramiz
kinolar = {
    'Shoxabbos':["Mo'jiza",'do`stlik', 'samolardan balantda', 'FIFA tarixi'],
    'Elyor':['ruskiy boyvek','o`shinning 12 do`sti','QVZ','salom sevgi salom g`am'],
    'Doniyor':['jumong','ish ertagi','kayfdagi jo`ralar','o`lginungcha yashab qol'],
    'Bahtiyor':['chegarasizlar 1','chegarasizlar 2', 'chegarasizlar 3', 'chegarasizlar 4']

}
# for ism, kino in kinolar.items():
#     print(f"{ism.title()}ning sevimli kinolari")
#     for n in kino:
#         print(n.capitalize())
#     print()
# davlat nomli lugat shakllantiramiz
davlatlar = {
    'uz':{
        'davlat':'O`zbekiston',
        'poytaxt':'tashkent',
        'maydoni':'449 ming km kvadrat',
        'aholi':34011621,
        'til':"O`zbek",
        'puli':'uzs'
    },
    'ru':{
        'davlat':'rosiya',
        'poytaxt':'moskiva',
        'maydoni':'17.1 mln km kvadrat',
        'aholi':'145.3 mln',
        'til':"rus",
        'puli':'rubl'
    },
    'en':{
        'davlat':'AQSH',
        'poytaxt':'washington',
        'maydoni':'9.373 mln km kvadrat',
        'aholi':750000000,
        'til':"english",
        'puli':'usd'
    },
    'kz':{
        'davlat':'Qozog`iston',
        'poytaxt':'Ostona',
        'maydoni':'2.723 mln km kvadrat',
        'aholi':14000000,
        'til':"qozoq",
        'puli':'tanga'
    }

}
davlat = input('Davlat kalit so`zini kiriting:' )
if davlatlar.get(davlat):
    print(f"{davlatlar[davlat]['davlat'].capitalize()}ning poytahti {davlatlar[davlat]['poytaxt'].title()}\n"
          f"Maydoni {davlatlar[davlat]['maydoni']} metr\nAholisi {davlatlar[davlat]['aholi']} kishi"
          f" \nDavlat tili {davlatlar[davlat]['til'].capitalize()} \nPuli birligi {davlatlar[davlat]['puli'].upper()}")
    print()
else: print('Afsus bunday ma`lumot bizda mavjud emas')