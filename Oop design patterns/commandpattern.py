from abc import ABC,abstractmethod

##evoker
class Button:
	def __init__(self,command):
		self.command = command
	def press(self):
		self.command.execute()

		
## reciver interface
class ElectronicDevice(ABC):
	@abstractmethod
	def on(self):
		pass
	@abstractmethod
	def off(self):
		pass
### reciver

class Bulb(ElectronicDevice):
	state = False
	@classmethod
	def on(cls):
		if cls.state == False:
			cls.state = True
			print('Light Bulb is at On State')
		else:
			print('Already On')
	@classmethod		
	def off(cls):
		if cls.state == True:
			cls.state = False		
			print('Light Bulb is at Off state')
		else:
			print('Already Off')
							
class Fan(ElectronicDevice):
	state = False
	@classmethod
	def on(cls):
		if cls.state == False:
			cls.state = True
			print('Fan is at On State')
		else:
			print('Already On')
	@classmethod		
	def off(cls):
		if cls.state == True:
			cls.state = False		
			print('Fan is at Off state')
		else:
			print('Already Off')				
								
												

#### command interface
class ICommand(ABC):
	@abstractmethod
	def execute(self):
		pass
	@abstractmethod
	def unexecute(self):
		pass
## concret commend
class OnCommand(ICommand):
	def __init__(self,device:ElectronicDevice):
		self.device = device
	def execute(self):
		self.device.on()
	def unexecute(self):
		pass
		
class OffCommand(ICommand):
	def __init__(self,device:ElectronicDevice):
		self.device = device
	def execute(self):
		self.device.off()
	def unexecute(self):
		pass
		
class BulbRemote:
	@classmethod
	def get_device(cls):
		return Bulb()
		
class FanRemote:
	@classmethod
	def get_device(cls):
		return Fan()		
		
def presson(remote):
	for i in remote:
		device = i.get_device()
		on = OnCommand(device)
		on_buttom = Button(on)
		on_buttom.press()
	
	
def pressoff(remote):
	for i in remote:
		device = i.get_device()
		on = OffCommand(device)
		on_buttom = Button(on)
		on_buttom.press()	

	
		
bulb = BulbRemote()	
fan = FanRemote()
device =[bulb]
devices =[bulb,fan]
presson(device)
pressoff(device)

	


