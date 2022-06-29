"""
# SORU: sözlük uygulaması olsun Tr-Eng
#       sözlük={"siyah":"black"...}
#       kullanıcı 4 seçenekli bir menü verelim
#          1-Arama
           2-Çıkarma
           3-Listeleme
           4-Çıkış

        Kullanıcı 1'e basarsa ->
            - Aranacak kelimeyi giriniz:
            - Bu kelime dict varsa english karşılığını yazılır.
            - Yoksa uygulamayı geliştirmek istermisiniz?
                - E ise bu kelimenin ingilizce karşılığını alırız ve sözlüğe eklenir.
                - H ise Peki.. 
        Kullanıcı 2'e basarsa -> 
            - Çıkarılmak istenen kelime:
            - Kelime sözlükte varsa çıkartılır.
            - Yoksa uyarı verilir.
        Kullanıcı 3'e basarsa ->
            - Tum key value lar listenilir.
            - KEY -> VALUE
        Kullanıcı 4'e basarsa ->
            - Döngü sonlanır..
"""

sozluk = {"araştırma": "survey", "ummak": "expect", "dikkate almak": "conside"}
print("***********TR-ENG SÖZLÜK***********")
while True:
	secenekler = int(input("""
		1- Arama
		2- Çıkarma
		3- Listeleme
		4- Güncelleme
		5- Çıkış
	"""))
	
	if secenekler == 5:
		break
	elif secenekler == 1:
		kelime =  input("Kelimeyi giriniz:")
		if kelime in sozluk:
			print(sozluk.get(kelime))
		else:
			secim =  input("Uygulamayı geliştirmek ister misiniz? (E/H)").upper()
			if secim == "E":
				kelimeing =  input(kelime+ " kelimesinin İngilizce anlamını giriniz:")
				sozluk[kelime] = kelimeing
			else:
				print("Peki...")
	
	elif secenekler == 2:
		silinecek_kelime =  input("Lütfen silinecek kelimeyi yazınız: ")
		if silinecek_kelime in sozluk:
			del sozluk[silinecek_kelime]
			print("Silme işlemi başarılı")
		else:
			print("Bu kelime sözlükte yok")
	elif secenekler ==  3:
		print(sozluk)
	
	elif  secenekler ==  4:
		kelime = input( "Değişecek Kelimeyi giriniz:" )
		if kelime in sozluk:
			yeni_anlam =  input("Yeni anlamı giriniz")
			sozluk[kelime] = yeni_anlam
	else:
		print("Hatalı seçim")
