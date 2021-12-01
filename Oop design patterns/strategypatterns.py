
#class Car(ABC):
#	@abstractmethod
#	def start(self):
#		pass
	
##	@abstractmethod
#	def stop(self):
#		pass
## concret class
	
class Telsa:
	def __init__(self,engine):
		self.engine = engine
			
	def start(self):
		print(self.engine.type,'start')
		print('the car is open')
		
	def stop(self):
		print('engine stop')
		print('the car is stop')
		
class ElectricEngine:
	def __init__(self):
		self.type = 'Electric Engine'

# startegies	
class DiselEngine:
	def __init__(self):
		self.type = 'Disel Engine '
		
disel_engine = DiselEngine()
electric_engine = ElectricEngine()
telsa = Telsa(electric_engine)
telsa.start()