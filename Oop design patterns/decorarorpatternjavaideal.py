from abc import ABC,abstractmethod

class Noodle(ABC):
	@abstractmethod
	def get_cost(self):
		pass
	@abstractmethod
	def get_des(self):
		pass
		
class PlainNoodle(Noodle):
	def get_cost(self):
		return 500
	def get_des(self):
		return f'Plain Noodle'
		
class Extra(Noodle):
	def __init__(self,noodle):
		self.noodle = noodle
	def get_cost(self):
		return self.noodle.get_cost()
	def get_des(self):
		return f'self.noodle.get_des()'
		
class Pork(Extra):
		def __init__(self,noodle):
			super(). __init__(noodle)
		def get_cost(self):
			return self.noodle.get_cost()+1000
		def get_des(self):
			return f'pork {self.noodle.get_des()}'
			

yum = PlainNoodle()
pork = Pork(yum)
double = Pork(pork)
print(double.get_cost())
mix = Pork(Pork(yum))
print(mix.get_cost())