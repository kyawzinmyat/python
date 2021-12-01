from abc import ABC,abstractmethod

class INode(ABC):
	@abstractmethod
	def add_adj(self):
		pass
	@abstractmethod
	def value(self):
		pass
	@abstractmethod
	def adj(self):
		pass
		
class Node(INode):
	def __init__(self,value):
		self._value = value
		self.adjs = []
	def add_adj(self,node:INode):
		self.adjs.append(node)
	@property
	def value(self):
		return self._value
	def adj(self):
		return self.adjs

class GraphTraverse:
	def __init__(self,stg):
		self.level ={}
		self.parent={}
		self.stg = stg
		
	def traverse(self):
		return self.stg.traverse()
		
		
		
class Bfs:
	def __init__(self,source):
		self.source = source
		self.level  ={}


	def traverse(self):	
		adjs = [self.source]
		i=0
		while adjs:
			next=[]
			for obj in adjs:
				if not obj in self.level:
					self.level[obj] = i	
					adjs = obj.adj()
					for j in adjs:
						next.append(j)	
			i+=1
			adjs = next 
		return self.level
					

class Result:
	def __init__(self,list):
		self.original = list
		self.result ={}
	def transform(self):
		for key,value in self.original.items():
			self.result[key.value]=value	
		return self.result	
								
																
			

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeA.add_adj(nodeB)
nodeA.add_adj(nodeC)
nodeB.add_adj(nodeC)
nodeC.add_adj(nodeD)

bfs = Bfs(nodeA)


graph = GraphTraverse(bfs)
t =graph.traverse()
result = Result(t)
f_result = result.transform()
print(f_result)





adjA = nodeA.adj()
adjB = nodeB.adj()
adjC = nodeC.adj()


