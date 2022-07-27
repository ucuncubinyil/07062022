from abc import ABC, abstractmethod

class Animal( ABC ):  # Animal bir abstact sınıftır
	
	@abstractmethod
	def Drink( self ):
		pass
	
	@abstractmethod
	def Walk( self ):
		pass
	
	@abstractmethod
	def Sleep( self ):
		pass
