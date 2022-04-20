class Array:
	def __init__(self):
		self.init()
		self.current_length =0
		
	def init(self):
		self.length = 8
		self.array=[None for x in range(8)]
		
	def append(self,item):
		self.array[self.current_length]=item
		self.current_length+=1
	
	def pop(self):
		temp= self.array[self.current_length-1]
		self.array[self.current_length-1]=None
		self.current_length-=1
		return temp
		
		
	
		
	def double_table(self):
		self.length*=2
		
		
	def check_size(self):
		return True if self.length >self.current_length else False
		
		
	
	
	def __repr__(self):
		return f"{self.array}"
		
		
		
n1 = Array()
n1.append(1)
n1.append(2)
print(n1.pop())
print(n1)





j=2

		