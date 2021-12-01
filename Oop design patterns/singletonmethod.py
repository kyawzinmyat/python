class SingleTonPerson:
	__instance = None
	
	@classmethod
	def get_instance(cls):
		if not cls.__instance:
			cls('default')		 
		return cls.__instance.name
	
	def __init__(self,name):
			if not self.__instance:
				self.name = name
				SingleTonPerson.__instance = self
			else:
				raise Exception('Cant instanciate more than once')

	@classmethod
	def get_data(cls):
			print(SingleTonPerson.__instance.name)

			
#print(SingleTonPerson.get_instance())	
p1 = SingleTonPerson('Kyaw')		
p = SingleTonPerson.get_instance()
print(p)
p1 = SingleTonPerson.get_data()
#print(p2)
#p2 = SingleTonPerson.get_data()


