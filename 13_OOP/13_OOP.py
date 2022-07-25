###################################################################
############### OOP: Object Oriented Programming ##################
################ Nesneli Yöneliklik Programlama ###################
###################################################################

'''
OOP: büyük projeler yazılacağı zamanlarda, proje temelini oluşturma aşamasından
başlayarak analiz sentez kodlama sınama ve onarım gibi yaşam döngüsü adımlarında daimi olarak
uyugulanması ve takip edilmesi gerekli bir yapıdır.
En büyük kazancı proje temelini oluşturan yapıların bir bütün halinde(object)
tutulması ve yapınların özelliklerinin(field) alt başlıklar halinde yapıya özel olmasını sağlar.
Kayıt güncelleme,silme veya okuma işlemlerinde object (nesne) sayesinde veri bütünlüğü sağlanmış
ve tek bir işlemle manipüle edeilmiş olur.
'''

## Bir okulunuz oolduğunu ve öğrenci kaydı yapılacağını düşünelim.
# Her öğrencinin ad,soyad,tc,dogumtarihi gibi bilgileri kayıt edilecektir.
"""
ad = "Mehmet Nuri"
soyad =  "Öztürk"
tc = 246545
dogum_tarihi =  "20.11.1993"


ad = "Ferdi"
soyad =  "Arslandaş"
tc = 654646541635
dogum_tarihi =  "21.09.1974"


ad = "Deniz"
soyad =  "Drahyalı"
tc = 87987989
dogum_tarihi =  "11.03.1989"
"""
#
# class Ogrenci:
# 	ad = str() # ""
# 	soyad =  str()
# 	tc = 0
# 	dogum_tarihi = str()
#
# 	# self=> nesneyi temsil ediyor ve bu methodun nesne üzerinden kullanılabileceğini gösteriyor.
# 	def bilgi_yaz( self ):
# 		print(f"Ad: {self.ad} Soyad: {self.soyad}, TC: {self.tc}, Doğum Tarihi: {self.dogum_tarihi}")
#
# 	@classmethod # cls => cls ifadesi Class üzerinden çağrılabileceğini belirtir.
# 	def  ara( cls, ad, liste ):
# 		for i in liste:
# 			if i.ad == ad:
# 				print(f"Ad: {i.ad} Soyad: {i.soyad}, TC: {i.tc}, Doğum Tarihi: {i.dogum_tarihi}")
#
#
#

# from  Ogrenci import Ogrenci
#
# ogrenci_listesi =  list()
#
#
# # Instance: Bir classtan örneklem almaya denir. Alınan örnek(object) class'taki tanımlı olan özelliklere sahip olacaktır.
# mehmet = Ogrenci()
# mehmet.ad = "Mehmet Nuri"
# mehmet.soyad =  "ÖZTÜRK"
# mehmet.dogum_tarihi= "20.11.1993"
# mehmet.tc = 654654654
# # mehmet.bilgi_yaz()
#
#
# ferdi =  Ogrenci()
# ferdi.ad = "Ferdi"
# ferdi.soyad = "ARSLANDAŞ"
# ferdi.tc = 8798798
# ferdi.dogum_tarihi = "21.09.1974"
# # ferdi.bilgi_yaz()
#
# ogrenci_listesi.append(mehmet)
# ogrenci_listesi.append(ferdi)
#
# Ogrenci.ara("Ferdi", ogrenci_listesi)







#
# a = Insan()
# a.ad =  input("Bebeğin Adı: ")
# a.soyad =  input("Bebeğin Soyadı: ")
# bebek_listesi.append(a)
#
#
# Insan.yazdir(bebek_listesi)
# from Insan import Insan
# bebek_listesi =  list()
# while True:
# 	a = Insan()
# 	a.ad =  input("Bebeğin Adı: ")
# 	a.soyad =  input("Bebeğin Soyadı: ")
# 	a.konusma()
# 	bebek_listesi.append(a)
# 	cevap =  input("Devam etmek istiyor musunuz ? ").upper()
# 	if cevap == "E":
# 		continue
# 	else:
# 		break
# Insan.yazdir(bebek_listesi)
# Insan.kaydet(bebek_listesi)
# Insan.yazdir(bebek_listesi)

# from Buzdolabi import Buzdolabi
#
#
# arcelik =  Buzdolabi()
# arcelik.marka ="BABA"
# print(arcelik.marka)
#
# arcelik.fiyat =  100
# arcelik.fiyat_hesapla(arcelik.fiyat, 24)
#
# Buzdolabi.fiyat_hesapla(arcelik.fiyat,24)



# from Matematik import Matematik
#
# toplama_sonucu =  Matematik.topla(1,2,3,4,5,6,7,8,9,10)
# print(toplama_sonucu)
#
# cikarma_sonucu =  Matematik.cikar(10,5)
# print(cikarma_sonucu)
#
# carpma_sonucu =  Matematik.carp(1,2,3,4,5,6,7,8,9,10)
# print(carpma_sonucu)
#
# bolme_sonucu =  Matematik.bol(1,5)
# print(bolme_sonucu)


#
# from Ders import Ders
#
# python =  Ders()
# python.ders_kaydet()

from Personel import Personel

while True:
	secim =  input("""
	1- Personel kayıt işlemi
	2- Personel listeleme işlemi
	3- Çıkış
	""")
	
	try:
		if secim.isdigit( ):
			if int(secim) == 1:
				personel =  Personel()
				personel.personel_kaydet()
				cevap = input("Devam etmek ister misiniz(E/H) ?").upper()
				if cevap == "E":
					continue
				else:
					break
			elif int(secim) == 2:
				Personel.listele()
				cevap = input( "Devam etmek ister misiniz(E/H) ?" ).upper( )
				if cevap == "E":
					continue
				else:
					break
			elif int(secim) == 3:
				break
			else:
				print("Hatalı seçim")
				continue
			
		else:
			raise RuntimeError( "Seçimi sadece sayısal yapabilirsiniz !!!" )
	except RuntimeError:
		print("Seçimi sadece sayısal yapabilirsiniz !!!")










