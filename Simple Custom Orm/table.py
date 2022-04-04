import inspect
#import Database
from Command import CommandFactory



class Table:	
	
	column=[]
	
	def __init__(self,**kwargs):
		self._data={"id":None}
		self.commands = CommandFactory()
		self.validate_column(kwargs)

		
		
			
		for i,j in kwargs.items():
			self._data[i]=j
			
			
			
		
	def __getattribute__(self,key):
		data=object.__getattribute__(self,"_data")
		if key in data:
			return data[key]
		return object.__getattribute__(self,key)
		
			
		
		
		
	
	
	@classmethod
	def get_name(cls):
			return cls.__name__
	
	@classmethod		
	def get_command(cls):
			fields=[
		("id","INTEGER PRIMARY KEY AUTOINCREMENT ")
	]
			for name,field in inspect.getmembers(cls):
				if isinstance(field,Column):
					fields.append((f"{name}",f"{field.type}"))
					cls.column.append(name)
			fields=[" ".join(x) for x in fields]	
			command ="CREATE TABLE {nam} ({fields})".format(nam=cls.get_name(),fields=",".join(fields))
			
			return command
		
		
		
	
	def validate_column(self,kwargs):
		print(self.column)
		for column in kwargs:
			if column not in self.column:
				raise ValueError
				
		

							
														
																					
class Column:
	def __init__(self,type):
		self.type=type
		
		

						
