from Arac import Arac

class Kamyon(Arac):
	
	def __init__(self):
		super().__init__()
		self.tasima_kapasitesi =  0
		self.yakit_deposu_sayisi = 0
	
	def bilgi_yaz( self ):
		super().bilgi_yaz()
		print( f"""
Taşıma Kapasitesi           :{self.tasima_kapasitesi}
Yakıt Deposu Sayısı         :{self.yakit_deposu_sayisi}""")