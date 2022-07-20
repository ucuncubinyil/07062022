import datetime


def kontrol( sayi ):
	dd = open( "C:\\TEST\\log.txt", mode="a", encoding="utf-8" )
	
	while True:
		try:
			sayi = int( sayi )
			print( sayi ** 2 )
			print( sayi / 0 )
		except Exception as e:
			print("{} -> {} Hatası"
			      .format(datetime.datetime.now()
			              .strftime("%Y.%m.%d %H:%M:%S"), e.__class__.__name__),
			      file=dd)
			# zaman -> hata sınıfı
			break
