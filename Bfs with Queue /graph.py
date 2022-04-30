import matplotlib.pyplot as plt



class Graph:
	def __init__(self):
		self._graph={}
		
	def add_vertices(self,list_of_vertices):
		for vertice in list_of_vertices:
			self._graph[vertice]=[]
			
	def add_adj_nodes(self,node,list_of_adj_node):
		for adj_node in list_of_adj_node:
			self._graph[node].append(adj_node)
			
			
			
	def get_adj(self,node):
		return self._graph[node]
	
	@property		
	def graph(self):
		return self._graph
		


class Graph:
	def __init__(self):
		self._graph={}
		
	def add_vertices(self,list_of_vertices):
		for vertice in list_of_vertices:
			self._graph[vertice]=[]
			
	def add_adj_nodes(self,node,list_of_adj_node):
		for adj_node in list_of_adj_node:
			self._graph[node].append(adj_node)
			
			
			
	def get_adj(self,node):
		return self._graph[node]
	
	@property		
	def graph(self):
		return self._graph
		



