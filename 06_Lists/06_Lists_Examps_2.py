meyveler = list( )
sebzeler = list( )

ELMA = 0
ARMUT = 0
MUZ = 0
KIRAZ = 0
CILEK = 0
PATLICAN = 0
DOMATES = 0
BIBER = 0
PATATES = 0
SOGAN = 0
print("************     HALE HOŞ GELDİNİZ       ************")
while True:
	
	print("Meyve mi, sebzemi istersiniz (S/M). Çıkmak için (Ç)")
	secim =  input("Seçiminiz: ").upper() # kelimeleri büyük harfe çevir
	
	if secim == "M":
		while True:
			print("""
					1- Elma
					2- Armut
					3- Muz
					4- Kiraz
					5- Çilek
					6- Anamenü
			""")
			meyve  = input("Seçiminiz: ")
			if meyve.isalpha(): # girilen değer karakter mi (56356, ksjadlkajsd)
				print("Hatalı Seçim")
			else:
				if meyve == "1":
					if "ELMA"  not in meyveler: # listede var olan meyveyi tekrar ekeleme
						meyveler.append("ELMA")
					ELMA += int(input("Kaç kilo elma almak istersiniz"))
					donus  = input("Başka bir arzunuz var mı ?(E/H)").upper()
					if donus == "E":
						continue
					else:
						break
				elif meyve == "2":
					if "ARMUT" not in meyveler:
						meyveler.append("ARMUT")
					ARMUT += int(input("Kaç kilo armut almak istersiniz: "))
					donus = input( "Başka bir arzunuz var mı ?(E/H)" ).upper( )
					if donus == "E":
						continue
					else:
						break
						
				elif meyve == "6":
					break
		
	elif secim == "S":
		pass
	elif secim == "Ç":
		break
	
	else:
		print("Hatalı seçim")
