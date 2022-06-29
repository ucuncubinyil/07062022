################## DICTIONARY (SOZLUK) ########################
"""
sozluk={} boş bir sözlük tanımı
sozluk=dict() boş bir sözlük tanımı

#Sozluk={key:value,key:value,...}

sozluk = {"renk1":"Kırmızı","renk2":"Beyaz","renk3":"Turuncu"}

print(sozluk)
print(type(sozluk))

print(sozluk["renk1"]) # sozluk elemanları key ile çağrılır ve ekrana value
# print(sozluk["Kırmızı"]) # keyError verir.
# print(sozluk["renk4"]) # olmayan key çağrıldığında KeyError: 'renk4' hatasını verir.

print(sozluk.get("renk1"))
print(sozluk.get("renk4")) # olmayan key çağrıldığında None döndürür.

sozluk["renk4"]="Mavi"
print(sozluk)
"""
"""
sozluk2={1:"Eyüp",2:"Emre",3:5}
print(sozluk2)
# sozluk2.clear()
# del sozluk2 # ram belleğinden siler.
# del sozluk2[3] # key vererek key:value silme
# print(sozluk2)

# print(sozluk2.keys())
# print(sozluk2.values())
# print(sozluk2.items())
"""
"""
sozluk1 = {"renk1":"Kırmızı","renk2":"Beyaz","renk3":"Turuncu"}
sozluk2={1:"Eyüp",2:"Emre",3:5}

print("sozluk1 uzunluk:",len(sozluk1))
print("sozluk2 uzunluk:",len(sozluk2))

print("renk1" in sozluk1)
print("renk4" in sozluk1)

print("Kırmızı" in sozluk1.values())
print("Siyah" not in sozluk1.values())
"""
"""
s1={"ad":"Selim","soyad":"Kaçar"}
s2={"soyad":"Kaçar","ad":"Selim"}
s3={"soyad":"Varan","ad":"Selim"}

print("s1 s2 ye eşit mi? : ",s1==s2)
print("s2 s3 e eşit mi? :",s2==s3)
"""

"""
sozluk1 = {"renk1":"Kırmızı","renk2":"Beyaz","renk3":"Turuncu"}
for key in sozluk1:
    print(key)

for val in sozluk1.values():
    print(val)
"""

s1={"ad":"Selim","soyad":"Kaçar"}
s2={"soyad":"Kaçar","ad":"Selim"}
s3={"soyad":"Varan","ad":"Selim"}
s4={"soy":"Kaçar","ad":"Selim","yas":30}
# s2.update(s3)
# print(s2)
#
# s4.update(s3)
# print(s4)

# s5=s2 # Ram'de aynı adreste bulunurlar. o sebeple birindeki değişiklik diğerini etkiler.
# print(s2)
# print(s5)
# s2["yas"]=30
# print(s2)
# print(s5)
# del s2["yas"]
# print(s2)
# print(s5)
# del s2
# print(s5)


# s5=s2.copy() # Ram'de farklı adreslere sahipler.
# print(s2)
# print(s5)
# s2["yas"]=30
# print(s2)
# print(s5)

# print(s2.pop(""))

# s3lu={}
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,0]
# list3 = [11,22,33]
# s3lu["x"]=list1
# s3lu["y"]=list2
# s3lu["z"]=list3
# print(s3lu)
#
# print(s3lu["x"])

#### SORU: Kullanıcıdan alınan ad,soyad,yas,cinsiyet bilgilerini Personel isimli bir sözlükte saklayın ve ad soyad bilgisini sözlükten alarak ekrana yazdırınız.

# Personel={}
#
# Personel["ad"]=input("Adınız")
# Personel["soyad"]=input("soyad:")
# Personel["yas"]=input("yaş:")
# Personel["cinsiyet"]=input("cinsiyet:")
#
# print(Personel["ad"],Personel["soyad"])
# print(Personel["soyad"])

#SORU: Bir firmanın İnsan kaynakları,Bilgi İşlem ve Muhasebe departmanlarının çalışan listelerini yöneticiden isteyerek bir dict atınız
# ve ekrana istenilen bölümdeki çalışanları listeyiniz.
"""
IK=list()
IT=list()
MHSB=list()
firma=dict()

for i in range(1):
    IK.append(input("İnsan kaynakları personel ad soyad:"))
    IT.append(input("Bilgi işlem personel ad soyad:"))
    MHSB.append(input("Muhasebe personel ad soyad:"))

firma["insan kaynaklari"]=IK
firma["bilgi islem"]=IT
firma["muhasebe"]=MHSB

secim = input("İnsan Kaynakları - Bilgi İşlem - Muhasebe bölüm adı giriniz:").replace('ş','s').replace('ı','i')

for i in firma[secim]:
    print(i)
"""

#
# yasakli_karakter = ['ı','ş','ü','ğ','ö','ç']
# uygun_karakterler = ['i','s','u', 'g', 'o', 'c']
#
# metin  = input("Lütfen metin giriniz: ").lower()
#
# for i in metin:
# 	if i in yasakli_karakter:
# 		indx = yasakli_karakter.index(i)
# 		krktr =  uygun_karakterler[indx]
# 		print(krktr)
# 		metin = metin.replace(i, krktr)
#
# print(metin)



