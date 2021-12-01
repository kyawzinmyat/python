from abc import ABC,abstractmethod

class TypeC:
	def type_c_charging(self):
		print('Charging with type C')



class Adapter(TypeC):
	def __init__(self):
		self.charger = TypeA()
		
	def type_c_charging(self):
		self.charger.type_a_charging()
	
		

		
						
class TypeA:
	def type_a_charging(self):
		print('Charging with type A')


a = Adapter()
a.type_c_charging()