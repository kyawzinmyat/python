
from node import Node

class Bst:
	
	def __init__(self):
		self.root=None
		
#####################	
	
	def add(self,node_to_add):
		self.decide_left_right(self.root,node_to_add)
	
	def decide_left_right(self,current_node,node_to_add):
		if current_node.get_value()>node_to_add:
			self.go_left_or_create_node(current_node,node_to_add)
		else:
			self.go_right_or_create_node(current_node,node_to_add)
			current_node.get_right_child().set_parent(current_node)
			
	
	
	def go_left_or_create_node(self,current_node,node_to_add):
		if current_node.get_left_child():
			return self.decide_left_right(current_node.get_left_child(),node_to_add)
		current_node.set_left_child(Node(node_to_add))
		current_node.get_left_child().set_parent(current_node)
		
		
		
	
	def go_right_or_create_node(self,current_node,node_to_add):
		if current_node.get_right_child():
			return self.decide_left_right(current_node.get_right_child(),node_to_add)
		current_node.set_right_child(Node(node_to_add))
		current_node.get_right_child().set_parent(current_node)
		
		
# for creation of node
######################		
					
			
				
	
	def inorder(self,data):
		if isinstance(data,Node):
			return self._inorder(data)
		return self._inorder(self.get_node(data))
		
		
	def _inorder(self,root_node):
		if root_node:
			self._inorder(root_node.get_left_child())
			print(root_node.get_value())
			self._inorder(root_node.get_right_child())
			
			
		
			
	# return the first node(in order traversal) of subtree rooted with given node	
	def subtree_first(self,node):
		if node.get_left_child():
			return self.subtree_first(node.get_left_child())
		return node
	
	def subtree_last(self,node):
		if node.get_right_child():
			return self.subtree_last(node.get_right_child())
		return node
		
	
#####################
	def find(self,data):
		if isinstance(data,Node):
			return self.get_node(data.get_value())
		return self.get_node(data)
		
		
						
	def get_node(self,value):
		if self.root.get_value()==value:
			return self.root
			
		elif self.root.get_value()>value:
			return self._get_node(self.root.get_left_child(),value)
	
		return self._get_node(self.root.get_right_child(),value)
			
			
	def _get_node(self,current_node,value):
		if current_node:
			if current_node.get_value()==value:
				return current_node
			
			elif current_node.get_value()>value:
				return self._get_node(current_node.get_left_child(),value)
			
			return self._get_node(current_node.get_right_child(),value)
			
			
	
			
		
#####################					
	def succesor_of(self,node):
		if node.get_right_child():
			return self.subtree_first(node.get_right_child())
		return self.go_up_for_succesor(node)
	
	def predecessor_of(self,node):
		if node.get_left_child():
			return self.subtree_last(node.get_left_child())
		return self.go_up_for_predecessor(node)
			
	
	def go_up_for_succesor(self,current_node):
		if current_node.get_value() > current_node.get_parent().get_value():
			return self.go_up_for_succesor(current_node.get_parent())
		return current_node.get_parent()
	
	def go_up_for_predecessor(self,current_node):
		if current_node.get_value() < current_node.get_parent().get_value():
			return self.go_up_for_predecessor(current_node.get_parent())
		return current_node.get_parent()
	

		
	def insert_after(self,node,node_to_add):
		if not node.get_right_child():
			return self.go_right_or_create_node(node,node_to_add)
		return self.go_left_or_create_node(self.succesor_of(node),node_to_add)
		
		
######################
	def swap(self,first_node,second_node):
		first_node_value=first_node.get_value()
		first_node.set_value(second_node.get_value())
		second_node.set_value(first_node_value)
	
	def delete(self,data_to_delete):
		if isinstance(data_to_delete,Node):
			return self._delete(data_to_delete)
		return self._delete(self.get_node(data_to_delete))
				
			
	def _delete(self,node_to_delete):
		if node_to_delete.get_left_child():
			self.swap(node_to_delete,self.predecessor_of(node_to_delete))
			return self._delete(self.predecessor_of(node_to_delete))
		elif node_to_delete.get_right_child():
			self.swap(node_to_delete,self.succesor_of(node_to_delete))
			return self._delete(self.succesor_of(node_to_delete))
		else:
			self.call_leaf_case(node_to_delete)
			
	def call_leaf_case(self,node_to_delete):
			parent= node_to_delete.get_parent()
			if parent.get_left_child():
				if parent.get_left_child().get_value()==node_to_delete.get_value():
					parent.set_left_child(None)
			else:
				parent.set_right_child(None)	
			del node_to_delete
			
	
			
		
		
		
	
				
		
	def set_root(self,value):
		if not self.root:
			self.root = Node(value)

			
						
												
			
			
					