class Publisher:
	def __init__(self):
		self.subscribers = dict()

	def register(self,who,fun=None):
		if fun is None:
			fun = getattr(who,'update')
		self.subscribers[who]=fun
	
	def dispatch(self,message):
		for subscriber,fun in self.subscribers.items():
			fun(message)
			
class SubscriberOne:
	def __init__(self,name):
		self.name = name
	
	def update(self,message):
		print(f'Got Update !',self.name,message)
		
class SubscriberTwo:
	def __init__(self,name):
		self.name = name
	
	def receive(self,message):
		print(f'Got update by receive method !',self.name,message)
		
pub = Publisher()

kyaw = SubscriberOne('Kyaw',)
zin = SubscriberTwo('Zin')
pub.register(kyaw,kyaw.update)
pub.register(zin,zin.receive)

pub.dispatch('hello world')

