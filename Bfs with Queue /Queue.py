



from collections import deque

class Queue(deque):
	def __init__(self):
		super().__init__()
		
	def append(self,list_of_itmes):
		for item in list_of_itmes:
			super().append(item)
		
