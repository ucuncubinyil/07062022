from Base import Base

# CRUD (Create Read Update Delete - >
# Oluştur Oku Güncelle Sil)
class Product(Base):
	
	def __init__(self):
		self.price =  0.0
		self.stock = 0
	
	def save( self ):
		print(self.id)
		print(self.name)
		print(self.price)
		print(self.stock)
	
	def update( self ):
		pass
	
	def remove( self ):
		pass
	
	def list_all( self ):
		pass
		
	