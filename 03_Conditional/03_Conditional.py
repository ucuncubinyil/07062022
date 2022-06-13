##################### AKIŞ KONTROL : IF ELIF ELSE ########################################


# sayi = 6
#
# if (sayi > 6):
#     print( "Sayi 6 dan büyük" )
#     print(6*2)
#
# elif (sayi == 6):
#     print( "Sayi 6 ya eşit" )
#
# else:
#     print( "Sayı 6 dan büyük değildir" )


# Haftanın kaçıncı günüdeyiz? ekrana gün adını yazdıralım
#
# gun = int( input( "Haftanın gün sayısını girin: " ) )
#
# if gun == 1:
#     print( "Pazartesi" )
# elif gun == 2:
#     print( "Salı" )
# elif gun == 3:
#     print( "Çarşamba" )
# elif gun == 4:
#     print( "Perşembe" )
# elif gun == 5:
#     print( "Cuma" )
# elif gun == 6 or gun == 7:
#     print("Haftasonu")
# else:
#     print("Hatalı giriş")

# SORU: Klavyeden girilen değer: 100'den büyükse karesini,
# küçükse küpünü ekrana yazdıran prog.

# sayi = int( input( "Sayıyı gir:" ) )
#
# if sayi > 100:
#     print( sayi ** 2 )
# elif sayi < 100:
#     print( sayi ** 3 )
# else:
#     print("Sayı 100 e eşittir")

## MOD ALMA

# sayi = 5
#
# print(sayi%2)

# Klavyeden girilen sayı çift ise:
# Ekrana sayı çifttir yazılacak,
# değilse tektir yazılacak
# çift ise 4 ile çarpsın, tek ise 9 ile toplasın

# sayi = int( input( "Sayıyı girin:" ) )
#
# if sayi % 2 == 0:
#     print("Sayı çifttir")
#     print(sayi*4)
# else:
#     print("Sayı tektir")
#     print(sayi+9)


# Kullanıcıdan alınan sayının aralığını belirleyiniz

# sayi = int( input( "Sayıyı girin:" ) )
# if sayi > 0 and sayi < 11:
#     print( "Sayı 0-10 aralığınadır" )
# elif sayi > 10 and sayi < 21:
#     print( "Sayı 10-20 aralığındadır" )


# Klavyeden girilen 4 sayıdan tek ve çift olanları ayrı
# ayrı toplayarak ekrana yazdırınız..

# cift_toplam = 0
# tek_toplam =  0
#
# s1 = int(input("Birinci Sayi:")) # 4
# if s1 %2 == 0:
#     cift_toplam += s1 # cifttoplam=cifttoplam+s1 => ciftoplam=4
# else:
#     tek_toplam += s1
#
# s2 = int(input("İkinci Sayi:"))
# if s2 % 2 ==0:  # 12
#     cift_toplam += s2 #cifttoplam= 4 + 12 => 16
# else:
#     tek_toplam += s2
#
# s3 = int(input("Üçüncü Sayi:"))
# if s3 % 2 == 0:
#     cift_toplam += s3
# else:
#     tek_toplam += s3
#
# s4 = int(input("Dördüncü Sayı:"))
# if s4 %2==0:
#     cift_toplam += s4
# else:
#     tek_toplam += s4
#
#
# print(f"Teklerin toplamı: {tek_toplam}")
# print(f"Çiftlerin toplamı: {cift_toplam}")


## Kullanıcıdan vize final not girilmesi istensin not aralığı 0 ile 100 arasında olmalıdır.
## vize ve finalin ortalaması alınsın.
## 0-44 : Kaldınız
## 45-69: Geçtiniz
## 70-84: İyi
## 85-100: Pekiyi

# vize = float( input( "Vize:" ) )
# final = float( input( "Final:" ) )
#
# if (vize <= 100 and vize >= 0) and (final <= 100 and final >= 0):
#     ortalama = (vize + final) / 2
#     if ortalama >= 0 and ortalama < 45:
#         print( "Kaldınız" )
#     elif ortalama >= 45 and ortalama < 70:
#         print( "Geçtiniz" )
#     elif ortalama >= 70 and ortalama < 85:
#         print( "İyi" )
#     else:
#         print( "Pekiyi" )
#
#     print( ortalama )
# else:
#     print( "Girilen notlar 0-100 aralığında olmalıdır" )


# Kullanıcıdan isim,yaş,maaşve çocuk sayısı alalım

"""
    Eğer kullanıcının yaşı 45'in altındaysa;
        çocuk sayısına bakılacak ve çocuk sayısı 3^ten az ise çocuk başına 250₺,
         değilse çocuk başına 200₺ maaşa eklenecek
    Eğer kullanıcının yaşı 45 ve üzerinde ise:
        çocuk başına para verilmeyecek direk 500₺ maaşa eklenecek.

    Ekrana "Nesrin Yılmaz Maaşınız: 4000₺" yazılacak.
"""

# isim = input( "İsminiz: " )
# yas = int( input( "Yaşınız: " ) )
# maas = int( input( "Maaş: " ) )
# cocuk_sayisi = int( input( "Çocuk sayısı: " ) )
#
# if yas < 45 and yas > 18:
#     if cocuk_sayisi < 3 and cocuk_sayisi >= 0:
#         maas += cocuk_sayisi * 250
#     else:
#         maas += cocuk_sayisi * 200
# elif yas >= 45:
#     maas += 500
#
# else:
#     print( "Belirlenen yaş aralığında değilsiniz !" )
#
# print( f"{isim} Maaşınız:{maas} ₺" )


# ÖDEV: Kullanıcı Gİriş Paneli Tasarlayınız.
"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz? 
                Hayır ise PEKİ!!! 
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması 
"""


# Email ve parola bilgileri ile giriş kontrolü yapınız.

# email =  "info@mehmetnuri.net"
# parola = "123456"
#
# girilen_email = input("Lütfen e-mail adresinizi giriniz:")
# girilen_parola =  input("Lütfen parolanızı giriniz: ")
#
# if  girilen_email == email and girilen_parola == parola:
#     print("Giriş başarılı")
# else:
#     print("Lütfen bilgilerinizi kontrol ediniz !!!")


# Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.

a =  int(input("a sayısı:"))
b =  int(input("b sayısı:"))
c =  int(input("c sayısı:"))

if (a>b) and (a>c):
    print(f"En büyük değer a dır ve değeri {a}")
elif (b>a) and (b>c):
    print(f"En büyük değer b dir ve değeri {b}")
else:
    print(f"En büyük değer c dir ve değeri {c}")

