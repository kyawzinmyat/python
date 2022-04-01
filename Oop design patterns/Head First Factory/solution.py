from abc import ABC,abstractmethod


#problem case
class Pizza_Store:
	def __init__(self,factory):
		self.factory = factory
		
	
	
		
	
	def order_Pizza(self,name):
		self.pizza =self.factory.create_Pizza(name)
		self.pizza.prepare()
		self.pizza.pack()
		
		
		
		
class Pizza_Factory:
	def create_Pizza(self,name):
		if name=="plain":
			return Plain_Pizza("Plain Pizza")
		elif name =="cheese":
			return Cheese_Pizza("Cheese Pizza")
		else:
			return Unknown_Pizza(name)
	
		
				
						
								
												
		
	
class Pizza(ABC):
		
		def __init__(self,type):
			self.type=type
		
		def prepare(self):
			print(f"{self.type} is preparing ...")

		def pack(self):
			print("Pizza is packing")	
		
		@abstractmethod
		def get_Description(self):
			pass
			
			
class Plain_Pizza(Pizza):
		
		def get_Description(self):
			return f"Just plain pizza"


class Cheese_Pizza(Pizza):
		
		def get_Description(self):
			return f"Pizza with cheese"
			
			
class Unknown_Pizza(Pizza):
		
		def prepare(self):
			print(f"There is no such a \"{self.type}\" pizza type in our menu")
			
		def pack(self):
			pass
		
		def get_Description(self):
			return f"Unknown Pizza"
			
	
piz_store=Pizza_Store(Pizza_Factory())	
piz_store.order_Pizza("chese")
			
		