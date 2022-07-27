from abc import ABC, abstractmethod

class Base( ABC ):
	
	def __init__( self ):
		self.id = str( )
		self.name = str( )
		self.add_date = str( )
		self.updated_date = str( )
		self.deleted_date = str( )
	
	
	@abstractmethod
	def  save( self ):
		pass
	
	@abstractmethod
	def  update( self ):
		pass
	
	@abstractmethod
	def  remove( self ):
		pass
	
	@abstractmethod
	def list_all( self ):
		pass