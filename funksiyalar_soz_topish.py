# assalomu alaykum bu yerda soz oyini uchun funksiyalar yaratamiz

# Birinchi navbatda biz tayyor royhatdan bitta sozni generansiya qilib olvolamiz

from kiril_perevot import lugatlar
from random import choice
from uzwords import words

def get_word(words):
    """Bu funksiya words royhatidan tasodifiy bitta so'z qaytaradi"""
    word = choice(words)
    # bu yerda sozimizda bo'shliq yoki tere borligini tekshiradi bolsa boshqa soz qaytaradi
    while "-" in word or " " in word:
        word = choice(words)
    return word

# Foydalanuvchi kiritgan harflarni sozda borlarini tekshiramiz
def correct_word(input_words,word):
    """Kiritilgan harflar topilayotgan soz ichida bor yoki yoqligini aniqlovchi funksiya"""
    correct_words = ''
    # qidirilayotgan sozni ichida kiritilgan harflar bor yoki yo'qligini tekshirib qiymay qo'shadi
    for letter in word:
        if letter in input_words:
            correct_words +=letter.upper()
        else: correct_words +="-"
    return correct_words.upper()

# play funksiya yaratib olamiz va shu funksiyada oyin oynashni boshlemiz

def play():
    """Kompyuter oylagan so'zni topish funksiyasi"""
    print("\nKeling men so'z o'ylayman. Siz toping!!!")
    uz_ru = input("Qaysi alifboda o'ynaymiz kiril(ru)/lotin(uz)")
    if uz_ru == "ru":  word = get_word(words)
    else: word = get_word(lugatlar)


    print(f"Men {len(word)} xonali so'z o'ladim. Topishga harakat qiling!")
    print("-"*len(word))
    input_letters = ''
    urinishlar = 0
    while True:
        if uz_ru=="ru": letter = input("Харфни кирил алифбосида киритинг >>> ")
        else: letter = input("Marhamat harf kiriting >>> ")
        if letter not in input_letters:
            urinishlar+=1
            input_letters+=letter
            if letter in word:
                print(f"Qoyil. {letter.upper()} harfi to'g'ri! ")
                print(f"Topilgan harflar")
                print(correct_word(input_letters,word))
                print(f"Shu paytgacha kiritilgan harflar {input_letters.upper()}")

            else:
                print(f"\nTopaolmadingiz. Boshqa harf kiriting ")
                print(f"Topilgan harflar")
                print(correct_word(input_letters, word))
                print(f"Shu paytgacha kiritilgan harflar {input_letters.upper()}")
        else: print(f"Kechirasiz {letter.upper()} harfi oldinroq kiritilgan.")
        if "-" not in correct_word(input_letters,word): break
    print(f"Tabriklayman. Siz {word.upper()} so'zini {urinishlar-1} ta urinishda topdingiz!!!")

while True:
    play()
    javob = int(input("Yana o'ynaysizmi ha(1)/yo'q(0)"))
    if javob == 0: break
print("Siz bilan o'ynaganimdan hursandman!!!")
