#### Küme işlemleri
kume = { 11, 22, 33, 44 }
kume2 = { 33, 44, 55, 66, 77, 88, 99 }

#İki Küme Farkı

kume_fark = kume - kume2 # 1. yöntem tavsiye edilmeyen
print(kume_fark)

kume_fark_2 =  kume.difference(kume2) # Tavisiye edilen yöntem
print(kume_fark_2)

kume_fark_3 =  kume2.difference(kume)
print(kume_fark_3)

# Küme Kesişim
kume_kesisim =  kume & kume2 #1. Tavsiye edilmeyen
print(kume_kesisim)

kume_kesisim_2 =  kume.intersection(kume2) #2. Tavsiye edilen
print(kume_kesisim_2)


# Küme Birleşim

kume_birlesim =  kume.union(kume2)
print(kume_birlesim)

# kume_birlesim_2 = kume + kume2 # hata verir +  işlemi desteklenmez
# print(kume_birlesim_2)

#Alt Küme
print(f"Kume kümesi Küme2 kümesinin alt kümesi midir: {kume.issubset(kume2)}")

#Üst Küme
print(f"Kume kümesi Kume2 kümesinin üst kümesi midir? {kume.issuperset(kume2)}")

#Ayrık Küme
print(f"Kume kümesi ile Kume2 kümeleri ayrık küme mi ? {kume.isdisjoint(kume2)}")

