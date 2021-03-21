# range funksiyasini qaytadan yozamiz
def oraliq(min,max,qadam = 1):
    """Range funksiyasini qayta yozamiz"""
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar
print(oraliq(0,10,8))