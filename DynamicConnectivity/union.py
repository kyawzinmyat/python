from plot import Plot


class Union:
	def __init__(self,size):
		self.size= size
		self.init_array()
		
		
	
		
	def init_array(self):
		self.array =[z for z in range(self.size)]
		self.parent_array=[x for x in range(self.size)]
	
		
	## only work for union	
	def isConnected(self,first_index,second_index):
		return self.array[first_index]==self.array[second_index]
		
	
		
	def union(self,first_index,second_index):
		temp = self.array[first_index]
		for index,mark in enumerate(self.array):
			if mark==temp:
				self.array[index]=second_index
				
	def plot(self):
		self.plot = Plot()
		self.add_nodes()
		self.add_edge()
		
		
	def add_nodes(self):
		nodes =[num for num in range(self.size)]
		self.plot.add_nodes(nodes)
		self.add_edge()
		self.plot.save_file("dynamic_connectivity")
	
	def add_edge(self):
		for index,edge in enumerate(self.array):
			if index!= edge:
				self.plot.add_edge(index,edge)
		

		
	
		
	def find_root(self,index):
		while index!= self.array[index]:
			index = self.array[index]
		return index
			
	def is_connected_qu(self,first_index,second_index):
		return self.find_root(first_index) == self.find_root(second_index)
			
														
	def quick_union(self,first_index,second_index):
		if not self.is_connected_qu(first_index,second_index):
			first_index_root = self.find_root(first_index)
			second_index_root=self.find_root(second_index)
			self.parent_array[first_index_root]=second_index_root
		

	def print(self):
		print(self.array)
			
