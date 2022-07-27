############## KALITIM-INHERITANCE ###############

'''
Inheritance veya kalıtım bir sınıfın başka bir sınıfan özelliklerini(attribute)
 ve metodlarını miras almasıdır.
Bu yapı aslında bizim kend anne babamızdan değişik özelliklerive davranışları miras almamıza benzetilebilir.

Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz.
 Bunun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor.
Aslında baktığımız zaman bu sınıfların hepsinin belli ortak metodları ve özellikleri bulunuyor.
O zaman bu ortak özellikleri ve metotları tekrar tekrar bu sınfıların içinde
tanımlamak yerine, bir tane ana-temel(base) class tanımlayıp ortak özellik ve metotları bu class'ta yazıp diğer classların bu base classı miras almasını sağlayabiliriz. Inheritance'ın temel amacı budur.
'''

from Yonetici import Yonetici

# yonet =  Yonetici("Murat", 7000, "Bilgi İşlem")
# # print(yonet.ismi)
# #
# # yonet.bilgi_goster()
# #
# # Yonetici.departman_degistir("Sistem", yonet )
# # yonet.bilgi_goster()
#
#
# yonet.zam_yap(300)
# yonet.bilgi_goster()


### OVERRIDING (iptal Etme-Revize)
"""
Eğer biz miras aldığımız methodları aynı isimle kendi sınıfımızda tekrar tanımlarsak,
 artık metodu çağırdığımızda base class'dan değil kendi türettiğimiz class'tan çalıştırmış oluyoruz.
Bu işleme OOP override etme denir.

Örneğin artık çalışan sınıfının init metodunu kullanmak yerine Yönetici sınıfında init metodunu override edebiliriz.
Böylece Yönetici sınıfına ekstra bir attribute ekleyebiliriz.
"""

# yonet = Yonetici("Mehmet", 3233, "IT", 25)
# yonet.bilgi_goster()


##SUPER Anahtar Kelimesi
"""
super anahtar kelimesi: türemiş sınıfta base sınıftan de miras alınan bir
methodu tekrar tanımladığımızda override işlemi gerçekleşiyordu.
Super keyword ü ile bu methodu override edip yok etmek yerine basedeki gerçekleşen
 işlemi alıp sadece türemiş sınıfta atanan özelliği eklemizi sağlar.
  Böyle Base classdaki method komple yok sayılmak yerine yeni özellikle revize edilmiş olur.
"""

# yonet = Yonetici("Mehmet", 3233, "IT", 25)
# yonet.bilgi_goster()
# yonet.departman_degistir("Sistem")
# yonet.bilgi_goster()

# from Otomobil import Otomobil
# from Kamyon import Kamyon
#
# o = Otomobil()
# o.marka = "Tofaş"
# o.model = "Şahin"
# o.renk = "Beyaz"
# o.uretim_yili =  1995
# o.fiyat = 55000.00
# o.kasa_tipi = "Sedan"
# o.vites_tipi = "Manüel"
#
# o.bilgi_yaz()
# print("\n*****************************************************")
#
# k = Kamyon()
# k.marka = "Ford"
# k.model = "Truck"
# k.renk = "Sarı"
# k.uretim_yili =  1999
# k.fiyat = 1000000.00
# k.tasima_kapasitesi = 50000
# k.yakit_deposu_sayisi = 2
# k.bilgi_yaz()

from BuzDolabi import BuzDolabi
from CamasirMakinesi import CamasirMakinesi
from texttable import Texttable

####### POLIMORPHISM #########
"""
Polimorfizm(Çok biçimlilik): 1 fonksiyonun birden farklı işlemler
gerçekleştirmesine denir.
"""

arcelik = BuzDolabi( )
arcelik.marka = "Arçelik"
arcelik.model = "XC-4a4a"
arcelik.renk = "Beyaz"
arcelik.fiyat = 7655.36
arcelik.hacim = 500000
arcelik.kapak_sayisi = 4
arcelik.enerji_sinifi = "A+++"
# arcelik.kaydet()


vestel =  CamasirMakinesi()
vestel.marka = "Vestel"
vestel.model = "VS-456a"
vestel.renk = "Gri"
vestel.fiyat =  6000.00
vestel.enerji_sinifi = "B"
vestel.yikama_kapasitesi = 9
vestel.hizli_yikama = True
# vestel.bilgi_yaz()

t =  Texttable()
t.set_cols_align( [ "c", "c", "c","c", "c", "c" ] )
t.add_rows( [ [ 'Marka', 'Model', 'Enerji Sınıfı', 'Fiyat', 'Yıkama Kapasitesi', 'Hızlı Yıkama' ],
              [ vestel.marka, vestel.model, vestel.enerji_sinifi, vestel.fiyat, vestel.yikama_kapasitesi, vestel.hizli_yikama ] ]
            )
print( t.draw( ) )
