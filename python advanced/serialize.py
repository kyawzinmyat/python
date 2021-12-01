import pickle

class Person:
	def __init__(self,name,age,info):
		self.name = name
		self.age = age
		self.info = info
	def display(self):
		print(f'{self.name} is a {self.age} years old person')
		for item,key in self.info.items():
			print(f'{item}={key}')
			
			
info =dict(sex='male',major="Cs")			
kyaw = Person('Kyaw',18,info)
kyaw.display()

ps = pickle.dumps(kyaw)
print(int('y'))

psc = pickle.loads(ps)
psc.display()