from Calisan import Calisan

class Yonetici(Calisan):
	
	def __init__(self, isim, maas, departman, kisi_sayisi):
		super().__init__(isim,maas,departman) # Super base class ı temsil eder
		self.kisi_sayisi = kisi_sayisi
		
	def bilgi_goster( self ):
		print( "Çalışan bilgileri" )
		print( f"İsim: {self.ismi} Maas:{self.maas}"
		       f" Departman:{self.departman}"
		       f" Kişi Sayısı:{self.kisi_sayisi}" )
		
	
	def  zam_yap( self, zam_miktari ):
		print("Yöneticiye Zam Yapılıyor....")
		self.maas += zam_miktari
		
	
	def  departman_degistir( self, yeni_departman ):
		super().departman_degistir(yeni_departman)
		
