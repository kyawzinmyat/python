from abc import ABC,abstractmethod

class Desktop(ABC):
	@abstractmethod
	def open_exe(self):
		pass
		
class Laptop(Desktop):
	def open_exe(self):
		print('Opening Exe')
	def __str__(self):
		print('Running On Laptop')

	
			
class Phone(ABC):
	@abstractmethod
	def open_app(self):
		pass
		
	
class Android(Phone):
	def open_app(self):
		print('Opening an app')
		
class DesktopAdapter(Laptop):
	def __init__(self,device:Desktop):
		self.device = device
	
	def open_exe(self):
		print(self.device.open_app())
		super(). __str__()
		

a = DesktopAdapter(Android())	
a.open_exe()