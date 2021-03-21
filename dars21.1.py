# royhatdan malumot olib birinchi harfini katta harf qiluvchi funksiya yozing
# katta harf nomli funksiya yaratib olamiz
def katta_harf(matnlar):
    index = 0
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
        index += 1
    return matnlar

letters = ['salom','alik','assalom','qalesan']
letter2 = katta_harf(letters[:])
print(letters)
print(letter2)