from random import randint
numbers = list(range(1,101))
numbers.pop(randint(0,100))
tahmin = 1
for i in numbers:
    if tahmin != i: break
    else: tahmin+=1
print(f"Tushub qolgan son {i-1}")
print(numbers)