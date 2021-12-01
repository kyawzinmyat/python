from abc import ABC,abstractmethod

class Atm:
	def __init__(self):
		self.set_state()
		self.set_a_cash(200000)
	
	def set_state(self,state=None):
		if state == None:
			self.state = Out()	
		else:
			self.state = state
		self.state.machine = self
		
		
	def card_in(self):
		self.state.card_in()
	def card_out(self):
		self.state.card_out()
	def varify(self):
		self.state.varify()
	def withdraw(self):
		self.state.withdraw()
	def get_a_cash(self):
		return self.a_cash
	def set_a_cash(self,cash):
		self.a_cash = cash
	
	
class State(ABC):
	def __init__(self):
		self.machine = None
		
	@abstractmethod
	def card_in(self):
		pass
	@abstractmethod
	def card_out(self):
		pass
	@abstractmethod
	def varify(self):
		pass
	@abstractmethod
	def withdraw(self):
		pass
	
class In(State):
	def card_in(self):
		print('Card is already inserted')
	def card_out(self):
		print('Card is ejected')
		self.machine.set_state(Out())
	def varify(self):
		code = int(input('Enter the code'))
		if code == 123:
			print('Wellcome !')
			self.machine.set_state(Varified())
		else:
			print('Wrong code')
			return self.varify()
			
	def withdraw(self):
		print('Varified first')
	
	
	
class Out(State):
	def card_in(self):
		print('Card is inserted')
		self.machine.set_state(In())
	def card_out(self):
		print('There is no card ')
	
	def varify(self):
		print('There is no card')
	def withdraw(self):
		print('There is no card')
		
class Varified(State):
	def card_in(self):
		print('Card is already inserted')

	def card_out(self):
		print('card is ejected ')
		self.machine.set_state(Out())
		
	def varify(self):
		print('Already varified')
		
	def withdraw(self):
		amount = int(input('Enter the amount u want to withdraw'))
		a_cash = self.machine.get_a_cash()
		if a_cash >= amount:
			print('You withdrawed the amount /',amount)
			self.machine.set_a_cash(a_cash-amount)
		elif a_cash !=0:
			print('Sorry ,We dont have enough cash to withdraw')
		else:
			self.machine.set_state(Out_of_Cash())
			
		
		
class Out_of_Cash(State):
	def card_in(self):
		print('Card is inserted')
		self.machine.set_state(In())
	def card_out(self):
		print('Card is ejected ')
		self.machine.set_state(Out())
	def varify(self):
		print('Sorry We are out of cash')
	def withdraw(self):
		print('Sorry We are out of cash(')
			
		
atm = Atm()

atm.card_in()
atm.varify()
atm.withdraw()
#atm.card_in()
#atm.card_out()
#atm.card_out()
atm.withdraw()
atm.withdraw()
#print(atm.get_a_cash())