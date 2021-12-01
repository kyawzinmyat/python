from abc import ABC,abstractmethod
import random 
import string

class User:
	def __init__(self,name,age):
		self.bank_name = None
		self.name = name
		self.age = age
		
		

def code_generator(total):
	letter = string.ascii_letters
	number = string.digits
	ans=""
	for i in range(total):
		if  random.random() > 0.2:
			ans += random.choice(letter)
		ans+= random.choice(number)
	return ans




class Bank(ABC):
	
	@abstractmethod
	def create_card(self):
		pass

class KBZ(Bank):
	def __init__(self):
		self.bank_name = 'KBZ'
		self.accounts ={}
	#	self.register = Register
	
	
	def create_card(self,user):
		self.accounts[user.name]=None
		print('Account create successfully')
		print('name /',user.name)	
		print('age /',user.age)
		print('--------------------------')
			




class PayRoll(ABC):
	def __init__(self):
		pass
		
	@abstractmethod
	def varify(self):
		pass
		
	
	@abstractmethod
	def cash_in(self):
		pass
		
	@abstractmethod
	def cash_out(self):
		pass
		
class KBZPay(PayRoll):
	def __init__(self,bank):
		self.varified = False
		self.bank = bank
	
	
	def varify(self,name):
		try:
			if name in self.bank.accounts:
				self.varified = True
				print('Wellcome You can use KBZ services now !')
		except:
			print('Sorry Your name is not registerd')
		
		
	def cash_in(self,name,amount):
		if self.varified:
				self.bank.accounts[name]= amount
				print('Name /',name)
				print('Your account balance is /',amount,'kyat')
				
		
	def cash_out(self,name,amount):
		if self.varified:
			balance = self.bank.accounts[name]
			if balance >= amount:
				result =self.bank.accounts[name] = balance-amount
				print('name /',name)
				print('You amount now /',result)
			else:
				print('your balance is not enough to draw ')
		else:
			print('Your name is not varified')
				
		

Kbz = KBZ()
kbzpay = KBZPay(Kbz)

user = User('kyaw',19)
user2 = User('zin',20)

Kbz.create_card(user)
Kbz.create_card(user2)
#for i,j in Kbz.accounts.items():
#	print(j)

kbzpay.varify('kyaw')
kbzpay.cash_in('kyaw',20000)
kbzpay.cash_out('kyaw',12000)

kbzpay.varify('zin')
kbzpay.cash_in('zin',20000000)