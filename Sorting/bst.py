import math

class Node:
	def __init__(self,value):
		self.value = value
		self.lc = None
		self.rc = None


class Bst:
	def __init__(self):
		self.root = None
		
	def add(self,value):
		if self.root == None:
			self.root = Node(value)
		else:
			self._insert(value,self.root)
			
	def _insert(self,value,cur_node):
		if value > cur_node.value:
			if cur_node.rc != None:
				self._insert(value,cur_node.rc)
			else:
				cur_node.rc = Node(value)
		else:
			if cur_node.lc != None:
				self._insert(value,cur_node.lc)
			else:
				cur_node.lc = Node(value)
				
	def search(self,value):
		if self.root != None:
			if value != self.root.value:
				print('current node is ',self.root.value)
				if value>self.root.value:
					return self._search(value,self.root.rc)
				else:
					return self._search(value,self.root.lc)
			else:
				return self.root.value
		else:
			print('False')
			


	def _search(self,value,cur_node):
			if value > cur_node.value:
				print('current node is',cur_node.value)
				if cur_node.rc:
					return self._search(value,cur_node.rc)
				else:
					return cur_node.value
			else:
				print('current node is',cur_node.value)
				if cur_node.lc:
					return self._search(value,cur_node.lc)
				else:
					return cur_node.value
					
					
	def inorder(self,root):
	
		if root != None:
			if root.lc != None:
				self.inorder(root.lc)
				print(root.value)
				if root.rc != None:
					self.inorder(root.rc)

			else:
					print(root.value)
					if root.rc != None:
						self.inorder(root.rc)
						
						
	def inorder_2(self,root):
		if root != None:
			self.inorder_2(root.lc)
			print(root.value)
			self.inorder_2(root.rc)
		
		
		
	def get_first(self):
		if self.root != None:
			return self._get_first(self.root)
		return None
			
			
	def _get_first(self,node):
		if node.lc != None:
			return self._get_first(node.lc)
		else:
			return node.value
			
	def get_last(self):
		if self.root != None:
			return self._get_last(self.root)
		return None
	
	def _get_last(self,node):
		if node.rc != None:
			return self._get_last(node.rc)
		return node.value
		
	
	
	
b = Bst()
b.add(7)
#print(b.add(2))
b.add(9)
b.add(5)
b.add(11)
b.add(4)
b.add(6)
b.add(8)

b.inorder(b.root)

#print(b.search(4))
#b.inorder_2(b.root)
#print(b.get_first())
#print(b.get_last())


	
