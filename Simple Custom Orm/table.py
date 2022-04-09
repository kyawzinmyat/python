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
		#print("called")
		if key in data:
			return data[key]
		return object.__getattribute__(self,key)
		
	def __setattr__(self,key,value):
		super().__setattr__(key,value)
		data = object.__getattribute__(self,"_data")
		if key in data:
			self._data[key]=value
			
		
		
		
	
	
	@classmethod
	def get_name(cls):
			return cls.__name__
			
			
			
			
			
			
	# check object attribute when instantiate	
	# inspect fileds
	def validate_column(self,kwargs):
		fields  = ["id"]
		
		for name,field in inspect.getmembers(self.__class__):
			if isinstance(field,Column):
				fields.append(name)
			elif isinstance(field,ForeignKey):
				fields.append(name)	
		for name in kwargs:
				if name not in fields:
					if name[:-3] not  in fields:		
										
						raise ValueError
										
	# inspect field
	@classmethod		
	def get_create_command(cls):
			fields=[
		("id","INTEGER PRIMARY KEY AUTOINCREMENT ")
	]
	
			for name,field in inspect.getmembers(cls):
				if isinstance(field,Column):
					fields.append((f"{name}",f"{field.type}"))		
				elif isinstance(field,ForeignKey):
					fields.append((f"{name}_id",f"{field.type}"))
					
			fields=[" ".join(x) for x in fields]		
					
			return CommandFactory.get_command("create").format(table_name=cls.get_name(),fields=",".join(fields))
			
	
		
	
	
	
	
	
					
	def get_insert_command(self):
			
			fields,values,placeholder=self.get_fields_values_placeholders()
			
			command =CommandFactory.get_command("insert").format(table_name=self.__class__.get_name(),fields=",".join(fields),placeholder=",".join(placeholder))
			
			return command,values
	
	def get_update_command(self):
		fields=[]
		values =[]
		
		for name,field in inspect.getmembers(self.__class__):
			if isinstance(field,Column):
				fields.append(name+" = ? ")
			elif isinstance(field,ForeignKey):
				foreign_key=getattr(self,name)
				__class__.db.save(foreign_key)
				
		
		data = self._data
		
		for field in fields:	
			values.append(data[field[:-5]])
				
		
		
		
		command = "UPDATE {table_name} SET {fields} WHERE id={id}".format(table_name=self.__class__.get_name(),fields=",".join(fields),id=self.id)
		return command,values
				
		
		
	def check_insert_or_update(self):
			if self.id:
					return self.get_update_command()
			return self.get_insert_command()		
					
									
	def get_fields_values_placeholders(self):
		fields=[]
		values=[]
		placeholder=[]
		for name,field in inspect.getmembers(self.__class__):
				if isinstance(field,Column):
					fields.append(name)
					values.append(getattr(self,name))
					placeholder.append("?")
				elif isinstance(field,ForeignKey):
					fields.append(name+"_id")	
					values.append(getattr(self,"test1").id)
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
			elif isinstance(field,ForeignKey):
				fields.append(name+"_id")
				
		return fields	
			
		
				
		
		
	@classmethod
	def all(cls):
		data_obj =[]
		command,fields =  cls.get_select_all_command()
		
		values = cls.db.execute(command).fetchall()	
	
		for row in values:

			new_fields,new_row=cls.check_foreignkey_and_modify(fields,row)
			data = dict(zip(new_fields,new_row))
			data_obj.append(cls(**data))
		return data_obj	
	
						
	@classmethod
	def get_select_where_command(cls,kwargs):
		fields =["id"]
		for name,field in inspect.getmembers(cls):
			if isinstance(field,Column) :
				fields.append(name)
			elif isinstance(field,ForeignKey):
						fields.append(name+"_id")
		
						
		filters=[]
		param =[] 
						
		for key,value in kwargs.items():
			filters.append(key +" =?")	
			param.append(value)
			
			
		command="SELECT {fields} FROM {table_name} WHERE {filters}".format(fields=",".join(fields),table_name=cls.get_name(),filters=" AND ".join(filters))
		
		
		return command,param,fields
		
		
	@classmethod	
	def get(cls,**kwargs):
			command,param,fields = cls.get_select_where_command(kwargs)
			values=cls.db.execute(command,param).fetchone()		
			new_fields,new_values = cls.check_foreignkey_and_modify(fields,values)
			data = dict(zip(new_fields,new_values))
			
			return cls(**data)
	
					
	# if its contain foreign key that gonna make foreign key data object and add it to values .if not just return the same
			
	@classmethod		
	def check_foreignkey_and_modify(cls,fields,values):

			new_fields=[]
			new_values=[]
			for field,value in zip(fields,values):
				if field.endswith("_id"):
					field = field[:-3]
					cla = getattr(cls,field).table
					value = cla.get(id=value)
										
				new_fields.append(field)
				new_values.append(value)
			return new_fields,new_values
			
						
						
		
		
	@classmethod	
	def get_table_fields(cls):
		fields=[]
		for name,field in inspect.getmembers(cls):
				fields.append(name)
		return fields	
					
														
																					
class Column:
	def __init__(self,type):
		self.type=type
		
		
class ForeignKey:
		def __init__(self,Table):
			self.type="INTEGER"
			self.table = Table
			
		
		

						
