from abc import ABC,abstractmethod


#problem case
class Pizza_Store(ABC):
	
	@abstractmethod				
	def create_Pizza(self):
		pass			
	
	def order_Pizza(self,type):
		self.pizza= self.create_Pizza(type)
		self.pizza.order()
		
		
		
class Ny_Pizza_Store(Pizza_Store):
		def create_Pizza(self,type):
			if type=="cheese":
						return 	Cheese_Pizza(Ny_Ingredient_Factory())
			elif type=="calm":
						return Calm_Pizza(Ny_Ingredient_Factory())
		
		

class Cal_Pizza_Store(Pizza_Store):
				def create_Pizza(self,type):
					if type=="cheese":
						return 	Cheese_Pizza(Cal_Ingredient_Factory())
					elif type=="calm":
						return Calm_Pizza(Cal_Ingredient_Factory())
							
				
						
								
												
		
	
class Pizza(ABC):
		
		def __init__(self):
			
			self.type= None
			self.sauce=None
			self.dough=None
		#	self.cheese=None
			self.toppings=["Sausages","Tomatoes","Chicken slice"]
		
			
			
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
			print(f"Cheese / {self.cheese}")
			
				
				
			
class Cheese_Pizza(Pizza):
		def __init__(self,ingredient_factory):
			self.ingredient_factory = ingredient_factory
			
		def prepare(self):
				self.type="Cheese pizza"
				self.dough=self.ingredient_factory.create_dough()
				self.cheese=self.ingredient_factory.create_cheese()
				self.sauce=self.ingredient_factory.create_sauce()
			
				
class Calm_Pizza(Pizza):
		def __init__(self,ingredient_factory):
			self.ingredient_factory=ingredient_factory
			
		
		def prepare(self):
				self.type = "calm pizza"
				self.dough=self.ingredient_factory.create_dough()
				self.cheese=self.ingredient_factory.create_cheese()
				self.sauce=self.ingredient_factory.create_sauce()
				self.calm = self.ingredient_factory.create_calm()			
				
				
								
								
										
														
		



class IngredientFactory(ABC):
		@abstractmethod
		def create_dough(self):
			pass
			
		@abstractmethod
		def create_sauce(self):
			pass
				
		@abstractmethod
		def create_cheese(self):
			pass	
			
		@abstractmethod
		def create_calm(self):
			pass
	
class Ny_Ingredient_Factory(IngredientFactory):
	def create_dough(self):
		return f"Newyork style thin crust dough"	
	def create_sauce(self):
		return f"Newyork style red sauce"	
	def create_cheese(self):
		return f"Newyork style cheese "
			
	def create_calm(self):
		return f"Fresh newyork calm"		
	

										
																				
																														
class Cal_Ingredient_Factory(IngredientFactory):
	def create_dough(self):
		return f"Cal style thin thick dough"	
	def create_sauce(self):
		return f"Cal  style tomatoe sauce"	
	def create_cheese(self):
		return f"Cal style mozar cheese "
		
			
	def create_calm(self):
		return f"Cal freeze calm"
													
class Unknown_Pizza(Pizza):
		
		def prepare(self):
			print(f"There is no such a \"{self.type}\" pizza type in our menu")
			
		def pack(self):
			pass
		
		def get_Description(self):
			return f"Unknown Pizza"

			
						
												
	
kfc=Ny_Pizza_Store()
#kfc.create_pizza("cheese")
cal = Cal_Pizza_Store()
kfc.order_Pizza("cheese")
cal.order_Pizza("calm")

		