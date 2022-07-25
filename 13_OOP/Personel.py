# SORU:
"""
Personel isimli bir class tanımlayın
Nesne Nitelikleri: ad,soyad,tc,telefon,adres,maas
__init__ fonksiyonu ile kullanıcıdan bu özellikler sorularak doldurulsun

Kaydet() isimli method Personel.txt adında bir dosyaya kaydetsin
Bir tane sınıf üzerinden erişebilir Listele() adında bir method tanılayın dosyadaki verileri okuma işlemi gerçekleştirsin

"""
import os
class Personel():
	
	def __init__(self):
		self.ad = input("Personel Ad: ")
		self.soyad =  input("Personel Soyad: ")
		self.tc =  input("Personel T.C.: ")
		self.telefon = int(input("Personel Telefon: "))
		self.adres =  input("Personel Adresi: ")
		self.maas =  float(input("Personel Maaş: "))
		
	def personel_kaydet( self ):
		
		try:
			dizin =  "C:\\TEST\\"
			kayitli_dosya =  dizin+ "Personel.txt"
			
			if not os.path.exists(dizin):
				os.mkdir(dizin)
			
			dosya  = open(kayitli_dosya, mode="a+", encoding="utf-8")
			dosya.write(f"Ad: {self.ad}\tSoyad:{self.soyad}\tT.C.:{self.tc}\tTelefon:{str(self.telefon)}"
			            f"\tAdres:{self.adres}\tMaaş:{str(self.maas)}\n")
			dosya.close()
		except Exception:
			print("Dosya kayıt edilirken bir hata oluştu")
	
	@classmethod
	def listele( cls ):
		try:
			dosya = open("C:\\TEST\\Personel.txt", mode="r", encoding="utf-8")
			satirlar =  dosya.readlines()
			
			for satir in satirlar:
				print(satir)
			
			dosya.close( )
		except FileNotFoundError:
			print("Dosya bulunamadı")
		except Exception:
			print("Dosya okunurken hata oluştu")
			
			