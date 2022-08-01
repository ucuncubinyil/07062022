class Musteri():
	
	def __init__(self):
		self.__ad = None
		self.__soyad = None
		self.__telefon =  None
		self.__mail_adresi =  None
		
	
	@property
	def ad( self ):
		return self.__ad
	
	@ad.setter
	def ad( self, parametre ):
		self.__ad =  parametre
	
	@property
	def  soyad( self ):
		return  self.__soyad
	
	@soyad.setter
	def  soyad( self, parametre ):
		self.__soyad = parametre
		
	@property
	def telefon( self ):
		return  self.__telefon
	
	@telefon.setter
	def telefon( self, parametre ):
		self.__telefon = parametre
	
	@property
	def mail_adresi( self ):
		return self.__mail_adresi
	
	@mail_adresi.setter
	def mail_adresi( self, parametre ):
		self.__mail_adresi = parametre
		
	
	def yazdir( self ):
		print(f"""
AD          :{self.__ad}
SOYAD       :{self.__soyad}
MAIL        :{self.__mail_adresi}
GSM         :{self.__telefon}
		""")
	
	