# assalomu alaykum
# bugungi dasr funksiyaga royhatlarni togri kochirish bilan tanishdik

# baholar nomli funksiya yaratamiz qani kettik

def bohola(ismlar):
    boholar = {}
    for ism in ismlar:

        boho = input(f"{ism.title()}ning bohosini kiriting: ")
        boholar[ism] = int(boho)
    return boholar
talabalar = ['anvar','shokir','nodir','jamshid']
print(bohola(talabalar))
print(talabalar)