#### Tuple: Sabit Liste ###
# Listeden farkı içerik güncellenemez

# sabit_liste1 =  () # boş sabit liste
# sabit_liste2 = tuple() # boş sabit liste
# sabit_liste3 = (1,2,3,4, True, "Mehmet",22.5)
#
# print(sabit_liste1)
# print(sabit_liste2)
# print(sabit_liste3)
#
# for i in sabit_liste3:
# 	print(i)
# # sabit_liste3[3] = 5 # hata verir cunku sabit liste güncellenemez !!!
# print(sabit_liste3[3])
# print(sabit_liste3.index(3)) # değeri 3 olan elemanın indis numarasını verir
#
#
# my_tuple = (1,2,[3,4])
# print(my_tuple[2][1])
#
# print(type(my_tuple))
#
# print(2 in my_tuple) # 2 değerine sahip eleman my_tuple sabit listesinde var mı?
#
# print(5 not in my_tuple) # 5 değerine sahip eleman my_tuple sabit listesinde yok mu ?
#
#

### Set : Kume ###
kume = set() # boş küme tanımlama yöntem 1
kume2 =  {} # boş küme tanımlama yöntem 2

print(type(kume))

kume3 = {1,2,3,4,5} # dolu küme
print(kume3)

kume3.add(6)
print(kume3)

kume3.add(6) # kümeler tekrar eden değerleri içermezler
print(kume3)

kume3.add("Elma")
print(kume3)

kume3.remove("Elma") # tavsiye edilmez
print(kume3)
#
# kume3.remove("Elma") # hata verecektir
# print(kume3)

kume3.discard("Elma") # değer eğer kümede yoksa hata vermez varsa siler
print(kume3)

print(len(kume3)) # kume3 kümesinin eleman sayısını verir













