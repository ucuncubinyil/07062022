############ DİZİN İŞLEMLERİ #################
"""

system()  => Kullanırken çok dikkat edilmesi gereken bir metod
getcwd()  => Python programımızın hangi dizinde olduğunu gösterir ---- Win C:\ Linux macOsX /home/kullanıcı_adi
chdir()  => Dizin değiştirmemizi sağlar
listdir() => Bulunduğumuz dizindeki dizinleri(klasörleri) listeler
mkdir() => Klasör(Dizin) oluşturmak için kullanacağımız metot
rmdir() => Klasör(Dizin) silmek için kullanacağımız metot
rename() => İsim değiştirmek için kullandığımız metot
path()  => Bir dosya veya dizinin olup olmadığını kontrol eder.

"""

# from  os import chdir,getcwd,listdir,mkdir
#
# print(getcwd())
#
# chdir("C:\\")
# print(getcwd())
# print(listdir())
#
# mkdir(getcwd()+"TEST1")

########### ALIŞTIRMALAR ############
# SORU1: C:\TEST\YIL-AY-GUN ismi ile bir klasör oluşturunuz
# import os
# from datetime import *
# from os import *
#
# zaman =  date.today()
#
# klasor_adi =  zaman.strftime("%Y-%m-%d")
# dosya_yolu =  "C:\\TEST\\"+klasor_adi
#
# if not path.exists("C:\\TEST"):
# 	os.mkdir("C:\\TEST")
# 	print("C altında TEST klasörü oluşturuldu")
#
# if not path.exists(dosya_yolu):
# 	os.mkdir(dosya_yolu)
# 	print("C altında TEST klasörünün altında yil-ay-gun oluşturuldu")
#


#### DOSYA İŞLEMLERİ ####

"""
Dosya Yetki Modları
w:  sadece yazma yetkisi ile açar. (dosya var ise siler yeniden oluşturur.yoksa oluşturur.)
r:  sadece okuma yetkisi ile açar.
a:  sona ekleme yetkisi ile açar. (dosya yoksa oluşturur.)
x:  yazma yetkisi ile açar. (yoksa oluşturur. varsa hata verir.)

w+: yazma + okuma yetkisi ile açar. (dosya var ise siler yeniden oluşturur.yoksa oluşturur.)
r+  okuma + yazma yetkisi ile açar.
a+  ekleme + okuma yetkisi ile açar. (dosya yoksa oluşturur.)
"""

# from os import chdir,getcwd, path
#
# #Linux /home/kullaniciadi /...  osx /Users/kullaniciadi/...
# chdir( "C:\\TEST\\2022-07-06" )
# dosya_yolu = getcwd( ) + "\\dosyam.txt"  #C:\TEST\2022-07-06\dosyam.txt
#
# if not path.exists( dosya_yolu ):
# 	dosya = open( dosya_yolu, mode="a+" )
#
# dosya = open( dosya_yolu, mode="a+" )
# dosya.write( "Merhaba Python" )
# dosya.close()

# import os
# # os.system("calc")
# print(os.system("hostname"))
# print(os.system("ipconfig"))

### SORU: 1 - 10 sayıların karelerini kare.txt isimli bir dosyaya aşağıdaki formatla yazdırınız.

#
# from  os import mkdir,chdir, path
#
# dosya_yolu = "C:\\TEST\\"
#
# chdir("C:\\")
#
# if not path.exists( dosya_yolu ):
# 	mkdir( dosya_yolu )
#
# dosya_adres =  dosya_yolu +"kare.txt"
# dosya =  open(dosya_adres, mode="a+")
#
# print(type(dosya))
#
# for i in range(1,11):
# 	dosya.write(str(i)+ " sayısının karesi "+ str(i**2) + "\n")
#
# dosya.close()


# from os import  chdir,mkdir,path
#
# chdir("C:\\")
#
# dosya_yolu = "C:\\TEST\\"
# if not path.exists(dosya_yolu):
# 	mkdir(dosya_yolu)
#
# dosya_adres =  dosya_yolu+"kare.csv"
# dosya =  open(dosya_adres,mode="w")
# print(type(dosya))
#
# for i in range(1,11):
# 	dosya.write(f"{i} sayısının karesi {i**2} dir; ")
#
# dosya.close()
#


# SORU: 1-100 arası üretilen 10 adet sayıyı Rastgele.txt isimli
# bir dosyaya aşağıdaki formatta yazdıran program.

"""
    Zaman                   OlaySırası          RastgeleSayı
    20.01.2020 19:16:45         1                       98
    20.01.2020 19:16:46         2                       15
    20.01.2020 19:16:47         3                       45
    20.01.2020 19:16:48         4                       87
"""
#
# from os import  chdir,mkdir,path
# from  datetime import datetime
# from random import randint
#
# dosya_yolu = "C:\\TEST\\"
#
# if not path.exists(dosya_yolu):
# 	mkdir(dosya_yolu)
#
# dosya_adresi = dosya_yolu+"Rastgele.txt"
#
# if not path.exists(dosya_adresi):
# 	dosya =  open(dosya_adresi, mode="a+")
# 	dosya.write( """
# 	    Zaman                       OlaySırası              RastgeleSayı
# 	    -----                       ----------              ------------
# 	""")
# 	dosya.close()
#
# dosya = open(dosya_adresi, mode="a+")
#
# for i in range(1,11):
# 	rastgele_sayi =  randint(1,100)
# 	zaman = datetime.now()
# 	dosya.write( """
# """ + str( zaman ) + "               " + str( i ) + "             " + str( rastgele_sayi ) + """
# 	  """
# 	             )
#
# dosya.close()




# SORU: Kullanıcının girdiği küçük sayıdan büyük sayıya kadar olan sayıları txt dosyasında alt alta yazınız.

from os import chdir, mkdir, path

# klasor = "C:\\TEST\\"
#
# if not path.exists(klasor):
# 	mkdir(klasor)
#
# kucuk =  int(input("Lütfen küçük sayıyı giriniz: "))
# buyuk =  int(input("Lütfen büyük sayıyı giriniz: "))
#
# if kucuk > buyuk:
# 	kucuk,buyuk = buyuk,kucuk
# elif buyuk > kucuk:
# 	pass
# else:
# 	print("Değerler eşit olamaz")
#
# dosya_yolu =  klasor+"sayi_listesi.txt"
#
# dosya =open(dosya_yolu,mode="a+")
#
# for i in range(kucuk, buyuk+1):
# 	dosya.write(f"{i}\n")
# dosya.close()


### DOSYA OKUMA İŞLEMLERİ ###
# dosya_adresi =  "C:\\TEST\\kare.txt"
#
# dosya =  open(dosya_adresi, mode="r", encoding="utf8")
#
# temiz_liste =  list()
#
# # for i in dosya.readlines():
# # 	temiz_liste.append(i.rstrip("\n").rstrip(" ").lstrip(" "))
#
# for i in dosya.readlines():
# 	i.strip()
# 	temiz_liste.append(i.replace("\n",""))
#
# print(temiz_liste)
#

##SORU:sayıListesi.txt isimli bir dosya oluşturunuz içinde
# çift ve tek sayılar karışık olacak şekilde 10 sayı ekleyiniz.

# dosya_adresi =  "C:\\TEST\\sayıListesi.txt"
# dosya =  open(dosya_adresi, "w")
#
# for i in range(10):
# 	sayi =  input("Sayı girin: ")
# 	if sayi.isdigit():
# 		dosya.write(sayi +"\n")
#
# dosya.close()
##SORU: sinif.txt'de kayıtlı olan puan ad soyad
# bu sınıfın ortalamasını,en yüksek ve en düşük puanını ekrana yazdıran methodu kodlayınız.


# def oku():
# 	yeni_liste =  list()
# 	dosya =  open("C:\\TEST\\sinif.txt", mode="r", encoding="utf8")
# 	liste =  dosya.readlines()
# 	dosya.close()
# 	print(liste)
#
# 	for i in liste:
# 		dd =  i.split(" ")
# 		print(dd)
# 		yeni_liste.append(int(dd[0]))
#
# 	OrtalamaPuan =  sum(yeni_liste) /len(yeni_liste)
# 	MinPuan =  min(yeni_liste)
# 	MaxPuan =  max(yeni_liste)
#
# 	print(OrtalamaPuan)
# 	print(MinPuan)
# 	print(MaxPuan)
#
# oku()


## Kullanıcıdan personel sayı bilgisini al: Her personel için;
    # Ad,Soyad,DogumYılı bilgilerini alarak PersonelKayitlari.txt dosyasına yazdırınız.
    
personel_sayisi =  int(input("Personel sayısı:"))

dosya = open("C:\\TEST\\PersonelKayitlari.txt", mode="w", encoding="utf8")

for i in range(personel_sayisi):
	ad = input("Personel Ad")
	soyad = input("Personel Soyad")
	dogum_yili = input("Personel Doğum Yılı")
	dosya.write(ad+"\t\t"+soyad+"\t\t"+dogum_yili+"\n")
	
dosya.close()