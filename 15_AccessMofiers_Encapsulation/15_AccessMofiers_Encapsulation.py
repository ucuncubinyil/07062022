## ACCESS MODIFIER: public,private,protected

#public: Yazılım dillerinde genel erişime açık anlamına gelir.
# Herhangi bir erişim belirteci verilemezse default olarak hem
# class hem field'lar public tanımlanmış olur.
#
# class Muhendis:
# 	ad = "Mehmet Nuri"
# 	soyad = "Öztürk"
#
# 	def  ekrana_yaz( self ):
# 		print(self.ad)
# 		print(self.soyad)
#
#
# muhendis = Muhendis()
# muhendis.ad  = "Ali"
# muhendis.soyad = "Kaçan"
#
# muhendis.ekrana_yaz()

# private: Yazılım dillerinde SADECE TANIMLANDIĞI CLASS içerisinde
# erişilebilir anlamına gelir. '__' iki adet alt çizgi ile belirtilir.
# from Muhendis import Muhendis
#
# muhendis = Muhendis()
# print(muhendis.ad)
# # print(muhendis.__soyad)# Hata verir
# muhendis.ekrana_yaz()

# from Uye import Uye
#
# ahmet =  Uye()
# ahmet.kaydet()
# ahmet.yaz()




#protected: Sınıf içinde public ama sınıf dışında sadece miras
# alınan(inheritance) classlarda erişilebilir. '_' tek alt çizgi ile tanımlanır.

# from Calisan import Calisan
#
# ahmet = Calisan()
#
# ahmet._ekranayaz()
#

#
# from  Kapsul import Kapsul
#
#
# kap =  Kapsul()
# kap.set_gizli_bilgi("Handan")
# print(kap.get_gizli_ozellik())
# # kap.__gizli_ozellik2() #encapsule işlemi yapılmadığından hata verir


from Banka import BankaKayit


ahmetin_hesabi = BankaKayit()

ahmetin_hesabi.yaz()






