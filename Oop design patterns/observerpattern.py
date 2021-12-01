from abc import ABC,abstractmethod

## observable interface
class Casino(ABC):
	@abstractmethod
	def open_time(self):
		pass
	
	@abstractmethod
	def close_time(self):
		pass
		
	@abstractmethod
	def add_member(self):
		pass
	

	

## observers interface
class MemberShip(ABC):
	@abstractmethod
	def get_my_data(self,name):
		pass
		
		
							
class MemberShipFee:
	def __init__(self):
		self.membership_fee ={}
		
	def add_new_catageory(self,name,fee):	
		self.membership_fee[name]= fee
		
	def change_fee(self,name,new_fee):
		self.membership_fee[name]= fee
	
	def remove_catageory(self,name):
			self.membership_fee.pop(name)
		
	def get_chart(self):
			return self.membership_fee
			
						
### concret obervable


class GJ(Casino):

	def __init__(self):
		self.members={}
		self.updates=[]
	#	self.update = Update()
		
		
	def open_time(self,time):
		return f'casino open at {time} am'
		
	def close_time(self,time):
		return f'casino close at {time} pm'
		
	def add_member(self,name,age):
		if check_age_18(age):
			self.members[name]='normal member'
			
			
	def upgrade_membership(self,MemberShipFee,catageory,fee,name):
		chart =	MemberShipFee.get_chart()
		if chart[catageory] <= fee:
			if name in self.members:
				self.members[name]= catageory
			else:
				return f'please register first'
		else:
			return f'dont enough momey'
			
		
							
					
	def get_data(self,name):
		return self.members[name]
	
class Member(MemberShip):
	def __init__(self,observable):
		self.obs = observable
	def get_my_data(self,name):
		return self.obs.get_data(name)
	def new_update(self,fun):
		return self.obs.update(fun)
		

				
def check_age_18(age):
	if age>18:
		return True
	else:
		return False
		
gj = GJ()
gj.add_member('kyaw',20)

membership = MemberShipFee()
membership.add_new_catageory('Vip',10000)

membership.add_new_catageory('VVip',20000)
#print(membership.get_chart())

print(gj.upgrade_membership(membership,'Vip',12000,'kyaw'))

kyaw = Member(gj)

print(kyaw.get_my_data('kyaw'))

print(gj.open_time(8))


### concret observer

