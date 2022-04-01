

class Node:
	
	def __init__(self,value,left_child,right_child,parent):
		self._value= value
		self._left_child=left_child
		self._right_child = right_child
		self._parent=parent
	
	def value(self,newValue):
		self.valu
	
	@property	
	def value(self):
		return self._value
		
		
class Bst:
	
	def __init__(this,root_node:Node):
		this.root_node = root_node
		
	def setRootNode(this,new_Root_Node):
		if not this.root_node:
			this.root_node = new_Root_Node
		
		
		
		
		
	
node1 = Node(1,2,3,4)
print(node1.value)
node2 = Node(2,3,4,5)
tree = Bst(node1)
tree.setRootNode(node2)