from abc import ABC,abstractmethod


#problem case
class Pizza_Store(ABC):
	
	@abstractmethod				
	def create_Pizza(self):
		pass			
	
	def order_Pizza(self):
		self.pizza= self.create_Pizza()
		self.pizza.order()
		
		
		
class Ny_Pizza_Store(Pizza_Store):
		def create_Pizza(self):
			return Ny_Plain_Pizza()		
		
		

		
				
						
								
												
		
	
class Pizza(ABC):
		
		def __init__(self,type,sauce,dough):
			self.type=type
			self.sauce=sauce
			self.dough=dough
			self.toppings=[]
			
			
		def order(self):
			self.prepare()
			self.pack()
			self.get_Description()
						
			
		def prepare(self):
			print(f"{self.type} is preparing ...")

		def pack(self):
			print("Pizza is packing")	
			
		
	
		def get_Description(self):
			print(f"Pizza Type/ {self.type}")
			print(f"Dough / {self.dough}")
			print(f"Sauce / {self.sauce}")
			print("Topping list")
			for topping in self.toppings:
				print(topping)
				
				
			
class Ny_Plain_Pizza(Pizza):
		def __init__(self):
			self.type="New York style cheese and Sauce Pizza"
			self.dough="Thin Crust Dough"
			self.sauce ="Marinara Sauce"
			self.toppings=["Sausages","Tomatoes","Chicken slice"]
		
		
		
class Chi_Cheese_Pizza(Pizza):
		
		pass
			
class Unknown_Pizza(Pizza):
		
		def prepare(self):
			print(f"There is no such a \"{self.type}\" pizza type in our menu")
			
		def pack(self):
			pass
		
		def get_Description(self):
			return f"Unknown Pizza"

			
						
												
	
kfc=Ny_Pizza_Store()
kfc.order_Pizza()

		