class Node:
	def __init__(self,value):
		self.value = value
		self.lc = None
		self.rc = None
		self.parent = None


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
				cur_node.rc.parent = cur_node
		else:
			if cur_node.lc != None:
				self._insert(value,cur_node.lc)
			else:
				cur_node.lc = Node(value)
				cur_node.lc.parent= cur_node
				
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
				print('current node is',cur_node.value,'parent',cur_node.parent.value)
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
			return node
			
	def get_last(self):
		if self.root != None:
			return self._get_last(self.root)
		return None
	
	def _get_last(self,node):
		if node.rc != None:
			return self._get_last(node.rc)
		return node.value
		
	
	
	def succesor(self,value):
		if self.root != None:
			if value != self.root.value:
	
				if value>self.root.value:
					return self._search1(value,self.root.rc)
				else:
					return self._search1(value,self.root.lc)
			else:
				return self.root.value
		else:
			print('False')
			


	def _search1(self,value,cur_node):
			if value > cur_node.value:
				if cur_node.rc:
					return self._search1(value,cur_node.rc)
				else:
					return cur_node.parent.value
			elif value == cur_node.value:
				if cur_node.rc:
					return cur_node.rc.value
				else:
					return self.go_up(cur_node.parent,cur_node)
			else:
				if cur_node.lc:
					return self._search1(value,cur_node.lc)
				else:
					return cur_node.parent.value
	
	def go_up(self,parent,cur):
		if parent.lc:
			if parent.lc.value == cur.value:
				return parent.value
		else:
			return self.go_up(parent.parent,parent)
			
	def search_for_insert_after(self,value,new_node):
		if self.root != None:
			if value != self.root.value:
	
				if value>self.root.value:
					return self._search2(value,self.root.rc,new_node)
				else:
					return self._search2(value,self.root.lc,new_node)
			else:
				return self.root.value
		else:
			print('False')	
	def _search2(self,value,cur_node,new_node):
			if value > cur_node.value:
				if cur_node.rc:
					return self._search2(value,cur_node.rc,new_node)
				else:
					return cur_node.parent.value
			elif value == cur_node.value:
				if cur_node.rc:
					tmp =self._get_first(cur_node.rc)
					tmp.lc = Node(new_node)
					tmp.lc.parent = tmp
				else:
					cur_node.rc = Node(new_node)
					cur_node.rc.parent = cur_node
					
			else:
				if cur_node.lc:
					return self._search2(value,cur_node.lc,new_node)
				else:
					return cur_node.parent.value
	
	
			
	def insert_after(self,node,new_node):
		return self.search_for_insert_after(node,new_node)
	
	def search_for_insert_before(self,value,new_node):
		if self.root != None:
			if value != self.root.value:
	
				if value>self.root.value:
					return self._search3(value,self.root.rc,new_node)
				else:
					return self._search3(value,self.root.lc,new_node)
			else:
				return self.root.value
		else:
			print('False')	
			
	def _search3(self,value,cur_node,new_node):
			if value > cur_node.value:
				if cur_node.rc:
					return self._search3(value,cur_node.rc,new_node)
				else:
					return cur_node.parent.value
			elif value == cur_node.value:
				if cur_node.lc:
						tmp = self._get_first(cur_node.lc)
						tmp.rc = Node(new_node)
						tmp.rc.parent = tmp
				
				else:
					cur_node.lc = Node(new_node)
					cur_node.lc.parent = cur_node
					
			else:
				if cur_node.lc:
					return self._search3(value,cur_node.lc,new_node)
				else:
					return cur_node.parent.value	
		
	def insert_before(self,node,new_node):
		return self.search_for_insert_before(node,new_node)
		
		
	
b = Bst()
b.add(6)
b.add(7)
b.add(4)
b.add(5)
b.add(3)
b.add(2)
#b.add(1)

print(b.succesor(1))
#b.inorder_2(b.root)
#print(b.get_first())
#print(b.get_last())

#print(b.insert_after(2,1))
#b.inorder_2(b.root)
#print(b.insert_after(4,3))
#print(b.insert_before(2,1))
#b.inorder_2(b.root)
