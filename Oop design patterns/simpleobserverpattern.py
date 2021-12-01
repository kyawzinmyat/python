class Publisher:
	def __init__(self):
		self.subscribers = set()

	def register(self,who):
		self.subscribers.add(who)	
	
	def dispatch(self,message):
		for subscriber in self.subscribers:
			subscriber.update(message)
			
class Subscriber:
	def __init__(self,name):
		self.name = name
	
	def update(self,message):
		print(f'Got Update !',self.name,message)
		
pub = Publisher()

kyaw = Subscriber('Kyaw')
zin = Subscriber('Zin')
pub.register(kyaw)
pub.register(zin)

pub.dispatch('hello world')



class Person:
	def __init__(self,name):
		self.name = name
	def update(self):
		print('its me')
kyaw  = Person('kyaw')
h = getattr(kyaw,'update')
h()