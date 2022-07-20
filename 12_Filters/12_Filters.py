##### Zip() #####

'''
Kelimenin çevirsine baktığımızdaki anlamı yansıtır.zip fermuar anlamına gelir ve bu mantıkla kullanılır.
2 Listeyi birbiri indisleri üzerine birleştiriyor. Bunu yaparken eleman sayısı az olan listeyi baz alır.

zip(list1,list2)

zip çalıştığında list, tuple veya dict döndürür.
'''

isimler  = ["Mehmet", "Ferdi","Handan", "Sena"]
yaslar = [29,15,22,15,32]

liste = list(zip(isimler,yaslar))
tuplem =  tuple(zip(isimler,yaslar))
sozlugum =  dict(zip(isimler,yaslar))

print(liste)
print(tuplem)
print(sozlugum)

for i,j in liste:
	print(f"{i} kişisi {j} yaşındadır")
	
	
##### FILTER #####

'''
sayılabilen (iterable) tipindeki değerlerin içindeki ,
 item'ları süzme işlemi yapar ve sadece True deger donduren sonuçları verir.
Verdiği sonucun tipi filter tipindedir. Bunu list veya tuple çevirmemiz gereklidir.
Döngülere göre hız olarak daha başarılıdır.
'''

# filter(func,iter)
#
# liste=[12,32,44,11,12345,6543,213234]
# cc = []
#
# for i in liste:
# 	if  i % 2 == 0:
# 		cc.append(i)
#
# print(cc)
#
# ciftler = list(filter(lambda sayi: sayi%2==0, liste))
# print(ciftler)
#
#
# tekler = list(filter(lambda sayi: sayi%2==1, liste))
# print(tekler)
#
# liste=["Python Dersleri","django", "Python", "Gazi üniversitesi"]
#
#
# def baslik(karakter):
# 	return karakter.istitle()
#
# print(tuple(filter(baslik, liste)))
#
# print(list(filter(baslik, liste)))
# print(dict(filter(baslik, liste)))
#


liste=[6,1,8,11,-5,5,9]

dd = list(filter(lambda  s: s<9 and s >=5, liste))
print(dd)

print([x for x in liste if x <9 and x >=5])


print([x for x in [6,1,8,11,-5,5,9] if x <9 and x >=5])


######## Zip() ven Filter() Birlikte Kullanımı #########
kisiler=["Sinan","Halil","Altan","Sueda"]
tarihler=[1990,1998,1989,1999]

print(list(filter(lambda zipped:1996 <zipped[1] <=2000 ,zip(kisiler,tarihler))))


