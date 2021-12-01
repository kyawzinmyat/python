from abc import ABC,abstractmethod

class UniMajor(ABC):
	@abstractmethod
	def __init__(self,teachers):
		self._teachers = teachers
	@abstractmethod
	def get_major(self):
		pass
	
class Math(UniMajor):
	def __init__(self,teachers):
		self._teachers = teachers
	def get_major(self):
		return f'Major / Math'	
		
	@property
	def teachers(self):
		return self._teachers
	
class English(UniMajor):
	def __init__(self,teachers):
		 self._teachers = teachers
		
	def get_major(self):
		return f'Major / English'
		
	@property
	def teachers(self):
		return self._teachers
		
class Science(UniMajor):
	def __init__(self,teachers):
		 self._teachers = teachers
		
	def get_major(self):
		return f'Major / Science'
		
	@property
	def teachers(self):
		return self._teachers
		
		
class Cs(UniMajor):
	def __init__(self,teachers):
		self.teachers = teachers
		self._base_teachers = teachers
		self.majors = []
		
	def get_major(self):
		print(f'Major / Computet Science')
		for major in self.majors:
			print(f'Minor / {major.get_major()}')	
					
	def add_major(self,major):
		self.majors.append(major)
		

	def total_teachers(self):
		for major in self.majors:
			self.teachers += major.teachers
		print(f'Total teachers / {self.teachers}')
		
	def base_teachers(self):
		print(f'Base Teachers/ {self._base_teachers}')
		
class Bcs(UniMajor):
	def __init__(self,teachers):
		self.teachers = teachers
		self._base_teachers = teachers
		self.majors = []
		
	def get_major(self):
		print(f'Major /Bachelor Computet Science')
		for major in self.majors:
			print(f'Minor / {major.get_major()}')	
					
	def add_major(self,major):
		self.majors.append(major)
		

	def total_teachers(self):
		for major in self.majors:
			self.teachers += major.teachers
		print(f'Total teachers / {self.teachers}')
		
	def base_teachers(self):
		print(f'Base Teachers/ {self._base_teachers}')
			

class Physics(UniMajor):
	def __init__(self,teachers):
		self.teachers = teachers
		self._base_teachers = teachers
		self.majors = []
		
	def get_major(self):
		print(f'Major / Physics Science')
		for major in self.majors:
			print(f'Minor / {major.get_major()}')	
					
	def add_major(self,major):
		self.majors.append(major)
		

	def total_teachers(self):
		for major in self.majors:
			self.teachers += major.teachers
		print(f'Total teachers / {self.teachers}')
		
	def base_teachers(self):
		print(f'Base Teachers/ {self._base_teachers}')		
				
						
										
math = Math(5)
eng = English(7)
cs = Cs(7)
cs.add_major(math)
cs.add_major(eng)
#cs.get_major()
cs.total_teachers()
##cs.base_teachers()
bcs = Bcs(4)
bcs.add_major(cs)
#print(bcs.total_teachers())
#bcs.get_major()
sci= Science(3)
phy = Physics(7)
phy.add_major(math)
phy.add_major(sci)
phy.get_major()






class Test(ABC):
	def greet(self):
		print('Hello')
	
class Hello(Test):
	pass
	
h = Hello()
h.greet()