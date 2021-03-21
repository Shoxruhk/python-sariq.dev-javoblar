# biz bu dasturda fibonachi formulasi yordamida sonlarni chiqaramiz
# fibonachi funksayini yozamiz
def fibonachi(son):
    """Fibonachi teoremasi siz kiritgan son miqdorida fibonachi sonlar qaytaruvchi funksiya"""
    son = int(son)
    a = 0
    b = 0
    son1 = 0
    son2 = 1
    print(son1 + son2, son2+son1, end=",")
    for i in range(son):
        if a == 0:
            son1 = son1 + son2
            b = 0
        if a == 1:
            son2 = son1 + son2
            a = 0
        if b == 0:
            a += 1
            b += 1
        else: b = 0
        if i == son-1: print(son1+son2, end="")
        else: print(son1+son2, end=",")
son = input("Butun kiriting: ")
fibonachi(son)
