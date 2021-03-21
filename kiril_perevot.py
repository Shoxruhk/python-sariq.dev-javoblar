# keling sizlar bilan bugun royhatni kiril alifbosidan lotin alifbosiga otkazamiz
# buning uchun bizga tayyor royhat berilgan shu royhatdan foydalanamiz

from  uzwords import words
# bizga birinchi navbatda lotin harflarni shakllantiruvchi funksiya kerak bo'ladi

def translite(word):
    """kiril alifbosidagi so'zni lotin alifbosida qaytaruvchi funksiya"""
    trans_letter = ''
    word = word.lower()
    for letter in word:
        if letter == "ё": letter = "yo"
        elif letter == "й": letter = "y"
        elif letter == "ц" and word[0]: letter = "s"
        elif letter == "ц" and word[-1]: letter = "z"
        elif letter == "ц": letter = "ts"
        elif letter == "у": letter = "u"
        elif letter == "к": letter = "k"
        elif letter == "е" and word[0] == "е": letter = "ye" 
        elif letter == "e": letter = "e"
        elif letter == "н": letter = "n"
        elif letter == "г": letter = "g"
        elif letter == "ш": letter = "sh"
        elif letter == "ў": letter = "o'"
        elif letter == "з": letter = "z"
        elif letter == "х": letter = "x"
        elif letter == "ҳ": letter = "h"
        elif letter == "ъ": letter = "'"
        elif letter == "ф": letter = "f"
        elif letter == "в": letter = "v"
        elif letter == "қ": letter = "q"
        elif letter == "ғ": letter = "g'"
        elif letter == "а": letter = "a"
        elif letter == "п": letter = "p"
        elif letter == "р": letter = "r"
        elif letter == "о": letter = "o"
        elif letter == "л": letter = "l"
        elif letter == "д": letter = "d"
        elif letter == "ж": letter = "j"
        elif letter == "э": letter = "e"
        elif letter == "я": letter = "ya"
        elif letter == "ч": letter = "ch"
        elif letter == "с": letter = "s"
        elif letter == "м": letter = "m"
        elif letter == "и": letter = "i"
        elif letter == "т": letter = "t"
        elif letter == "б": letter = "b"
        elif letter == "ю": letter = "yu"
        trans_letter += letter
    return trans_letter
# translite funksiyamiz yordamida royhatlarni pervod qiluvchi funksiya yozamiz

def list_translite():
    tarjimalar = []
    for word in words:
        perevot = translite(word)
        tarjimalar.append(perevot)
    return tarjimalar
lugatlar = list_translite()

