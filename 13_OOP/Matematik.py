class Matematik():
	
	@classmethod
	def topla( cls, *sayilar ):
		toplam = 0
		for i in sayilar:
			toplam += i
		return toplam
	
	@classmethod
	def cikar( cls,s1,s2 ):
		return  s2-s1
	
	@classmethod
	def carp( cls,*sayilar ):
		carpim = 1
		for i in sayilar:
			try:
				if i == 0:
					raise RuntimeError( "Sayı sıfır olamaz" )
				carpim *= i
			except RuntimeError:
				print("Sayı sıfır olamaz")
		
		return carpim
	
	@classmethod
	def bol( cls, s1,s2 ):
		sonuc = 0
		try:
			sonuc =  s1/s2
			
		except ZeroDivisionError:
			print("Hiç bir sayı sıfıra bölünemez")
		return sonuc
