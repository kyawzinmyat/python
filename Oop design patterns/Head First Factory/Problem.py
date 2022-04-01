from abc import ABC,abstractmethod


#problem case
class Pizza_Store:
	
	
	def create_Pizza(self,name):
		if name=="plain":
			self.pizza = Plain_Pizza("Plain Pizza")
		elif name =="cheese":
			self.pizza = Cheese_Pizza("Cheese Pizza")
	
	def order_Pizza(self,name):
		self.create_Pizza(name)
		self.pizza.prepare()
		self.pizza.pack()
		
	
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
	
piz_store=Pizza_Store()	
piz_store.order_Pizza("plain")
			
		