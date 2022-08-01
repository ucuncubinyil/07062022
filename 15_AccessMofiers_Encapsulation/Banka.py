### Bir Banka müşteri kayıt sistemi oluşturulurken kayıt esnasında ad,soyad,tc(11 hane) ve
# Iban(TR+12) bilgileri alınıyor. Gerekl kontrolleri sağlayarak müşteri kayıt platformunu oluşturunuz.

class BankaKayit:
	
	def __init__(self):
		self.__tc = None
		self.__iban = None
		self.isim = input("İsim: ")
		self.soyisim =  input("Soyisim")
		self.__set_iban()
		self.__set_tc()
		
	
	
	def  get_iban( self ):
		return  self.__iban
	
	def __set_iban( self ):
		while True:
			IBAN = input("IBAN") #tr546546546
			ulke_kodu =  IBAN[0].upper()+IBAN[1].upper()
			
			if  ulke_kodu == "TR":
				iban = IBAN[2:]
				if len(iban) == 12 and iban.isnumeric():
					self.__iban =  ulke_kodu+iban
					break
				else:
					print("Lütfen iban bilginizi 12 haneli giriniz")
					continue
			else:
				print("Lütfen IBAN bilginizin başında TR ülke kodunu giriniz")
				continue
				
	def get_tc( self ):
		return  self.__tc
	
	def __set_tc( self ):
		
		while True:
			TC =  input("TC: ")
			if len(TC) == 11 and TC.isnumeric():
				self.__tc = TC
				break
			else:
				print("TC numaranız 11 haneli ve sadece rakamlardan oluşmalıdır")
				continue
	
	def yaz( self ):
		print(f"""
İsim            :{self.isim}
Soyisim         :{self.soyisim}
T.C.            :{self.__tc}
IBAN            :{self.__iban}
		""")
	
			
			
			
			
			
			
			
			
			
			
			