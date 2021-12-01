from abc import ABC,abstractmethod

class Meal(ABC):
	@abstractmethod
	def price(self):
		pass
	
class PlainRice(Meal):
	def price(self):
		return 500
	
class BrownRice(Meal):
	def price(self):
		return 1000
		
class PlainNoodle(Meal):
	def price(self):
		return 500
		
class Curry(ABC):
	@abstractmethod
	def with_rice(self):
		pass
		
	@abstractmethod
	def with_blownrice(self):
		pass
	
	@abstractmethod
	def with_noodle(self):
		pass
	

class ChickenCurry(Curry):
	def __init__(self):
		self.price = 1500
	
	def curry_alone(self):
		print('Chicken Curry')
		print('Preparing_________')
		print('Your order is done')
		print('Here\'s price ',self.price,'kyat')
	
	def with_rice(self):
		rice = PlainRice()
		print('Chicken Curry \n rice ')
		print('Preparing_________')
		print('Your order is done')
		print('Here\'s price ',self.price+rice.price(),'kyat')	
		
	def with_blownrice(self):
		blown_rice = BrownRice()
		print('Chicken Curry \n blown rice ')
		print('Preparing_________')
		print('Your order is done')
		print('Here\'s price ',self.price+blown_rice.price(),'kyat')	
	
	def with_noodle(self):
		noodle = PlainRice()
		print('Chicken Curry \n noodle ')
		print('Preparing_________')
		print('Your order is done')

		print('Here\'s price ',self.price +noodle.price(),'kyat')	
	


class Shop:
	def __init__(self):
		self.menu ={
			'c':ChickenCurry()
		}
	def currymenu(self):
		print('Curry')
		for i in self.menu:
			print(i)
	
	def order(self,curry,meal = None):
		if curry:
			if meal == 'rice':
				print(self.menu[curry].with_rice())
			elif meal == 'blownrice':
				print(self.menu[curry].with_blownrice())
			elif meal == 'noodle':
				print(self.menu[curry].with_noodle())
			else:
				print(self.menu[curry].curry_alone())
		
		
		
		
while True:
		shop = Shop()
		shop.currymenu()
		curry = input('Enter the curry u want to order')
		meal = input('rice/blownrice/noodle \n press enter for skip')
		
		
		shop.order(curry,meal)

		
		
	