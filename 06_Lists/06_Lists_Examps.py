### ALIŞTIRMALAR ###
# SORU: Kullanicidan 10 adet sayı alıp listeye atın
# ve sonrasında listenin aritmatik ortalamasını bulun.

# liste = []
#
# for i in range(1,11):
# 	sayi = int(input(f"{i}. sayıyı girin: "))
# 	liste.append(i)
#
# print(f"Listedeki elemanların toplamı {sum(liste)}")
# print(f"Listedeli eleman sayısı {len(liste)}")
# print( sum(liste) / len(liste) )

# 1. 1-100 arasında 20 adet sayı üretip listeye atın.

# import random
# #
# # sayilar = list( )
# # for i in range( 20 ):
# # 	sayi = random.randint( 1, 100 )
# # 	sayilar.append( sayi )
# # print( sayilar )
#
# # tekrar edeni atma yeniden rastgele sayi üret
# sayilar = list( )
# for i in range( 20 ):
# 	sayi = random.randint( 1, 100 )
#
# 	if sayi in sayilar:
# 		for x in range( 101 ):
# 			sayi = random.randint( 1, 100 )
# 			if sayi not in sayilar:
# 				sayilar.append( sayi )
# 				break
# 	else:
# 		sayilar.append(sayi)
#
# sayilar.sort()
# print( sayilar )
#
# sayilar.sort(reverse=True)
# print( sayilar )
#

# 2. Sonra kullanıcıdan 3 tahmin hakkı verip listeden 1 sayıyı tahmnin etmesini isteyin.
# for i in range(3):
# 	tahmin = int(input(f"{i+1}. tahmininiz: "))
# 	if tahmin in sayilar:
# 		print("Tebrikler")
# 		break
# 	else:
# 		print("Tekrar deneyin...")

# hak = 3
# while hak > 0:
# 	hak -= 1
# 	tahmin =  int(input("Tahmininiz: "))
# 	if  tahmin in sayilar:
# 		print("Tebrikler")
# 		break
# 	else:
# 		print("Tekrar deneyin...")


# 2. sayilar listesindeki sayıları ciflistesi
# ve teklistesi isimindeki iki ayrı listeye kontrol ederek ekleyiniz.

# cift = list()
# tek = list()
#
# for i in range(1,200):
# 	if i % 2 == 0:
# 		cift.append(i)
# 	else:
# 		tek.append(i)
#
# print(cift)
# print(tek)

#ASAL SAYI BULMA KODU

# sayi = 123
# asal_mi = True
#
# if sayi > 1:
# 	for i in range(2,sayi):
# 		if (sayi % i == 0):
# 			asal_mi = False
# 			print(i)
# 			break
# else:
# 	asal_mi = True
# 	print("Asal")
#
#
# if asal_mi:
# 	print("Asal")
# else:
# 	print("Asal değil")
#
# sayi = int(input("Kontrol edilecek sayiyi girin: "))
# asal_mi =  True
# for i in range(2, sayi):
# 	if sayi % i == 0:
# 		asal_mi = False
# 		break
#
# if asal_mi:
# 	print("Asal")
# else:
# 	print("Asal değil")


# SORU: Klavyeden alınan 5 kelimeyi bir listeye atın.
# : Girilen 6. kelimenin listede olup olmadığını ekrana yazdırınız.

# sayac = 1
# kelimeler = list()
#
# while sayac < 7:
# 	kelime =  input("Kelimeyi girin")
# 	if sayac < 6:
# 		if kelime not in kelimeler:
# 			kelimeler.append(kelime)
# 			sayac +=1
# 		else:
# 			print(f"{kelime} zaten listede mevcut")
# 	else:
# 		if kelime in kelimeler:
# 			print(f"{kelime} kelimeler listesinde mevcut")
# 			break
# 		else:
# 			print(f"{kelime} kelimeler listesinde mevcut değil")
# 			break



## Klavyeden -1 girilene kadar girilen sayıları bir listeye atsın.

# sayilar = list()
# sayi =  int(input("Sayi: "))
# while sayi != -1:
# 	sayilar.append(sayi)
# 	sayi =  int(input("Sayi: "))
# print(sayilar)

### ÇOK BOYUTLU LİSTELER
cokBoyutlu = [[1,2,3],[4,5,6]] # 2x3 matris(liste)
print(cokBoyutlu[0][0])
print(cokBoyutlu[0][1])
print(cokBoyutlu[0][2])

print(cokBoyutlu[1][0])
print(cokBoyutlu[1][1])
print(cokBoyutlu[1][2])













