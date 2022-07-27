from BeyazEsya import BeyazEsya
import os

class BuzDolabi(BeyazEsya):
	def __init__(self):
		super().__init__()
		self.kapak_sayisi = 1
		self.hacim = 0
	
	def  kaydet( self ):
		dizin =  "C:\\DERS14\\"
		dosya = dizin + "Buzdolabi.txt"
		
		if  not os.path.exists(dizin):
			os.mkdir(dizin)
			
		if not os.path.exists(dosya):
			dosya = open(dosya, mode="a+", encoding="utf-8")
			data =  f"""
Marka                   :{self.marka}
Model                   :{self.model}
Renk                    :{self.renk}
Fiyat                   :{self.fiyat}
Enerji Sınıfı           :{self.enerji_sinifi}
Kapak Sayısı            :{self.kapak_sayisi}
Hacim                   :{self.hacim}"""
			dosya.write(data)
			dosya.close()
		else:
			dosya = open( dosya, mode="a+", encoding="utf-8" )
			data = f"""
Marka                   :{self.marka}
Model                   :{self.model}
Renk                    :{self.renk}
Fiyat                   :{self.fiyat}
Enerji Sınıfı           :{self.enerji_sinifi}
Kapak Sayısı            :{self.kapak_sayisi}
Hacim                   :{self.hacim}"""
			dosya.write( data )
			dosya.close( )
		