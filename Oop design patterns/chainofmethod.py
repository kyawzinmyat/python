class End:
	def end(self):
		print('This\'s end ')



class Greet:
	def greet1(self):
		print('Hello World')
		return self
	def greet2(self):
		print('How it\'s going  ')
		return self
	def greet3(self,end:End()):
		print('Bye Bye')
		end.end()
		

g = Greet()
g.greet1().greet2().greet3(End())