# max qiymatni topuvchi funksiya yaratamiz
def kattasi(x,y,z):
    katta = None
    if x>y and x>z: katta = x
    elif y>x and y>z: katta = y
    else: katta = z
    return katta
x = float(input('1 chi sonni kiriting: '))
y = float(input('2 chi sonni kiriting: '))
z = float(input('3 chi sonni kiriting: '))
print(kattasi(x,y,z))
