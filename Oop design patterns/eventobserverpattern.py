class Publisher:
	def __init__(self,events):
		self.subscribers = {
			event:dict() for event in events
		}

	def register(self,who,event,fun=None):
		if fun is None:
			fun = getattr(who,'update')
		self.subscribers[event][who]=fun
			
	def get_subscribers(self,event):
		return self.subscribers[event]
	
	def dispatch(self,message,event):
		for sub,method in self.get_subscribers(event).items():
			method(message)
			
class Subscriber:
	def __init__(self,name):
		self.name = name
	
	def update(self,message):
		print(f'Got Update !',self.name,message)
		
pub = Publisher(['lunch','dinner'])

kyaw = Subscriber('Kyaw')
zin = Subscriber('Zin')
pub.register(kyaw,'dinner')
pub.register(zin,'dinner')

pub.dispatch('its dinner time','dinner')