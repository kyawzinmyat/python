from abc import ABC,abstractmethod

class Burger(ABC):
	def make_burger(self):
		self.make_bum()
		self.add_meat()
		self.add_veggie()
		self.add_cheese()
		self.done()
		
	@abstractmethod
	def add_meat(self):
		pass
	@abstractmethod
	def add_cheese(self):
		pass
	
	def make_bum(self):
		print('Cutting bum \n baking bum \n done!')
	def add_veggie(self):
		print('Adding cucumber slices\n tomatoe slice \n onion rings')
	def done(self):
		print('Your burger ready to take !')
	
class ChickenBurger(Burger):
	def add_meat(self):
		print('Adding chicken slices')
	def add_cheese(self):
		pass
		
class PorkBurger(Burger):
	def add_meat(self):
		print('Adding pork slices')
	def add_cheese(self):
		pass

class PorkBurgerBeacon(Burger):
	def add_meat(self):
		print('Adding pork slices')
		print('Adding extra beacons')
	def add_cheese(self):
		pass	
	
class ChickenCheeseBurger(Burger):
	def add_meat(self):
		print('Adding chicken slices')
	def add_cheese(self):
		print('Adding extra cheese')
	
c_b = ChickenCheeseBurger()
c_b.make_burger()
	