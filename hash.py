class Hash:
	def __init__(self):
		self.size = 1
		self.table = [[] for i in range(self.size)]
		
	def hash_division(self,key):
		return key%self.size
		
	def add(self,key):
		temp = self.hash_division(key)
		if self.check():
			self.table[temp]=[key]
		else:
			self.double()
			self.table[temp]=[key]
			
		
		
	def check(self):
		if self.size > len(self.table):
			return True
		else:
			return False
		
	def double(self):
		
		temp = self.table
		self.size = self.size * 2
		self.table = [[]for i in range(self.size)]
		j=0
		for i in temp:
			self.table[j]=i
			j+=1
			
			
	def show(self):
			print(self.table)
			
h1 = Hash()
h1.add(1)
h1.add(3)
h1.add(7)
h1.show()