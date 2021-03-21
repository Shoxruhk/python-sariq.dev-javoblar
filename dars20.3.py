# aylananing radiusi yordamida amallar bajarsin

def aylana(radius):
    """Aylana radiusi yordamida uning qiymatlarni topish funksiyasi"""
    radius = float(radius)
    doira = {
        'radius':radius,
        'diametr':radius*2,
        'primetr':radius*2*3.14,
        'yuzi':radius**2*3.14
    }
    return doira
radius = input('Aylana radiusni kiriting: ')
for nom , qiymat in aylana(radius).items():
    print(f"{nom.title()}: {qiymat}")