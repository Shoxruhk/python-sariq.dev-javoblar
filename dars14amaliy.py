# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:22:45 2021

@author: Shoxrux
"""

# =============================================================================
# # qarindoshlar nomli ro'yhat yaratamiz lugat tipida
# qarindoshlar = {
#     'dadam':'Ismi Shuhrat, 1968 - yilda tug\'ulgan malumoti oliy',
#     'onam': "Ismi Sahobat, 1968 i yilda tavallud topgan, ma'lumoti oliy",
#     'akam': 'Ismi Jahongir, 1993 - yilda tug\'ulgan , malumoti o\'rta',
#     'singlim':'Ismi Zebo, 2006 - yil, maktabda o\'quvchi'
#     }
# soz = input('kalit sozni kiriting\n')
# print(qarindoshlar.get(soz,'bunday qiymat mavjud emas'))
# =============================================================================

# sevimli taomlar nomli lugat yaratamiza
taomlar = {
    'ali':'mastava',
    'bahrom':'osh',
    'hamid':'manti',
    'eshmat':'dimlama',
    'ishmat':'osh'
    }
soz = input('kalit sozni kiriting: ')
print(taomlar.get(soz))