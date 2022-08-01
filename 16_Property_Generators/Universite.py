class Universite():
	
	def __init__(self):
		self.__vize = 0
		self.__final = 0
		
	def get_vize( self ):
		return  self.__vize
	
	def set_vize( self, parametre ):
		
		if ( parametre <0  or parametre >100 ):
			
			while True:
				print("Hatalı vize girişi !!! Vize notu 0-100 aralığında girilmelidir")
				vizenot = input("Vize Notu: ")
				if int(vizenot) < 0  or int(vizenot) >100:
					continue
				else:
					self.__vize = int(vizenot)
					break
		else:
			self.__vize =  parametre
			
	vize  = property(get_vize, set_vize)
	
	
	@property
	def final( self ):
		return self.__final
	
	@final.setter
	def final( self, parametre ):
		if (parametre < 0 or parametre > 100):
			
			while True:
				print( "Hatalı final girişi !!! Final notu 0-100 aralığında girilmelidir" )
				final_not = input( "Final Notu: " )
				if int( final_not ) < 0 or int( final_not ) > 100:
					continue
				else:
					self.__final = int(final_not)
					break
		else:
			self.__final = parametre
			
	
	def ortlama( self ):
		
		print(f"Ders Ortalaması  {   (self.__vize*0.4) +(self.__final*0.6)    }")