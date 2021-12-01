from abc import ABC,abstractmethod


#abstract 
class Engine(ABC):
	
	@abstractmethod
	def get_type(self):
		pass
	
	@abstractmethod
	def price(self):
		pass
		
#concret
class DiselEngine(Engine):
	
	
	def get_type(self):
		return f'Disel Engine Type '
		
	def price(self):
		return 500

class PetrolEngine(Engine):
	def get_type(self):
		return f'Petrol Engine Type '
	def price(self):
		return 400
	


## abstract

class ToyotaFactory(ABC):
	@abstractmethod
	def manufacture(self):
		pass
	
	@abstractmethod
	def get_model(self):
		pass
	
	@abstractmethod
	def price(self):
		pass
	
#concret		
class DiselFactory(ToyotaFactory):
	def __init__(self):
		self.engine = None
	
	def manufacture(self):
		self.engine = DiselEngine()
	
	def __str__(self):
		return f'Toyota car is making'
	
	def get_model(self):
		return f'2020/{self.engine.get_type()}'
		
	def price(self):
		return 1000+self.engine.price()
		
class PetrolFactory(ToyotaFactory):
	
	def __init__(self):
		self.engine = PetrolEngine()
		
	def get_model(self):
		return f'2020/{self.engine.get_type()}'
		
	def price(self):
		return 1000+self.engine.price()
	

toyota = DiselFactory()
toyota.manufacture()	
print(toyota.get_model())
print(toyota.price())

	
	
