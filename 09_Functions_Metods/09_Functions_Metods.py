#### ARMSTRONG SAYISI ####

"""
armstrong sayısı
1634 -> 1^4 + 6^4 + 3^4 + 4^4 =1634 --> armstrong sayısıdır.
25 -> 2^2 + 5^2 = 29 --> armstrong sayı değildir.

"""

## Kullanıcı bir sayı girecek bu sayı armstrong alup olmadığı ekrana yazdırınız..
#
# sayi =  input("Sayi gir: ")
#
# toplam =  0
# uzunluk =  len(sayi)
#
# for item in sayi:
# 	toplam += int(item) **uzunluk
# 	print(toplam)
#
# if toplam == int(sayi):
# 	print("Sayi bir amstrong sayısıdır")
# else:
# 	print("değildir")
#

# 1000000 sayısına kadar armstrong olan sayıları ekrana yazdırınız.
#
# for i in range(1000000):
# 	toplam = 0
# 	uzunluk =  len(str(i))
# 	for item in str(i):
# 		toplam += int(item) ** uzunluk
#
# 	if toplam == int(i):
# 		print(i, " amstrong dur")
#
	
################# FONKSİYONLAR #####################
	
"""
Programımızda belirli vir işi yapan kod bloklarının tekrar kullanılması durumunda tekrar yazılmadan çağrılmasını
sağlayan modüllerdir.
Yani bir modülü 1 defa tanımlayıp istediğimiz zaman istediğimiz kadar kullanabilmemizi sağlar.
Fonksiyonlar yazdığımız programın modüler olmasını sağlar, ayrıca okunabilirliği artırır.

Fonsksiyonlar 2'ye ayrılır.
    Değer Döndüren Fonk. => parametreli ve parametresiz
    Değer Döndürmeyen Fonk. => parametreli ve parametresiz
"""
# Fonksiyon Tanımlama

"""
Deger döndürmeyen
def fonksiyonismi(varsa parametre):
	bu fonksiyonda çalıştırılacak kodlar yazılır

Deger döndüren
def fonksiyonismi(varsa parametre):
	bu fonksiyonda çalıştırılacak kodlar yazılır
	return deger

"""
#
# def merhaba_dunya():
# 	print("Merhaba dünya")
#
#
# #Fonksiyon çağırma
# merhaba_dunya()

# global keyword; fonksiyon içerisindeki değişkenleri local olmaktan çıkartır.
	
# sayi1, sayi2 = 10,20
#
# ad = "Mehmet" # global değişken
# def degistir():
# 	global sayi1, sayi2
# 	global  ad
# 	ad = "Mehmet Nuri"
# 	sayi1 ,sayi2 = 100,200
# 	print(sayi1,sayi2)
#
# degistir()
# print(ad)
# print(sayi1,sayi2)
#
# # Parametresiz Metot değer döndürmeyen
# def topla():
# 	sayi =  int(input("1.sayı"))
# 	sayi2 =  int(input("2.sayı"))
# 	print(sayi2+sayi)
# topla()
#
#
#
# # Parametresiz Metot değer döndüren
# def topla2():
# 	sayi =  int(input("1.sayı"))
# 	sayi2 =  int(input("2.sayı"))
# 	return  sayi +sayi2
#
# sonuc =  topla2()
# print(sonuc)

# Parametreli Metot değer döndürmeyen
# def topla(s1,s2):
# 	print(s1+s2)
#
#
# sayi1 = int(input("1.sayi"))
# sayi2 = int(input("2.sayi"))
#
# topla(sayi1,sayi2)
#
# # Parametreli Metot değer döndüren
# def topla2(s1,s2):
# 	return int(s1)+ int(s2)
#
#
# sonuc =  topla2(sayi1,sayi2)
# print(sonuc)


######### ALIŞTIRMALAR ##########

#SORU: Kullanıcıdan 2 sayı 1 işlem alalım ve alınan sayılara verilen işlemi uygulayan ve ekrana yazdıran fonksiyonu yazınız.
#
# def dort_islem(s1,s2,islem):
#
# 	if  islem == "+":
# 		return  s1+s2
# 	elif islem == "-":
# 		return  s1-s2
# 	elif islem == "*":
# 		return s1*s2
# 	elif islem == "/":
# 		if s2 == 0:
# 			print("Hiç bir sayı sıfıra bölünemez")
# 		else:
# 			return s1/s2
# 	else:
# 		return  0
#
#
# while True:
# 	cevap = input("İşlem yapmak ister misiniz? (E/H)").upper()
#
# 	if cevap == "E":
# 		sayi1 =  int(input("Sayı 1: "))
# 		sayi2 =  int(input("Sayı 2: "))
# 		islem =  input("İşlem (+,-,/,*) ")
#
# 		sonuc = dort_islem(sayi1,sayi2,islem)
# 		if sonuc != None:
# 			print(sonuc)
# 	else:break


## SORU: Kendisine gönderilen sayı adedince klavyeden girilen ismi alıp listeye atan fonksiyonu yazınız.
#
# def  isim_yaz():
# 	isim_liste= list()
#
# 	sayi = int(input("Kaç kişi kayıt edilecek"))
# 	for i in range(sayi):
# 		isim = input(f"{i+1} . isim: ")
# 		isim_liste.append(isim)
# 	print(isim_liste)
#
# isim_yaz()


# liste = list()
#
# def isim_ekle(isim,liste):
# 	liste.append(isim)
#
# sayi = int(input("Kaç kişi kayıt edilecek"))
# for i in range(sayi):
# 	isim = input(f"{i+1} . isim: ")
# 	isim_ekle(isim,liste)
# print(liste)
#
# ## Parametre olarak aldığı listedeki tek elemanları yazdıran fonksiyonu yazınız.
#
# def liste_yazdir(isim_listesi):
# 	for i in isim_listesi:
# 		print(i)
#
# liste_yazdir(liste)



### Belirsiz sayıda parametre alan fonksiyon ###

def topla(*sayilar): # '*' ifadesi n sayıda parametre alınacağını tanımlar.
	toplam = 0
	
	for i in sayilar:
		toplam += i
		
	return  toplam

sonuc =  topla(665,5245,896)
print(sonuc)