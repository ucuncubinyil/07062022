########## RANDOM KÜTÜPHANESİ ###########

import random

print( random.random( ) )  # 0-1 arasında  noktalı rastgele sayı üretir

print( random.randint( 1, 100 ) )  # 1-100 arasında rastgele tam sayı üretir

print(random.uniform(1,100)) # 1-100 arasında noktalı sayı üretir

print(random.randrange(1,100)) # minimum ve maxumum değerler haricinde rastgele sayı üretir

print(random.randrange(1,100,3)) # 1-100 arasında ki sayıların 3 e bölündüğünde kalanı 1 olan sayılar arasında rastgele üretir

print(random.uniform(100000.0000,999999.9999))