import inspect

from Command import CommandFactory



class Table:	
	
	db=None
	
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
	
	
	# inspect field
	@classmethod		
	def get_create_command(cls):
			fields=[
		("id","INTEGER PRIMARY KEY AUTOINCREMENT ")
	]
	
			for name,field in inspect.getmembers(cls):
				if isinstance(field,Column):
					fields.append((f"{name}",f"{field.type}"))
			fields=[" ".join(x) for x in fields]	
			return CommandFactory.get_command("create").format(table_name=cls.get_name(),fields=",".join(fields))
			
	
		
		
	# check object attribute when instantiate	
	# inspect fileds
	def validate_column(self,kwargs):
		fields  = self.get_fields_with_id() 
		
		for name in kwargs:
				
				if name not in fields:
					raise ValueError
					
	
					
	def get_insert_command(self):
			
			fields,values,placeholder=self.get_fields_values_placeholders()
			
			command =CommandFactory.get_command("insert").format(table_name=self.__class__.get_name(),fields=",".join(fields),placeholder=",".join(placeholder))
			
			return command,values
			
	def get_fields_values_placeholders(self):
		fields=[]
		values=[]
		placeholder=[]
		for name,field in inspect.getmembers(self.__class__):
				if isinstance(field,Column):
					fields.append(name)
					values.append(getattr(self,name))
					placeholder.append("?")	
		return fields,values,placeholder
		
	
	@classmethod
	def get_select_all_command(cls):
		fields=cls.get_fields_with_id()			
			
		return  CommandFactory.get_command("all").format(fields=",".join(fields),table_name=cls.get_name()),fields
			
	@classmethod		
	def get_fields_with_id(cls):
		fields=["id"]
		for name,field in inspect.getmembers(cls):
			if isinstance(field,Column):
				fields.append(name)
				
		return fields	
			
					
		
	@classmethod
	def all(cls):
		data_obj =[]
		command,fields =  cls.get_select_all_command()
		
		values = cls.db.execute(command).fetchall()	
		for row in values:
			data = dict(zip(fields,row))
			data_obj.append(cls(**data))							
		return data_obj
		
		
	@classmethod	
	def get_table_fields(cls):
		fields=[]
		for name,field in inspect.getmembers(cls):
				fields.append(name)
		return fields	
					
														
																					
class Column:
	def __init__(self,type):
		self.type=type
		
		

						
