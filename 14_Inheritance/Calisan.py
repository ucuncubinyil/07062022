class Calisan():
	
	def __init__(self, ismi, maas, departman):
		self.ismi =  ismi
		self.maas = maas
		self.departman =  departman
		
	def  bilgi_goster( self ):
		print("Çalışan bilgileri")
		print(f"İsim: {self.ismi} Maas:{self.maas} Departman:{self.departman}")
	
	def  departman_degistir( self, yeni_departman ):
		print("Departman Değiştiriliyor")
		self.departman =  yeni_departman
		