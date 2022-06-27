##### ALIŞTIRMALAR ########

# SORU:
# 1 1-15 arasında 5'er adet sayı üretip 2 farklı kümeye kaydediniz.
# Daha Sonra iki kümeyi ekrana yazdırınız.

# from random import randint
#
# kume1 = set( )
# kume2 = set( )
#
# #1 YOL
# for i in range(5):
#
# 	while True:
# 		sayi =  randint(1,15)
# 		if sayi not in kume1:
# 			kume1.add(sayi)
# 			break
# 		else:
# 			print("Bu Sayı 1. kümede var")
#
# 	while True:
# 		sayi =  randint(1,15)
# 		if sayi not  in kume2:
# 			kume2.add(sayi)
# 			break
# 		else:
# 			print("Bu Sayı 2. kümede var")
#
# print(kume1)
# print(kume2)
#
# # 2. YOL
#
# kume1 =  set()
# kume2 = set()
#
# while len(kume1) <5:
# 	kume1.add(randint(1,15))
#
# while len(kume2) <5:
# 	kume2.add(randint(1,15))
#
#
# print(kume1)
# print(kume2)

# SORU: 1-100 arasında rastgele 10 sayı üretip bir listeye atayın.
# Daha sonra bu listedeki en büyük ve en küçük elemanları hazır fonksiyon kullanmadan bulun.
#  (liste ile çözün-max(),min(),sort(),reverse())

from random import randint

liste = list( )

for i in range( 1, 11 ):
	liste.append( randint( 1, 100 ) )

print( liste )

kucuk = 100
buyuk = 1
for eleman in liste:
	if eleman > buyuk:
		buyuk = eleman
	if eleman < kucuk:
		kucuk = eleman

print( f"Listedeki en küçük sayı: {kucuk}" )
print( f"Listedeki en büyük sayı: {buyuk}" )

print( f"Listedeki en küçük sayı: {min( liste )}" )
print( f"Listedeki en büyük sayı: {max( liste )}" )
