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

kadi = "mehmetnuri"
ksifre = "123456"
kemail = "info@mehmetnuri.net"

print( "-----------------KULLANICI GİRİŞİ-----------------" )

username = input( "Kullanıcı/Email Adınız:" )
password = input( "Şifreniz: " )

if ((username == kadi or username == kemail) and ksifre == password):
    print( "Giriş Başarılı !" )
else:
    cevap = input( "Girdiğiniz bilgiler yanlış. Kayıt olmak ister misiniz?(E/H)" ).upper( )

    if cevap == "E":
        kullanici_adi = input( "Kullanıcı Adınız :" )
        email = input( "Email adresiniz" )
        sifre1 = input( "Şifreniz" )
        sifre2 = input( "Şifreniz Tekrar" )
        
        if sifre1 == sifre2:
            print( "Hoş geldiniz" )
        else:
            print( "Girilen şifreler birbirini tutmuyor" )
    elif cevap == "H":
        print( "Peki" )
    else:
        print( "Hatalı Seçim" )
