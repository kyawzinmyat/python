#### deep and shallow equality
class Person:
	name : str
	age : int
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
		
from dataclasses import dataclass,field

@dataclass(order=True,frozen=True)
class Person_:
	sort_index : int =field(init=False,repr=False)##if u dont put init=False u need create an object with one more argument
	name :str
	age : int
	strength : int = 100
	
	def __post_init__(self):
	#	self.sort_index = self.strength # bcz froze = true
		object.__setattr__(self,'sort_index',self.age)
	
p1 = Person('kyaw',18)
p2 = Person('kyaw',18)
print(p1==p2)

p3 = Person_('kyaw',19)
p4 = Person_('kyaw',18)
print(p3)
print(p3>p4)