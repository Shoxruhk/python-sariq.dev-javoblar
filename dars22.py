# assalomu alaykum biz ozgaruvchan funksiyalar bilan tanishamiz

def summa(*sonlar):
    """Kiritilgan sonlar yigindisini qaytaruvchi funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi


def kopaytma(*sonlar):
    """Bu funksiya faktaryal qiymat qaytaradi"""
    hisobla = 1
    for i in sonlar:
        hisobla *= i
    return hisobla

# talaba nomli funksiya yaratamiz ism va familiya majburiy qolganini esa ixtiyoriy

def talaba(ism,familiya,**malumotlar):
    """Talaba haqida malumotlarni shakllantiramiz"""
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
# print(talaba("Shoxrux","Erqo'ziyev"))
# print(talaba("Shoxrux","Erqo'ziyev,",yoshi = 25, malumoti = "tugallanmagan oliy"))
# talaba()
