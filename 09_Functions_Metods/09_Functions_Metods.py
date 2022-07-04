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

# SORU: Kullanıcıdan 2 sayı 1 işlem alalım ve alınan sayılara verilen işlemi uygulayan ve ekrana yazdıran fonksiyonu yazınız.
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

# def topla(*sayilar): # '*' ifadesi n sayıda parametre alınacağını tanımlar.
# 	toplam = 0
#
# 	for i in sayilar:
# 		toplam += i
#
# 	return  toplam
#
# sonuc =  topla(665,5245,896)
# print(sonuc)


# Kendisine gönderilen karakter,en,boy parametrelerine göre
# ekrana karakterden oluşan bir dikdörtgen oluşturan fonksiyonu yazınız.

"""
oooooooo
oooooooo
oooooooo
oooooooo
"""

# def dikdortgen_yaz(karakter, en, boy):
# 	for i in range(boy):
# 		print(karakter*en)
#
#
# dikdortgen_yaz("æ", 30,4)


## DEGER DONDUREN FONKSİYONLAR ##
# değer döndürme anahtarı 'return' komutudur.

# kare4 = pow(4,2)
# print("4 ün karesi ", kare4, " !")
#
# def kuvvet_al(taban, us):
# 	sonuc = taban**us
# 	return sonuc
#
# sonuc = kuvvet_al(4,2)
# print("4 ün karesi ", sonuc, " !")

## Bir müşterim dolar'ını euro'ya çevirmek
# istiyor ben dolar/euro endeksini bilmediğim için doları tl => tl euro
#
# def dolar_to_tl(dolar):
# 	return dolar*16.83 # tercih sebebi
#
# def  tl_to_euro(tl):
# 	euro =  tl/17.55
# 	return  euro
#
#
# dolar =  int(input("Ne kadar dolar bozduracaksınız ?"))
# turk_parasi = int(dolar_to_tl(dolar))
#
# print(f"{dolar} $ {turk_parasi} ₺ değerindedir !")
#
# euro =  int(tl_to_euro(turk_parasi))
# print(f"{turk_parasi} ₺ {euro} € değerindedir !")


# Kendisine gönderilen 4 sayının ortalamasını döndüren fonksiyonu yazınız..
#
# def ortalama_hesapla_1(s1,s2,s3,s4):
# 	sonuc =  (s1+s2+s3+s4)/4
# 	return sonuc
#
# def ortalama_hesapla_2(s1,s2,s3,s4):
# 	return (s1+s2+s3+s4)/4
#
#
# sonuc1 =  ortalama_hesapla_1(1,2,3,4)
# sonuc2 = ortalama_hesapla_2(1,2,3,4)
# print(sonuc1)
# print(sonuc2)

# Kendisine gönderilen 4 sınıfa ait notların ortalamasını bulup bir
# listeye atan ve en başarılı sınıfı yazdıran fonksiyonu yazınız.
#
# def ortalama_bul( notlar=list( ) ):
# 	toplam = 0
# 	for i in notlar:
# 		toplam += i
#
# 	return toplam / len( notlar )
#
#
# sinif1 = { 10, 20, 30, 45, 65 }
# sinif2 = { 30, 55, 90, 100, 65 }
# sinif3 = { 0, 30, 66, 88, 23, 44, 95, 21, 36, 56 }
# sinif4 = { 23, 95, 85, 66, 74, 32, 100, 100, 99 }
#
# ortalamalar = list( )
# ortalamalar.append( ortalama_bul( sinif1 ) )
# ortalamalar.append( ortalama_bul( sinif2 ) )
# ortalamalar.append( ortalama_bul( sinif3 ) )
# ortalamalar.append( ortalama_bul( sinif4 ) )
# print( ortalamalar )
#
# print( "En yüksek ortalama: ", max( ortalamalar ) )
# print( "En düşük ortalama: ", min( ortalamalar ) )
#
# """
# { "sinif1": 56, "sinif2": 95, "sinif3":23, "sinif4": 95 }
# """
#
# sinif_ortalamalari = dict( )
# sinif_ortalamalari[ "sinif1" ] =  ortalama_bul( sinif1 )
# sinif_ortalamalari[ "sinif2" ] =  ortalama_bul( sinif2 )
# sinif_ortalamalari[ "sinif3" ] =  ortalama_bul( sinif3 )
# sinif_ortalamalari[ "sinif4" ] =  ortalama_bul( sinif4 )
#
# en_dusuk = min( sinif_ortalamalari.values( ) )
# en_yuksek = max( sinif_ortalamalari.values( ) )
#
# en_yuksek_sinif = ""
# en_dusuk_sinif = ""
#
# for i, k in sinif_ortalamalari.items( ):
# 	if k == en_dusuk:
# 		en_dusuk_sinif =  i
#
# 	if k == en_yuksek:
# 		en_yuksek_sinif =  i
#
# print(en_yuksek)
# print(en_dusuk)
#
# print(f"En başarılı sınıf  {en_yuksek_sinif} ve ortalaması"
#       f" {sinif_ortalamalari.get( en_yuksek_sinif )}" )
# print(f"En başarısız sınıf  {en_dusuk_sinif} ve ortalaması "
#       f"{sinif_ortalamalari.get( en_dusuk_sinif )}" )

# Kendisine parametre olarak gönderilen sayının faktöriyelini hesaplayıp döndüren fonksiyonu yazınız.


# 5 sayı => 1*2*3*4*5=120
#
# def faktoryel_hesapla(sayi =1):
# 	carpim = 1
# 	if sayi == 0:
# 		sayi = 1
#
# 	for s in range(1,sayi+1):
# 		carpim *=s
# 	return  carpim
#
# sonuc = faktoryel_hesapla(10)
# print(sonuc)
#

### Bir fonksiyon içinde fonksiyon çağrılması
# Parametre olarak aldığı 2 sayıdan büyük olanı döndüren fonksiyon
# def buyuk(a,b):
# 	if a>b:
# 		return a
# 	elif a<b:
# 		return b
# 	else:
# 		return a
# # Parametre oalrak aldığı 3 sayıdan büyük olanı döndüren fonksiyon
# def buyuk2(a,b,c):
# 	return buyuk(a,buyuk(b,c))
#
# print(buyuk2(56,33,95))


### TEK SATIRDA FONKSİYON TANIMLAMA

#
# def kare(s):
# 	return s**2
#
# usalma = lambda taban,us: taban**us
#
# print(kare(2))
# print(usalma(2,2))
#
#
# topla =  lambda a,b: a+b
# print(topla(1,2))
#
#

# import Matematik #taviye edilmez çünkü Metematik içindeki tüm fonksiyonları içeri alır

# from Matematik import topla, cikar,carp,bol
#
#
# sonuc =  topla(2,5)
# print(sonuc)
#
# sonuc =  carp(2,5)
# print(sonuc)
#
# sonuc =  bol(3,0)
# print(sonuc)
#
# sonuc =  cikar(10,5)
# print(sonuc)


# Kendi isminiz ile bir modül oluşturunuz.
# Modül içerisnde bir sansur(cumlelistesi,yasaklıkelime,yenikelime) isminde bir metot oluşturun
# Bu metot kendisine gönderilen cümle listesindeki yasaklı kelimeyi yeni kelimeyle sansürlesin
# sansur("Çocuklar kahve içerse kararır.","kahve","*")

# from Sansur import sansur
#
# cumleler = list()
# yeni_liste = list()
# yasakli_kelimeler = ["kahve","Kahve","KAHVE", "Muz","muz", "MUZ"]
# for i in range(3):
# 	cumle = input("Cümle giriniz: ")
# 	cumle =  cumle.strip().upper()
# 	cumleler.append(cumle)
#
#
# for i in yasakli_kelimeler:
# 	yeni_liste = sansur( cumleler, i, "*" )
#
# print(yeni_liste)


"""
# Kullanıcıdan 2 tane değer alan DegerleriAl() fonk. vardır. eger bu degerleri sayi degerleri döndürür,
 herhangi biri sayı değilse False döndürür.
#
# -ObebHesapla(s1,s2) -> gelen bu iki sayının obeb degerlerini hesaplar ve geri döndürür.
# -OkekHesapla(obeb) -> s1*s2=obeb*okek formulunden okek bulunur ve okek obeb yazdırılır.
"""

#
# def degerleri_al( ):
# 	sayi1 = input( "Sayı 1: " )
# 	sayi2 = input( "Sayı 2: " )
#
# 	if sayi1.isdigit( ) and sayi2.isdigit( ):
# 		return int( sayi1 ), int( sayi2 )
# 	else:
# 		return False
#
# def obeb_hesapla( s1, s2 ):
# 	obeb = 1
# 	for i in range(2, min(s1,s2)+1):
# 		if s1 %i == 0 and s2%i ==0:
# 			obeb = i
#
# 	return obeb
#
#
# def okek_hesapla(obeb, s1,s2):
# 	okek = int(s1*s2/obeb)
# 	return  okek
#
#
#
# obeb =  obeb_hesapla(4,12)
# okek =  okek_hesapla(obeb,4,12)
#
# print("Obeb : ", obeb)
# print("Okek : ", okek)

####################  HAZIR STRING FONKSİYONLAR  ########################
"""
capitalize() İlk Karakteri büyük harfe çevir
count()     Bir dizide belirtilen değerin kaç defa tekrarlandığını verir
endswith()  Dizide belirtilen değer ile bitmiş mi True yada False verir
find()      Dizide belirli bir değeri kontrol eder ve yerini verir
isalpha()   Metnin tamamen karakterlerden oluşup oluşmadığını kontrol eder True - False değerleri verir
isdecimal() Metin içindeki değerlerin noktalı sayı olup olmadını döner True-False
isspace()  Metin tamamen boşluktan oluşuyor ise True-False

lstrip()     Dizenin sol boşlugu siler
rstriip()    Dizenin sağ boşlugu siler
strip()     Dizenin sağ ve sol boşlugu siler
split()      Dizeyi belirtilen ayrıcıya böler.
isalnum()    Dizedeki değerler Alfabe ve numara olması durumunda True döner
"""
#
# kelime =  " mehmet nuri "
# print(kelime.capitalize())
#
# listem = ["ahmet","mehmet","ahmet"]
# print(listem.count("ahmet"))
#
# print(kelime.endswith("mehmet"))
# print(kelime.find("nuri"))
# print(kelime.isalpha())
#
# maas =  "22.01"
# print(maas.isdecimal())
#
# kelime =  " "
# print(kelime.isspace())
#
# kelime =  " mehmet nuri "
#
# print(kelime.rstrip())
# print(kelime.lstrip())
# print(kelime.strip())
#
# kelime =  "ahmet mehmet ali"
# print(kelime.split(" "))
#
# kullanici_adi = "mehmet44"
# print(kullanici_adi.isalnum())
#
#
# # metin parçalama
# kelimeler ="Bugün.hava.çok.sıcak.değildi."
# print(kelimeler.split("."))
#
# print(kelimeler.split(".", 4))


########################## DATETIME KUTUPHANESİ ###################
import  datetime
from  datetime import datetime, date, timedelta
import locale
locale.setlocale(locale.LC_ALL,'Turkish_Turkey.1254')


zaman = datetime.now()

print(zaman)
print(zaman.day)
print(zaman.month)
print(zaman.year)
print(zaman.hour)
print(zaman.minute)
print(zaman.second)
print(zaman.microsecond)

zaman2 =  datetime(1993,11,20)
print(zaman2.date())
print(zaman2.year)

# Zaman formatlama
# print("zaman değişkeninin formatlı hali:",zaman.strftime("%d_%m_%Y"))

"""
%d  : rakam ile gün
%m  : rakam ile ay
%Y  : rakam ile 4 haneli yıl
%y  : rakam ile 2 haneli yıl
%b  : yazı ile 3 haneli ay
%H  : rakam ile saat
%M  : rakam ile dakika
%S  : rakam ile saniye
%a  : yazı ile 3 haneli gün
%A  : yazı ile tam gün adı
%D  : AY/GUN/YIL
"""

print(zaman.strftime("Bu gün günlerden : %A"))

zaman=datetime.now()
print(zaman.strftime("%b"))
print(zaman.strftime("%D"))

# YIL-AY-GUN--Saat:Dakika:Saniye--GünAdı

formatli_zaman = zaman.strftime("%Y-%m-%d--%H:%M:%S--%A")
print(formatli_zaman)

zList =  formatli_zaman.split("--")
# for z in zList:
# 	print(z)
print(zList[0])
print(zList[1])
print(zList[2])

zamanList = zList[1].split(":")
print(zamanList)

eski_zaman =  date.strftime(date(1993,11,20), '%Y-%m-%d')
bu_gun =  date.today()

print(bu_gun)
print(eski_zaman)

bir_hafta_once = bu_gun -timedelta(7)
print(bir_hafta_once)

print( bu_gun- eski_zaman)
