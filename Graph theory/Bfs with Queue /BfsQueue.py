from collections import deque
from Queue import Queue
from graph import Graph


class Bfs:
	def __init__(self,graph):
		self.graph=graph
		self.queue = Queue()
		self.visited=[]
		self.parent={}
		

	def traverse(self,start_node):
			self.queue.append(start_node)
			while self.queue:
				current_node=self.queue.popleft()
				if current_node not in self.visited:
					self.visited.append(current_node)
				
					self.queue.append(self.graph.get_adj(current_node))
					
			return self.visited
				
			
						






# adj list

							
graph = Graph()



graph.add_vertices(["A","B","C","D"])
graph.add_adj_nodes("A",["B","D"])
graph.add_adj_nodes("B",["C","D"])
graph.add_adj_nodes("C",["D"])

bfs = Bfs(graph)
		
print(bfs.traverse("A"))







