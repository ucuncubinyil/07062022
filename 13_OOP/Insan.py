class Insan():
	ad = ""
	soyad = ""
	
	@classmethod
	def konus( cls, insan ):
		print(f" Ad: {insan.ad}  Soyad:{insan.soyad}")
		
	def konusma( self ):
		print( f" Ad: {self.ad}  Soyad:{self.soyad}" )
	
	@classmethod
	def  yazdir( cls, liste ):
		for i in liste:
			print(i.ad, i.soyad)
			
	@classmethod
	def kaydet( cls, liste ):
		a = Insan()
		a.ad =  input("Bebeğin Adı: ")
		a.soyad =  input("Bebeğin Soyadı: ")
		liste.append(a)