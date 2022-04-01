### SINGLE RESPONSIBILITY
class CreateOrder:
	def __init__(self,name):
		self.name = name 
		self.total = 0
		self.items = []
		
	def add_order(self,item,price):
		self.total += price
		self.items.append(item)
	
class Pay:
	def kbz(self,amount,order):
		if amount >= order.total:
			ans = amount - order.total
			return f'Purchased Successfully,your amount now ={ans}'
		
		
cart = CreateOrder('Kyaw')
cart.add_order('macbook',1200)
pay = Pay()
print(pay.kbz(2000,cart))

### open close 
### for example above method if u want to add new pay method you neet to change Pay class ,that violate open close rule ,instead try below

from abc import *
class Pay(ABC):
	
	@abstractmethod
	def pay(self,amount,order):
		pass
		
class KbzPay(Pay):
	def pay(self,amount,order):
		if amount >= order.total:
				ans = amount - order.total
				return f'Purchased Successfully,your amount now ={ans}'
		else:
			return f'not enough amount'
	

cart = CreateOrder('Zin')
cart.add_order('macbook',1800)
pay = KbzPay()
print(pay.pay(2000,cart))	

### if u want to add new payment method you dont neet to change Pay Class
#### liskov substitutaion
class Pay(ABC):
	@abstractmethod
	def pay(self,amount,order):
		pass
	
class Paypal(Pay):
	def __init__(self,email):
		self.email = email
	def pay(self,amount,order):
		if amount >= order.total:
				ans = amount - order.total
				print(f'name/',order.name)
				print(f'email/',self.email)
				return f'Purchased Successfully,your amount now ={ans}'
		else:
			return f'not enough amount'	
		
		
class Kbz(Pay):
	def __init__(self,security_code):
		self.security_code = security_code
		
	def pay(self,amount,order):
		if amount >= order.total:
				ans = amount - order.total
				print(f'name/',order.name)
				print(f'security_code/',self.security_code)
				return f'Purchased Successfully,your amount now ={ans}'
		else:
			return f'not enough amount'	


cart = CreateOrder('Myat')
cart.add_order('macbook',1900)
#pay = Kbz(1234)
pay = Paypal('kyaw@gmail.com')
print(pay.pay(2000,cart,))	