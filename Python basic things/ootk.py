
# course  instance,class,static variable,class,static method
class Human:
	planet = 'Earth' ##class or static variable
	def __init__(self,name,age):
		self._name = name
		self._age = age
		
	def show(self):
		print(self.planet)## look for instance if dont it'll use class variable
	##
	### setter getter
	
	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self,age):
		if  0<age<100:
			self._age = age
			
		
	def set(self,m):
		self.planet=m
		
		
	@staticmethod
	def static():
		print(Human.planet)
		
	@classmethod
	def class_m(cls):
		print(cls)
		
h1 = Human("Kuaw",18)
h1._name ='Kysw'
h1.age=101
print(h1.age)
#h2 = Human('Zun')
#print(h1.__dict__)
#h1.show()
#h1.set('Mars')
#h1.show()
#print(h1.__dict__)
#h1.class_m()
#h1.planet = 'Mars'
#h1.show()
##print(h2.planet)
##print(Human.planet)
#h1.static()


### cannot delete class var from object try below code only delete if u use set method above instead use class name to delete
#h1.set('Mars')
#del h1.planet
#del Human.planet
import string
import random
#print(dir(string))
#random.random()
choices = string.digits
lst=""

for i in range(0,5):
	
	if random.random()>0.3:
		lst = lst+random.choice(string.ascii_letters)
	else:
		lst =lst+random.choice(choices)
	
#print(lst)

def fib():
	x,y=1,1	
	while True:
		yield x
		x,y =y,x+y



#		print(i)


def fib_1():
	x,y = 1,1
	lst=[]
	def fib():
		nonlocal x,y
		lst.append(x)
		x,y=y,y+x
		return lst
	return fib

		
f = fib_1()	
#for i in range(10):
	#	print(f())


#### closure
def test():
		i=1
		def inner():
			nonlocal i
			i+= 1
			return i
		return inner
		
b = test()
#print(b())
#print(b())
		

### duck and sub typing
### reverse control

### super
class M1:
	ini_value = 1
	def __init__(self):
		self.value = 1
	
	def method(self):
		print('instance method in M1')
	
	@staticmethod
	def static():
		print(f'static method called')
	@classmethod
	def class_method(cls):
		print(f'class method called')

class M0:
	ini_value = 2
	def __init__(self):
		pass
	
	def method(self):
		print('instance method in M2')
			
				
								
class M2(M0,M1):
		def __init__(self):
				pass
				
		def test(self):
			super().method()
			M1.method(self)##same as above according to mrm ,method fun will be executed first at M0 if u want to call M1 method use this notion 
			print(super().ini_value)
		#	print(super().value)  canot access imstance var

m1 = M2()
m1.test()
			
				
##### polymorph

### in static lg in order to use polymorph,u need to use inheritance,
### in dynamic lg u dont need to inheritance bcz of duck typing

class Human:
	def __init__(self,name):
		self.name = name
	
	def work(self):
		print('Human Work')
	
class Programmer(Human):
	def __init__(self,name):
		self.name = name
		
	def work(self):
		print('programmer code')
	
kyaw = Programmer('kyaw')
h = Human(kyaw)
print(h.work())
	


## operator overloading
###
class Money:
	def __init__(self,value):
		self.value = value
		
	def __add__(self,other):
		return Money(self.value+other.value)


m1 = Money(2)
m2 = Money(3)
m = m1 + m2
print(m.value)		

		
m = 1
m= 3 ## overwrite in static lg is overloading 
m='three'	## overwrite
		
### overiding
class Human:
	def __init__(self):
		pass
	def work(self):
		print('Human work')
	
class Doctor(Human):
	def __init__(self):
		pass
	def work(self):
		super().work()
		print('Doctor Work ')##c overriding
		
kyaw = Doctor()
kyaw.work()

## abstract class is template for child classes in static lg if a class is inherit from abstract class u dont neet to make object for abstract but need to have same method from abc class in child class

## in dp
from abc import *
class Abstract(ABC):
	def __init__(self):
		pass
	@abstractmethod	
	def work(self):
		pass
		
class Child(Abstract):
	def __init__(self):
		pass
	def work(self):## if u dont put abstract method from parent(abstract class),it's gonna raise error
		print('work')
	
## a = Abstract()	# try this 
h = Child()
h.work()