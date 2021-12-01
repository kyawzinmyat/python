class cpu:
	def __init__(self,name,gen):
		self.name = name
		self.gen = gen
	def show(self,price):
		return self.name,self.gen,price
		
class laptop(cpu):
		def __init__(self,brandname,model):
			cpu . __init__(self,name,gen)
			self.brandname = brandname
			self.model = model
			
		
		
		

asus = laptop("Asus","M5334ia")
