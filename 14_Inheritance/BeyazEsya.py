class BeyazEsya:
	
	def __init__( self ):
		self.marka = ""
		self.model = ""
		self.renk = ""
		self.fiyat = 0.0
		self.enerji_sinifi = ""
	
	def  bilgi_yaz( self ):
		print(f"""
Marka                   :{self.marka}
Model                   :{self.model}
Renk                    :{self.renk}
Fiyat                   :{self.fiyat}
Enerji Sınıfı           :{self.enerji_sinifi}
		""")
