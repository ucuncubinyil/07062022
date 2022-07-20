#### TRY CATCH - TRY EXCEPT ####

"""
try:
    #Hata kontrolü yapılacak kod bloğu
except:
    #Hata oluştu durumlarda çalıştırılacak kod bloğu
"""


# try:
# 	sayi1 = int( input( "Sayi gir:" ) )
# except:
# 	print("Sadece rakam girilmelidir")
#
# try:
# 	sayi1 = int( input( "Sayi gir:" ) )
# except ValueError:
# 	print("Sadece rakam girilmelidir")
# finally:
# 	print("Ben hata olsada olmasada çalışırım")

# while True:
# 	try:
# 		dosya =  open("C:\\TEST\\ty_except.txt", "a+") # /Users/kullaniciadi/ajhah.txt
# 		sayi =  int(input("Lütfen bir sayı giriniz:"))
# 		dosya.write(str(sayi))
# 		dosya.close()
# 		break
# 	except ValueError:
# 		print("Sadece rakam girilmelidir!!")
# 		continue
# 	except FileNotFoundError:
# 		print("Dosya Bulunamadı")
# 	except TypeError:
# 		print("Dosyaya sadece string basılmalıdır")
# 		continue
# 	except ZeroDivisionError:
# 		print("Hiç bir sayı sıfıra bölünemez")
# 	except OverflowError:
# 		print("Değişkenin kapasitesi aşıldı")
# 	except ImportError:
# 		print("Modül dahil edilemedi")
# 	except IndexError:
# 		print("Liste boyutu aşıldı")
# 	except:
# 		print("Yukardaki hatalar dışında bir hata oluştu")
# 	finally:
# 		dosya.close()
#
# while True:
# 	try:
# 		sayi1 = int( input( "Sayi1" ) )
# 		sayi2 = int( input( "Sayi2" ) )
# 		sonuc = sayi2 / sayi1
# 		print( sonuc )
# 		break
# 	except ValueError:
# 		print( "Sadece sayısal değerler girilebilir" )
# 		continue
# 	except ZeroDivisionError:
# 		print( "Hiç bir sayı sıfıra bölünemez" )
# 		continue
# 	except:
# 		print( "Bir hata oluştu" )

###### HATA FIRLATMA:TANIMLAMA raise() #######
# try:
# 	not1 = int( input( "Notunuzu giriniz: " ) )
# 	if not1 < 0 or not1 > 100:
# 		raise Exception # Manuel olarak hatayı tetikliyoruz
# except ValueError:
# 	print("Sadece rakam girilmeli")
# except Exception:
# 	print("Not 0-100 aralığında olmalıdır")
#

### ASSERT => iddaa edilen
#
# try:
# 	kontrol_eposta = "info@mehmetnuri.net"
# 	eposta = input( "Lütfen email adresinizi giriniz" )
# 	assert eposta == kontrol_eposta #eğer değerler birbirine eşit değil ise AssertionError patlatır
# except AssertionError:
# 	print( "Eposta eşleşmedi" )


####### ALIŞTIRMALAR #########
# Kullancıdan 2 sayı 1'de işlem alıp önceden tanımladığınız methodlara alınan değerleri göndereceğiz.
# işlem topla,çıkar,çarp ve böl'den birisi değilse assert fırlatsın,
# Kullanıcıdan veri alınırken ValueError verdiğinde tekrar veri istensin
# ZeroDivisionError için tekrar veri istenmesin!

def topla(s1,s2):
	return s1+s2

def cikar(s1,s2):
	return s1-s2

def bol(s1,s2):
	return s1/s2

def carp(s1,s2):
	return s1*s2


def islem_yap( ):
	s1 = int( input( "Sayi1" ) )
	s2 = int( input( "Sayi2" ) )
	islem = input( "Toplama(+), Çıkarma(-), Çarpma(*), Bölme(/)" )
	
	assert islem == "+" or islem == "-" or islem == "*" or islem == "/"
	
	if islem == "+":
		print(topla(s1,s2) )
	elif islem == "-":
		print( cikar(s1,s2) )
	elif islem == "*":
		print( carp(s1,s2) )
	elif islem == "/":
		print( bol(s1,s2))

while True:
	try:
		islem_yap( )
	except ValueError:
		print( "Sadece rakam girilmelidir" )
		continue
	except ZeroDivisionError:
		print( "Hiç bir sayı sıfıra bölünemez" )
		break
	except AssertionError:
		print("İşlem bulunamadı")
	except Exception:
		print( "Bir hata oluştu" )
		break
