masalar = { "Masa-1": "F", "Masa-2": "F", "Masa-3": "F", "Masa-4": "F", "Masa-5": "F" }
corbalar = { "1-Mercimek Çorbası": "7.00", "2-Ezogelin Çorbası": "7.00", "3-Düğün Çorbası": "10.00" }
baliklar = { "1-Mezgit": "27.00", "2-Palamut": "35.00", "3-Çupra": "45.00", "4-Somon": "100.00" }
etler = { "1-Pirzola": "56.00", "2- Biftek": "65.00", "3-Lokum": "45.00" }
makarnalar = { "1-Bolonezli": "35.00", "2-Körili": "35.00", "3-Spagetti": "35.00" }
ara_sicaklar = { "1- İçli Köfte": "20.00", "2-Sigara Böreği": "40.00", "3-Patso": "10.00" }
salatalar = { "1-Çoban Salatası": "20.00", "2-Sezar Salata": "45.00", "3-Mevsim Salatası": "20.00" }
icecekler = { "1-Kola": "8.00", "2-Şalgam": "7.00", "3-Ayran": "7.00" }

for i in baliklar:
	print( i )
	print( baliklar[ i ] )

siparisler = dict( )

while True:
	menu = int( input( """
			Sipariş Almak İçin      1
			Hesap Almak İçin        2
			Menü Güncelleme İçin    3
			Çıkış İçin              4
			Seçiminiz:
	"""
	                   )
	            )
	
	if menu == 1:
		while True:
			print( """
			######################## KARDEŞLER ET LOKANTASINA HOŞ GELDİNİZ ########################
			"""
			       )
			kisi_sayisi = int( input( "Kaç kişiyiz ?" ) )
			
			musteri_masasi = str( )
			for masa in masalar:
				if masalar[ masa ] == "F":
					musteri_masasi = masa
					print( musteri_masasi )
					masalar[ masa ] = "T"
					break
			
			siparis = dict( )
			
			for i in range( kisi_sayisi ):
				print( i + 1, " . müşteri siparişi" )
				
				while True:
					print( """
						1- Çorba çeşitleri
						2- Balık çeşitleri
						3- Et çeşitleri
						4- Makarna çeşitleri
						5- Arasıcak çeşitleri
						6- Salata çeşitleri
						7- İçeçek çeşitleri
					"""
					       )
					
					secim = int( input( "Seçiminiz: " ) )
					
					if secim == 1:
						for i in corbalar:
							print( i, "\t\t:", corbalar[ i ] )
						secim_corba = int( input( "Çorba Seçiminiz:" ) )
						
						if secim_corba == 1:
							siparis[ "Mercimek Çorbası" ] = "7.00"
						elif secim_corba == 2:
							siparis[ "Ezogelin Çorbası" ] = "7.00"
						elif secim_corba == 3:
							siparis[ "Düğün Çorbası" ] = "10.0"
						else:
							print( "Hatalı çorba seçimi" )
					elif secim == 2:
						for i in baliklar:
							print( i, "\t\t:", baliklar[ i ] )
						secim_balik = int( input( "Balık Seçimi" ) )
						
						if secim_balik == 1:
							siparis[ "Mezgit" ] = "27.00"
						elif secim_balik == 2:
							siparis[ "Palamut" ] = "35.00"
						elif secim_balik == 3:
							siparis[ "Çupra" ] = "45.00"
						elif secim_balik == 4:
							siparis[ "Somon" ] = "100.00"
						else:
							print( "Hatalı Balık Seçimi !!!" )
					elif secim == 3:
						for i in etler:
							print( i, "\t\t:", etler[ i ] )
						secim_et = int( input( "Seçiminiz: " ) )
						
						if secim_et == 1:
							siparis[ "Pirzola" ] = "56.00"
						elif secim_et == 2:
							siparis[ "Biftek" ] = "65.00"
						elif secim_et == 3:
							siparis[ "Lokum" ] = "45.00"
						else:
							print( "Hatalı et seçimi" )
					elif secim == 4:
						for i in makarnalar:
							print( i, "\t\t:", makarnalar[ i ] )
						secim_makarna = int( input( "Seçiminiz:" ) )
						
						if secim_makarna == 1:
							siparis[ "Bolonezli" ] = "35.00"
						elif secim_makarna == 2:
							siparis[ "Körili" ] = "35.00"
						elif secim_makarna == 3:
							siparis[ "Spagetti" ] = "35.00"
						else:
							print( "Hatalı makarna seçimi" )
					elif secim == 5:
						for i in ara_sicaklar:
							print( i, "\t\t:", ara_sicaklar[ i ] )
						secim_ara_sicak = int( input( "Seçiminiz:" ) )
						
						if secim_ara_sicak == 1:
							siparis[ "İçli Köfte" ] = "20.00"
						elif secim_ara_sicak == 2:
							siparis[ "Sigara Böreği" ] = "40.00"
						elif secim_ara_sicak == 3:
							siparis[ "Patso" ] = "10.00"
						else:
							print( "Hatalı ara sıcak seçimi" )
					elif secim == 6:
						for i in salatalar:
							print( i, "\t\t:", salatalar[ i ] )
						secim_salata = int( input( "Seçiminiz:" ) )
						
						if secim_salata == 1:
							siparis[ "Çoban Salatası" ] = "20.00"
						elif secim_salata == 2:
							siparis[ "Sezar Salata" ] = "45.00"
						elif secim_salata == 3:
							siparis[ "Mevsim Salata" ] = "20.00"
						else:
							print( "Hatalı salata seçimi" )
					elif secim == 7:
						for i in icecekler:
							print( i, "\t\t:", icecekler[ i ] )
						secim_icecek = int( input( "Seçiminiz:" ) )
						
						if secim_icecek == 1:
							siparis[ "Kola" ] = "8.00"
						elif secim_icecek == 2:
							siparis[ "Şalgam" ] = "7.00"
						elif secim_icecek == 3:
							siparis[ "Ayran" ] = "7.00"
						else:
							print( "Hatalı içecek seçimi" )
					else:
						print( "Hatalı seçim" )
					
					siparisler[ masa ] = siparis
					
					cevap = input( "Başka bir arzunuz var mı ?(E/H)" ).upper( )
					
					if cevap == "E":
						continue
					elif cevap == "H":
						break
					else:
						print( "Hatalı seçim" )
						continue
			
			break
	
	elif menu == 2:
		print( "***********************HESAP BÖLÜMÜ***********************" )
		
		for i in siparisler:
			print( i, "====>", siparisler[ i ] )
		
		hesap = 0
		masa_hesabi = input( "Hangi Masa Hesabı İsteniliyor?" )
		for i in siparisler[ "Masa-" + masa_hesabi ].values( ):
			hesap += float( i )
		print( hesap )
		
		hesap_odendi_mi = input( "Hesap ödendi mi ?(E/H)" ).upper( )
		
		if hesap_odendi_mi == "E":
			masalar[ "Masa-" + masa_hesabi ] = "F"
		
		if i in masalar:
			print( i, "\t\t:", masalar[ i ] )
	
	elif menu == 3:
		pass
	
	elif menu == 4:
		break
	
	else:
		print( "Hatalı seçim" )
