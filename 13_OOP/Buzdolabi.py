class Buzdolabi():
	
	# CONSTRUCTOR METHOD
	"""
	Kurucu method: class'tan instance alındığında otomatik olarak çalışan bir methoddur.
	__init__ ismiyle tanımlanır.
	Eğer kurucu metodu tanımlamazsak görünmez olrak default da def __init__(self): şeklinde kendisi otomatik tanımlar.
	"""
	
	"""
	def __int__(self):
		pass
	"""
	
	def __init__(self):
		self.marka =  ""
		self.model = ""
		self.fiyat=0
		
	def  bilgi_ver( self ):
		print(self.marka, self.model)
	
	# static metotları hem class hem de nesne üzerinden direk kullanabilirsiniz.
	@staticmethod
	def  fiyat_hesapla(fiyat,faizorani):
		print(fiyat * (faizorani*0.25))