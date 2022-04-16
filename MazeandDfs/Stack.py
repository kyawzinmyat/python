class Stack:
	def __init__(self):
		self.stack = []
		
	def add(self,thing):
		self.stack.append(thing)
	
	def pop_left(self):
		return self.stack.pop()
	
	def print(self):
		for i in reversed(self.stack):
			print(i)
			
	
			
#		
#		
#st1 = Stack()
#st1.add(4)
#st1.add(3)kb
#st1.print()egmzqq¹d

#print(st1.pop_left())
#st1.print()