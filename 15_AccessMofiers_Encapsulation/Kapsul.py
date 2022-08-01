
############# KAPSULLEME (Encapsulation) #############

# getter methodlerı private özellikleri değerlerini okumamızı sağlar.
# readonly
# setter methodlar private özelliklere değer atamamızı sağlar

class Kapsul():
	
	def __init__(self):
		self.__gizli_ozellik = "Gizli Özellik 1 Değeri"
		self.__gizli_ozellik2 = "Gizli Özellik 2 Değeri"
		
	
	def get_gizli_ozellik( self ):
		return self.__gizli_ozellik
	
	def set_gizli_bilgi( self, value ):
		self.__gizli_ozellik = value