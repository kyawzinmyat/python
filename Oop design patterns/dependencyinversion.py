from abc import ABC,abstractmethod
class Flyable(ABC):
	@abstractmethod
	def fly(self):
		pass

	
			
class Bird(Flyable):
	def __init__(self,name):
		self.name = name
	def fly(self):
		print(self.name,'is flying')	


class Plane(Flyable):
	def __init__(self,name):
		self.name = name
		
	def fly(self):
		print(self.name,'is flying')						
	
class Fly:
	def __init__(self,object:Flyable):
			self.object = object
	def fly(self):
		self.object.fly()
		
bluebird = Bird('bluebird')
borin7 = Plane('borin7')
bluebird.fly()
borin7.fly()