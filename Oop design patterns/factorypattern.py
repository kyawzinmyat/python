from abc import ABC,abstractmethod

class VideoQuality(ABC):
	@abstractmethod
	def prepare(self):
		pass
	
	@abstractmethod
	def success(self):
		pass


				
												
class Low(VideoQuality):
	def prepare(self):
		print(f'Preparing___')
	
	def success(self):
		print(f'Low video Quality is applied')
		
class Medium(VideoQuality):
	def prepare(self):
		print(f'Preparing ____')
	
	def success(self):
		print('Medium Quality is applied')
	
class High(VideoQuality):
	def prepare(self):
		print(f'Preparing ____')
		
	def success(self):
		print(f'High Video Quality is applied')
		
class FourK(VideoQuality):
	def prepare(self):
		print(f'Preparing ___')
	
	def success(self):
		print(f'4K video quality is applied')
	
class QualityFactory(ABC):
	@abstractmethod
	def check(self):
		pass
	
	@abstractmethod
	def return_quality():
		pass
	
	
class LowFactory(QualityFactory):

	def check(self):
		pass
		
	
	def return_quality(self):
		return Low()
	
class MediumFactory(QualityFactory):
	def check(self):
		pass
	
	def return_quality(self):
		return Medium()
		
class HighFactory(QualityFactory):
	
	def check(self):
		pass
	
	def return_quality(self):
		return High()
		
class FourKFactory(QualityFactory):
	
	def check(self):
		pass
	
	def return_quality(self):
		return FourK()
		
		
		
def select_quality(choice):
	map ={
		'low':LowFactory(),
		'medium':MediumFactory(),
		'high':HighFactory(),
		'4K':FourKFactory()
	}
	try:
		return map[choice]
		
	except:
		print('Invalid keyword')
	
if __name__ == "__main__" :
	while True:
		choice = input('Enter the option u want to choose')
		quality =	select_quality(choice).return_quality()
		quality.prepare()
		quality.success()

		
	