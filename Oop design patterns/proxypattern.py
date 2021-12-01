from abc import ABC,abstractmethod


class Interface(ABC):
	def request(self):
		pass
	
class Server(Interface):
	def __init__(self):
		self.server = 'Kyawlay'
	
	def request(self):
		print('Server name /',self.server)
		print('Server Responsed / Hello world')
		
class Proxy(Interface):
	instance = None
	def __init__(self):
		if Proxy.instance == None :
			Proxy.instance = Server()	
		
	def request(self):
		if self.instance:
			self.instance.request()
		else:
			print('Server not found')

		


p = Proxy()
j = Proxy()
p.request()
j.request()
		
	
	