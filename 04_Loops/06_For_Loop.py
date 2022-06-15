"""
i=1
while(i<10):
    print(i)
    i+=1
"""

##### FOR DONGUSU #####

# RANGE aralık belirtmememizi sağlıyor 0
#
# range( 5 )  # 0-5  aralığı
# range( 1, 5 )  # 1-5 aralığı
# range( 1, 9, 3 )  # 1,4,7
#
# """
# for i in range(aralığı):
#     gerekli işlemler
# """
#
# # 0 - 5 aralığındaki sayılar
# for elma in range( 6 ):
#     print( elma )
#
# for i in range( 1, 5 ):
#     print( i )
#
# for i in range( 1, 9, 3 ):
#     print( i )
#
# ilce = "Kadıköy"
# for harf in ilce:
#     print( harf )
#
# ##### ALIŞTIRMALAR #####
# # 1 ile 40 arasındaki sayıları toplayan programı yazınız. 40 dahil.
#
# toplam = 0
# for sayi in range(1,41):
#     toplam += sayi
#
# print(f"1'den 40' a kadar olan sayıların toplamı {toplam}")

"""
toplam = 0
sayi = 1
while (sayi < 41):
    toplam += sayi
    sayi +=1
"""
## SORU 20-40 arasındaki çift ve tek sayıların
# toplamlarını ayrı ayrı ekrana yazdırınız.

cift_toplam =0
tek_toplam = 0
for sayi in range(20,41):
    if sayi % 2 == 0:
        cift_toplam += sayi
    else:
        tek_toplam +=  sayi

print(f"""
        Çift Sayıların Toplamı          : {cift_toplam}
        Tek Sayıların Toplamı           : {tek_toplam}
""")


# 1'den başlayarak Klavyeden girilen sayıya kadar olan
# sayılardan 4'e tam bölünenlerinin çarpımını yazdırınız

# bitis =  int(input("Sayıyı giriniz: "))
# carp = 1
# for i in range(1, bitis+1):
#     if i % 4 == 0:
#         carp *= i
#
# print(f"Sonuç : {carp}")


# SORU: klavyeden girilen sayının rakamları
# ütoplamını ekrana yazdıran prog. #345  => 12
# bitis =  int(input("Sayıyı giriniz: "))
# toplam =  0
#
# for i in range(0,bitis+1):
#     toplam += i
#
# print(f"Sonuç : {toplam}")


# Aşağıdaki çıktıları veren kodları for döngüsü ile yazınız
print("Ahmet" *2) #kopya

"""
*
**
***
****
*****
"""

for i in range(1,6):
    print("" * i)


"""
*****************
*               *
*               *
*               *
*               *
*****************

"""
#
# for i in range(1,7):
#     if i == 1 or i == 6:
#             print("*"*15)
#     else:
#         print("*", (" "*13), "*", sep="")
#


"""
            *
           ***
          *****
         *******
        *********
        
        """

sayac =  1
for satir  in range(1,6):
    print(" "*(5-satir), end="")

