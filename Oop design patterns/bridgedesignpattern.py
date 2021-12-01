from abc import ABC,abstractmethod

class TV(ABC):
	@abstractmethod
	def open(self):
		pass
	@abstractmethod
	def close(self):
		pass
		
class Remote(ABC):
	def __init__(self,device):
		self.device = device
	
	def buttom_1(self):
		self.device.open()
	def buttom_2(self):
		self.device.close()
	
	@abstractmethod
	def buttom_5(self):
		pass
		
		
class SonyTV(TV):
	def __init__(self):
		self.name = 'Sony'
		
	def open(self):
		print('Sony Tv is turned on ')
				
	def close(self):
		print('Sony Tv is turned off')
		
		
class SamsungTV(TV):
	def __init__(self):
		self.name = 'Samsung'
		
	def open(self):
		print('Samsung Tv is turned on ')
				
	def close(self):
		print('Samsung Tv is turned off')		
		
class TvRemote(Remote):
					
		def buttom_5(self):
			print(self.device.name ,'Tv is Flying')
			
		
#tv = SonyTV()
tv = SamsungTV()
remote = TvRemote(tv)
remote.buttom_1()
remote.buttom_2()
remote.buttom_5()


