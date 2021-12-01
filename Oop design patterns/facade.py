class Member:

	members ={}
	@classmethod
	def add_member(cls,name):
			cls.members[name]='Normal'
			
	
class CheckMem:
	def check_mem(name,member):
		if name in member:
			return True
		else:
			return False

class CheckAmount:
		fee = 12000
		def check_payment(self,amount):
			if amount >= self.fee:
				return True
			else:
				return False
				
		




class ClubFacade:
	
	def __init__(self,name,amount):
		self.name = name
		self.amount = amount
		members = Member()
		check_mem_ = CheckMem()
		check_amount = CheckAmount()
		if check_mem_.check_mem != True:	
			if check_amount.check_payment(self.amount):
			  
			  members.add_member(name)
			  print('Subscribed !',self.name)
			else:
				print('Not Enough Money')
		else:
			print('You\'re already suscribed' )
	

	
ClubFacade('kyaw',1200)		
				