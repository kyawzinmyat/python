import inspect
#import Database
from Command import CommandFactory



class Table:	
	
	
	def __init__(self,**kwargs):
		self._data={"id":None}
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
	def get_create_command(cls):
			fields=[
		("id","INTEGER PRIMARY KEY AUTOINCREMENT ")
	]
			for name,field in inspect.getmembers(cls):
				if isinstance(field,Column):
					fields.append((f"{name}",f"{field.type}"))
			fields=[" ".join(x) for x in fields]	
			command ="CREATE TABLE {nam} ({fields})".format(nam=cls.get_name(),fields=",".join(fields))
			
			return command
		
		
	# check object attribute when instantiate	
	
	def validate_column(self,kwargs):
		fields =[]
		for name,field in inspect.getmembers(self.__class__):
			if isinstance(field,Column):
				fields.append(name)
		
		for name in kwargs:
				if name not in fields:
					raise ValueError
					
					
	def get_insert_command(self):
			fields=[]
			values=[]
			placeholder=[]
			
			for name,field in inspect.getmembers(self.__class__):
				if isinstance(field,Column):
					fields.append(name)
					values.append(getattr(self,name))
					placeholder.append("?")
			command ="INSERT INTO {table_name}({fields}) VALUES({placeholder})".format(table_name=self.__class__.get_name(),fields=",".join(fields),placeholder=",".join(placeholder))
			return command,values
			
		

							
														
																					
class Column:
	def __init__(self,type):
		self.type=type
		
		

						
