class Uye:
	isim =  str()
	soyisim =  str()
	__tc = ""
	
	def kaydet( self ):
		self.isim =  input("İsim: ")
		self.soyisim =  input("Soyisim: ")
		TC = input("T.C. : ")
		
		if (len(TC) == 11 and TC.isnumeric()):
			self.__tc = TC
		else:
			self.__tc = 00000000000
	
	def yaz( self ):
		print(f"İsim: {self.isim} Soyisim: {self.soyisim} T.C. : {self.__tc}")