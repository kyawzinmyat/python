class Node:
	def __init__(self,value):
		self.value = value
		self.left_child = None
		self.right_child = None
		self.parent = None
		self.height = 0
		
class Bst:
		def __init__(self):
			self.root = None
		
		def insert(self,node):
			if self.root == None:
				self.root = Node(node)
			else:
				self._insert(self.root,node)
				
		def _insert(self,cur_node,node):
				if node >= cur_node.value:
					if cur_node.right_child:
						self._insert(cur_node.right_child,node)
					else:
						cur_node.right_child = Node(node)
						cur_node.right_child.parent = cur_node
						com = 'right'
						self.height_change(cur_node.right_child,com)
						self.parent(cur_node.right_child)
				else:
					if cur_node.left_child:
						self._insert(cur_node.left_child,node)

					else:
						cur_node.left_child = Node(node)
						cur_node.left_child.parent = cur_node
						com = 'left'
						self.height_change(cur_node.left_child,com)
						self.parent(cur_node.left_child)
		
		
		def parent(self,parent):
			if parent:
				if self.screw(parent) == 0 or self.screw(parent) ==1 or self.screw(parent)==-1:
					self.parent(parent.parent)
				elif self.screw(parent) >=2:
					if self.screw(parent.right_child)>=0:
						self.left_rotate(parent)
					elif self.screw(parent.right_child)== -1:
						self.right_rotate(parent.right_child)
						self.left_rotate(parent)
				#		self.inorder(self.root)
				elif self.screw(parent) >= -2:
					if self.screw(parent.left_child)<=0:
						self.right_rotate(parent)
					elif self.screw(parent.left_child) == 1:
						self.left_rotate(parent.left_child)
						self.right_rotate(parent)
						
				
		
		def inorder(self,root):
			if root != None:
				self.inorder(root.left_child)
				print(root.value)
				self.inorder(root.right_child)
				
		
								
		def search(self,value):
			if self.root != None:
				if value != self.root.value:
					if value>self.root.value:
						return self._search(value,self.root.right_child)
					else:
						return self._search(value,self.root.left_child)
				else:
					return self.root
			


		def _search(self,value,cur_node):
				if value == cur_node.value:
					return cur_node
				elif value > cur_node.value:
					if cur_node.right_child:
						return self._search(value,cur_node.right_child)

				elif value < cur_node.value:
					if cur_node.left_child:
						return self._search(value,cur_node.left_child)
							
								
		def succesor(self,node):
			temp = self.search(node)
			if temp:
				if temp.right_child:
					return temp.right_child.value				
				else:
					return self.go_up(temp.parent,temp)
						
								
		def go_up(self,parent,cur):
			if parent.left_child:
				if parent.left_child.value == cur.value:
					return parent.value
			else:
				return self.go_up(parent.parent,parent)
			
		def height(self,node):
			if node:
					h = 1+max(self.height(node.left_child),self.height(node.right_child))
					node.height= h
					
					return node.height
			else:
					return 0
					
		def height_change(self,node,com):
			if node:
				node.height=1
				if com == 'right':
					if node.parent.left_child:
						pass
					else:
						self._height_change(node.parent)
				else:
					if not node.parent.right_child:
						self._height_change(node.parent)
		
								
		def _height_change(self,node):
			if node:
				node.height += 1
				self._height_change(node.parent)
			
			
			
			
		def screw(self,node):
			right = self.height(node.right_child)
			left = self.height(node.left_child)
			res = right - left
			return res
			
	
			
		def left_rotate(self,node):
			is_parent = False
			parent = ''
			if node.parent:
				is_parent = True
				parent = node.parent
				
			node.parent = node.right_child
			node.right_child= node.parent.left_child
			if node.right_child:
				node.right_child.parent= node
			node.parent.left_child = node
			if not is_parent:			
				node.parent.parent = None
				self.root = node.parent
				
			else:
				if node.parent.value >= parent.value:
					parent.right_child = node.parent
				else:
					parent.left_child = node.parent

			self.height(self.root)
			
		def right_rotate(self,node):
			is_parent = False
			parent = ''
			if node.parent:
				is_parent = True
				parent = node.parent
				
			node.parent = node.left_child
			node.left_child= node.parent.right_child
			if node.left_child:
				node.left_child.parent= node
			node.parent.right_child = node
			if not is_parent:			
				node.parent.parent = None
				self.root = node.parent	
				
			else:
				node.parent.parent = parent
				if node.parent.value >= parent.value:
					parent.right_child = node.parent
				else:
					parent.left_child = node.parent
		#	self.inorder(self.root)
			self.height(self.root)
			
					
b = Bst()
b.insert(6)
b.insert(3)
b.insert(7)
b.insert(2)
b.insert(4)
b.insert(5)
#b.insert(7)
#b.insert(8)
#b.insert(1)
#b.insert(2.5)
#b.insert(9)
#b.insert(6)
#b.insert(8)
#b.insert(9)
#print(b.root.left_child.value)
#b.inorder(b.root)		
j=b.succesor(3)
#print(j)	
#print(b.height(b.root))	
#print(b.screw(b.root))	
#print(b.search().height)							
#print(b.screw(b.root))			
#b.left_rotate(b.root.right_child.right_child)	
#print(b.root.value)
b.inorder(b.root)				
#print(b.root.right_child.right_child.value)	
#print(b.height(b.root))
print(b.screw(b.root.right_child))	

			
		