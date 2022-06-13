################ WHILE ##################

# 1 ile 10 arasındaki sayıları ekrana yazdırınız.
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

"""
while(kosul):
    kosul true olduğu sürece bu kod bloğu çalışır.
# """
#
# i = 1
# while i <= 10:
#     print( i )
#     i += 1
#
# while i <= 11:
#     i += 2
#     print( i )
#     if i == 5:
#         break  # Döngüyü kırar(sonlandırır)
#
# while True:  # Sonsoz döngü oluşturur
#     print( "Mehmet" )
#     break
#
# # 90 ile 100 arasındaki  tek sayıları ekrana yazdırınız.
#
# sayi = 90
# while sayi <= 100:
#
#     if sayi % 2 == 1:
#         print( sayi )
#
#     sayi += 1

# 70 ile 55 arasındaki sayılarda 3'e tam bölünenleri
# ekrana yazdırınız

# sayi = 70
# while sayi > 55:
#
#     if sayi % 3 == 0:
#         print( sayi )
#
#     sayi -= 1

# SORU: 7 - 77 arasındaki tüm sayıların toplamını ekrana yazdırınız.

# sayi = 7
# toplam = 0
#
# while sayi <= 77:
#     toplam += sayi
#     sayi += 1
# print( f"7 den 77 ye kadar olan sayıların toplamı {toplam}" )

# SORU: 1'den kullanıcının girdiği sayıya kadar olan
# sayıların karesini ekrana yazdıran program.
# sayi = 1
# bitis = int( input( "Bitiş sayısı girin" ) )
# while sayi <= bitis:
#     print( sayi ** 2 )
#     sayi += 1

# CONTINUE: Run time da continue keyword'ü
# çalışırsa program bulunduğu yerden döngüye geri döner
# sayi = 1
# while sayi < 10:
#     if sayi == 2:
#         continue
#     if sayi == 5:
#         break
#     print( sayi )
#     sayi += 1

# SORU: Klavyeden girilen deger 'çık' ise döngüden çıkılacak.
# değilse toplama işlemi gerçekleştirilecek.
#
# toplam = 0
# while True:
#     girdi =input("Sayı girmek için sayıyı girin veya çıkmak için ÇIK YAZIN ").upper()
#     if girdi == "ÇIK":
#         break
#     elif girdi.isdigit():
#         sayi =  int(girdi)
#         toplam += sayi
#         continue
#     else:
#         print("Hatalı giriş")
#         continue
# print("Toplam", toplam)


#SORU: 1-100 arasındaki sayıların toplayan program.
# Ancak aşağıdak durumlarda sayıyı toplama eklemeyecek
# * Sayı 7'nin katı ise toplama eklenmesin
# * Sayı'nın 3 katının 7 fazlası 37'nın katı ise döngüden çıkılsın.
#
# sayi = 1
# toplam = 0
# while sayi <=100:
#     if sayi % 7 == 0:
#         sayi +=1
#         continue
#     kat = 3*sayi+7
#     if kat % 37 == 0:
#         print("Kat: ", kat)
#         print(sayi)
#         break
#     toplam += sayi
#     sayi += 1
#
# print("Toplam", toplam)


# SORU: Klavyeden girilen sayının faktöriyelini hesaplayan program
# Faktoriyel => 5 => 1*2*3*4*5=120
# sayi =  int(input("Faktöryeli hesaplanacak sayıyı giriniz: "))
# sonuc = 1
# sayac = 1
#
# while sayac <= sayi:
#     sonuc *= sayac #sonuc =  sayac*sonuc
#     sayac += 1
#     print(sonuc)
#
# print(f"{sayi} sayısının faktöryeli  {sonuc}")


#SORU:
"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak. 3 defa giriş hakkı vardır.
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz? 
                Hayır ise PEKİ!!! 
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı 
                alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması 
"""

kmail =  "info@mehmetnuri.net"
kadi = "mehmetnuri"
ksifre = "123456"

while True:
    print("########## KULLANICI GİRİŞİ ##########")
    username = input("Kullanıcı adınızı veya email adresinizi giriniz: ")
    password = input("Şifrenizi giriniz: ")

    if (kmail == username or  kadi == username) and ksifre == password:
        print("Giriş Başarılı")
        break
    else:
        cvp =  input("Kullanıcı Bulunamadı. Kayıt olmak ister misiniz (E/H)").upper()

        if cvp == "E":
            kullanici_adi =  input("Kullanıcı Adınız: ")
            kullanici_email = input("Email adresiniz: ")

            while True:
                sifre1 = input("Şifreniz")
                sifre2 = input("Şifreniz(Tekrar)")

                if sifre1 == sifre2:
                    print("Kayıt Başarılı")
                    break
                else:
                    print("Şifreler birbirini tutmuyor")
                    continue
            break
        elif cvp == "H":
            print("Peki...")
            break




















