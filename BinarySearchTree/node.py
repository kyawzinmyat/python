

class Node:
	def __init__(self,value):
		self.value=value
		self.right_child =None
		self.left_child=None
		self.parent = None
		self.height=0
		self.depth=0
		
		
		

	def get_value(self):
		return self.value
		
	def set_value(self,new_value):
		self.value = new_value

	def set_left_child(self,left_child_node):
		self.left_child=left_child_node


	def get_left_child(self):
		return self.left_child
	

	def set_right_child(self,right_child_node):
		self.right_child=right_child_node
		

	def get_right_child(self):
		return self.right_child
		
	def get_parent(self):
		return self.parent
	
	def set_parent(self,parent_node):
		self.parent= parent_node
		
	
	
	
