# TERSTEN YAZDIRMA
#
# for i in range(10,0,-2): # -1  ters aralık verir
#     print(i),
#
# ## ÇARPIM TABLOSU
# """
# 1 x 1 = 1 1 x 2 = 2 1 x 3 =3
# 2 x 1 = 2 ....
# 3 x 1 = 3
# """
#
# for i in range(1,10):
#     for j in range(1,10):
#         print(i, "x", j , "=", (i*j), end="     ")
#     print()
#
#
# #Sep Kullanımı
# print("Mehmet Nuri", "Öztürk", sep=" ")


#SORU: Kullanıcıdan personel sayısını alınız.
# Personelin kaç çocuğu olduğunu isteyelim.
# Program her çocuk için "Çocuğunuz adına 1 ağaç dikilmiştir" yazsın
# Toplam dikilen ağaç sayısınıda ekrana yazdıralım.

# toplam_agac = 0
# persayi = int(input("Personel Sayısını Giriniz: "))
#
# for i in range(1,persayi+1):
#     while True:
#         cocuk_sayisi = int(input(f"{i}. personel Çocuk sayısını giriniz:"))
#         toplam_agac += cocuk_sayisi
#         break
#
#     for j in range(cocuk_sayisi):
#         print("Çocuğunuzun adına 1 Ağaç dikilmiştir.")
#

#### TAHMİN OYUNU ####
# Bilgisayar 1-100 arasında rastgele bir sayı üretsin.
# Kullanıcının 5 hakkı olsun ve sayıyı bilmeye çalışsın.
# Bilirse TEBRİKLER. bilemezse tekrar deneyiniz. hakkı biter hakkınız bitti yazsın.
# BONUS: tahmin değeri rastgele değerden büyük ise tahmininizi küçültünüz
#        tahmin değeri rastgele değerden küçük ise tahmininizi büyültünüz

import random
rast_gele_sayi = random.randint(1,100)
# hak = 5
# while hak > 0:
#     hak -=1
#     tahmin =  int(input("Tahmin ettiğiniz sayı: "))
#     if (rast_gele_sayi > tahmin):
#         print("Tahmin sayınızı arttırınız !")
#     elif (rast_gele_sayi < tahmin):
#         print("Tahmin sayınızı küçültün")
#     else:
#         print("Tebrikler !!!")
#         break
# if hak == 0:
#     print(rast_gele_sayi)
#     print("Hakkınız bitti")
#


# for hak in range(1,6):
#     tahmin = int(input(f"{hak}. tahmininiz " ))
#
#     if (rast_gele_sayi > tahmin and hak < 5):
#         print("Tahmin sayınızı arttırınız !")
#
#     elif (rast_gele_sayi < tahmin and hak < 5):
#         print("Tahmin sayınızı küçültün !")
#
#     elif rast_gele_sayi == tahmin:
#         print("Tebrikler")
#         break
#     else:
#         print(rast_gele_sayi)
#         print("Hak bitti")

for i in range(1,6):
    print("👽"*i)













