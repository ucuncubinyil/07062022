############### LİSTE list() #####################
# listem = list( )  # boş liste oluşturma yöntem 1
#
# listem = [ ]  # boş liste oluşturma yöntem 2
#
# listem = [ 2, "Mehmet", False, 25.6 ]
#
# print(listem[3]) # dizi elemanına ulaşmak için elemanın sıra numarası
# 				# nın bir eksiği yazılır
# print(listem[2])
# print(listem)
# print(type(listem))
#
# #listeye veri ekleme
#
# listem +=[99] #1. yöntem tavsiye edilmeyen
# listem += ["Malatya"]
# listem += ["Konya"]
# print(listem)
#
# listem.append("Mehmet Nuri") # 2. yöntem tavsiye edilen
# print(listem)
#
#
#
# #Listeden veriyi silme
#
# del listem[5] # Tavsiye edilmeyen
# print(listem)
#
# listem.remove("Mehmet Nuri") # Tavsiye edilen
# print(listem)
#
# # Çoklu Veri Ekleme
#
# isim_listesi = []
#
# isim_listesi += ["Ahmet","Mehmet","Osman"] # tavsiye edilmeyen
# print(isim_listesi)
#
# isim_listesi.append(["Ali","Veli","Kerim"])
# print(isim_listesi)
#
# print(isim_listesi[3][2]) # çok boyutlu dizi(liste)

# *** Listede verilen index veri ekleme ***
# rakamlar = [ 1, 2, 3, 4, 6, 7 ]
# print(rakamlar)
# print(rakamlar[4])
#
# rakamlar.insert(4,5) # 4. indise sahip olan rakamın yerine 5 i ata sağdakileri 1 sağa kaydır
# print(rakamlar)
# print(rakamlar[4])
#
#
# # *** Listedeki değerin index'ine ulaşma ***
# print(f"5 sayısının listem listesindeki indis numarası {rakamlar.index(5)}")
#
# #SORU: 7 rakamının indis numarasını ekrana yazdırınız.
# print(rakamlar.index(7))
#
# sayilar = ["Mehmet","Ali",990,550,770]
# print(sayilar.index("Mehmet"))
#
# isim_listesi = [ "Ahmet", "Mehmet", "Osman", "Burak", "Kemal", "Mustafa" ]
#
# print( isim_listesi.index( "Osman", 1, 3 ) )  # 1-3 indisler arası ara
# print( isim_listesi.index( "Osman", 1 ) )  # 1. indisten sonra ara
#
# # *** Listedeki eleman sayısını bulma ***
# print( len( isim_listesi ) )  # eleman sayısını verir  !!!! indis numarası ile karışmasın
#
# # SORU: isimler listesindeki değerleri ekrana alt alta yazdırınız.
#
# for isimler in isim_listesi:
# 	print( isimler )
#
# for isimler in range( len( isim_listesi ) ):
# 	print( isim_listesi[ isimler ] )
#
# i = 0
# while i < len( isim_listesi ):
# 	print( isim_listesi[ i ] )
# 	i += 1


# *** Listedeki bir değerin kaç defa eklendiğini bulma ***
#
# sayilar = [ 10, 20, 30, 10, 20, 40, 30, 30, 50, 50 ]
# print(sayilar.count(20)) # tekrar eden eleman sayısını verir
#
#
# i =0
# for sayi in sayilar:
# 	if sayi == 20:
# 		i+=1
# print(i)
#
# # Aynı eleman bulundurmama örneği
# meyveler = ["Armut", "Kiraz"]
# giris =  input("Meyve Gir")
# if  meyveler.count(giris)>0:
# 	print("Bu meyve var zaten")
# else:
# 	meyveler.append(giris)
#
# print(meyveler)
#


# SIRALAMA İŞLEMLERİ
# import locale
# locale.setlocale(locale.LC_ALL,"tr_TR.UTF-8") # Türkçe karkter sistemi için sisteme türkçe varsayılan
# #atandı
#
# #SORT  metinsel verilerde A-Z ye sıralar, sayısal verilerde küçükten büyüğe sıralar
#
# sehirler =  ["İstanbul", "Ankara","Şanlıurfa","Mardin","Van", "Zonguldak","Sivas", "Ordu"]
#
# sehirler.reverse()
# print(sehirler)
#
# sehirler.sort(key=locale.strxfrm)
# print(sehirler)
#
# sehirler = ["Bursa","Van","Edirne"]
# sehirler.sort()
# print(sehirler)
#
# sayilar =  [6,5,8,12,65,25,489,65,4798]
# sayilar.sort()
# print(sayilar)
#
# sayilar.sort(reverse=True)
# print(sayilar)
#
# sehirler.sort(reverse=True)
# print(sehirler)
#

#### Listeden değerleri dışarı atma
#
# sayilar = [ 1, 2, 3, 4, 5, 6 ]
# print(sayilar)
#
# sayilar.pop() #Varsayılan son veriyi siler
# print(sayilar)
#
# sayilar.pop(3) # 2. indise sahip olan veriyi siler
# print(sayilar)
#
# ##### bir değerin listede var olup olmadığı kontrol etme
#
# giris = int(input("Sayı gir"))
#
# if giris not in sayilar:
# 	sayilar.append(giris)
# else:
# 	print("Bu sayı zaten listede var")
#
# sayilar.sort()
# print(sayilar)
#
#
# liste1 = [ 1, 2, 3 ]
# liste2 = [ 3, 4, 5 ]
#
# listeler = liste1 + liste2
# print(listeler)
# print(max(listeler)) # En yüksek değeri verir
# print(min(listeler)) # En düşük değeri verir
# print(sum(listeler)) # liste içinmdeki değerleri toplar
#
#
# liste =  list()
# for i in range(11):
# 	liste.append(i)
# 	# liste[i] = i tercih edilmeyen
# print(liste)
# print(max(liste))
# print(min(liste))
# print(sum(liste))


# *** Tek satırda for yazma işlemi ***
#
# liste = [a for a in range(11)] # tek satırda for yazma
#
# print(liste)
#

# SORU 10 ile 100 arasındaki çift sayıları bir listeye atın.

liste = list()

# for x in range(10,101,2):
# 	liste.append(x)
# print(liste)


for x in range(10,101):
	if x % 2 != 0:
		liste.append(x)
	
print(liste)

liste = [ x for x in range(11,101,2)]
print(liste)
