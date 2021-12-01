from abc import ABC,abstractmethod

class Coffee(ABC):
	@abstractmethod
	def get_description(self):
		pass
	
	@abstractmethod
	def cost(self):
		pass
		
class Expresso(Coffee):
	def get_description(self):
		return 'Expresso coffee'
	
	def cost(self):
		return 1000
	
	def __str__(self):
		return f'expresso coffee is making'
		
class Extra(Coffee):
	def __init__(self,coffee):
		self.coffee = coffee

	def get_description(self):
		return self.coffee.get_description()
	

	def cost(self):
		return self.coffee.get_cost()

class Milk(Extra):
		
	def get_description(self):
		return self.coffee.get_description(),'Milk' 
	
	def cost(self):
		return 500 + self.coffee.cost()
	
	def __str__(self):
		print(self.coffee)
		return f'adding extra milk'
		
		
class ExtraMilk(Extra):
	
		
	def get_description(self):
		return self.coffee.get_description()," Extra milk"
	
	def cost(self):
		return 1000 + self.coffee.cost()
	
	def __str__(self):
		print(self.coffee)
		return f'adding extra Extra milk'
		
class Cream(Extra):
	
		
	def get_description(self):
		return self.coffee.get_description() ,'  Cream'
	
	def cost(self):
		return 300 + self.coffee.cost()
	
	def __str__(self):
		print(self.coffee)
		return f'adding extra cream milk'
		
	
exp = Expresso()
#exp_milk = Milk(exp)
#print(exp_milk)
exp_extra_milk = ExtraMilk(exp)
print(Cream(exp_extra_milk).get_description())	