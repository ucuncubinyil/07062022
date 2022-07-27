#### ABSTRACTION (Abstract,Interface) #####
'''
Abstract class(soyut sınıf): Abstract sınıfların kullanım amacı tanımlanan
bir class'ın sadece base class özelliği taşıması sağlamaktır.
Python dilinde diğer dillerden farklı olarak abstract yapısı hazır
olarak tanımlıdır ve import edilmesi gereklidir.
Abstract class'lar da tanımlanan field(özellik,attribute)'lara değer
atanmaz ve metotların gövdeleri doldurulmaz.
Yani amac sadece tanımlama(miras alındığında türeyen sınıfa aktarılması
istenen özellikler).

Abstract methodlar sadece Abstract(ABC) class'larda bulunurlar ama class
Abstract diye bütün methodlar @abstractmethod olmak zorunda değil.
'''



# a = Animal() TypeError: Can't instantiate abstract class Animal with abstract methods Drink, Sleep, Walk

# from Bird import Bird
#
#
# karga =  Bird()
# karga.Walk()
# karga.Drink()
# karga.Sleep()


"""
Bir Eticaret Sitesinin ALTYAPISINI OLUŞTURUNUZ
Product => Id,name,price,stock,adddate,updatedate,deletedate
Category => Id,name,description,adddate,updatedate,deletedate
User => Id,name,surname,username,password,email,adddate,updatedate,deletedate =>
 Member,Admin
Brand => Id,name,description,adddate,updatedate,deletedate
Kayıt,Listele gibi fonksiyonlar tanımlayınız.
"""

from  Product import Product

usb_bellek =  Product()
usb_bellek.id =  2
usb_bellek.name = "Verbatin 16 GB USB Bellek USB 3.0"
usb_bellek.stock =  26
usb_bellek.price =  20.50
usb_bellek.add_date = "01.01.2022"
usb_bellek.updated_date =  "06.06.2022"


usb_bellek.save()