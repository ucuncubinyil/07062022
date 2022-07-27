from BeyazEsya import BeyazEsya

class CamasirMakinesi(BeyazEsya):
	
	def __init__(self):
		super().__init__()
		self.yikama_kapasitesi =  0
		self.hizli_yikama = False
	
	def bilgi_yaz( self ):
		
		super().bilgi_yaz()
		hizli =  ""
		
		if self.hizli_yikama == True:
			hizli = "VAR"
		else:
			hizli = "YOK"
			
			print( f"""
Yıkama Kapasitesi              :{self.yikama_kapasitesi}
Hızlı Yıkama                   :{hizli}""")
