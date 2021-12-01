from abc import ABC,abstractmethod

class Gate:
	#_state = None
	def __init__(self,state):
		_state = None
		self.change(state) 
	def  change(self,state):
		self._state = state
		self._state.context = self
	def close(self):
		self._state.close()
	def open(self):
		self._state.open()
class State(ABC):
	@property
	def context(self):
		return self._context
	@context.setter
	def context(self,context):
		self._context = context
	@abstractmethod
	def close(self):
		pass
	@abstractmethod
	def open(self):
		pass	
		
class Open(State):
	def open(self):
		print('Gate is already open')
		
	def close(self):
		print('Gate is close')
		self.context.change(Close())
		
class Close(State):
	def open(self):
		print('Gate is open')
		self.context.change(Open())
		
	def close(self):
		print('Gate is already close')

		
gate = Gate(Close())
gate.close()
gate.open()
gate.close()
gate.close()
