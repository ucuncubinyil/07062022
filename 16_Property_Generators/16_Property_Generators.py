#####################################################
#################### PROPERTY #######################
#####################################################

# class Personel:
#
# 	def __init__(self, parametre):
# 		self.__isim =  parametre
#
# 	def get_isim( self ):
# 		return  self.__isim
#
# 	def set_isim( self, parametre ):
# 		self.__isim =  parametre
#
# 	ad  = property(get_isim,set_isim)
#
#
# nesne =  Personel("Sevgi")
# print(nesne.ad)


## SORU: Vize ve final notunu alarak ortalama
# hesaplayan(Ortalama ()) univeriste isminde bir sınıf tanımlayınız.

# from Universite import Universite
#
#
# ogrenci =  Universite()
# ogrenci.vize = 101
# ogrenci.final = 90
#
# ogrenci.ortlama()

from  Musteri import Musteri

musteri =  Musteri()

musteri.ad = "Ali"
musteri.soyad = "Veli"
musteri.telefon = "6546546"
musteri.mail_adresi =  "asdasd@asdasd.com"

musteri.yazdir()

print(musteri.mail_adresi)








