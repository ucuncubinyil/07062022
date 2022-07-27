from Arac import Arac

class Otomobil(Arac):
	
	def __init__(self):
		super().__init__()
		self.kasa_tipi = str()
		self.vites_tipi =  str()
		
	
	def bilgi_yaz( self ):
		super().bilgi_yaz()
		print( f"""
Kasa Tipi           :{self.kasa_tipi}
Vites Tipi          :{self.vites_tipi}""")
