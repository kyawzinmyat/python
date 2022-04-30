from Queue import Queue
from plotgraph import Plot


class Bfs:
	def __init__(self,graph):
		self.graph=graph
		self.queue = Queue()
		self.visited=[]
		self.parent={}
		self.plot=Plot()
		

	def traverse(self,start_node,end_node=" "):
			self.queue.append(start_node)
			while self.queue:
				current_node=self.queue.popleft()
				self.visited.append(current_node)
				if current_node==end_node:					
					return self.parent
					#self.find_path(start_node,end_node)						
				temp=[]	
				for adj_node in self.graph.get_adj(current_node):
					
					if adj_node not in self.visited and adj_node not in self.queue:
						temp.append(adj_node)
						self.parent[adj_node]=current_node			
				self.queue.append(temp)
			#print(self.queue)		
			return 
			
			
	def find_path(self,start,end):
		pointer = end
		test=[]
		answer=[]
		for node,parent in reversed(self.parent.items()):
			if node != start:
				if node == pointer: 
					pointer=parent
					answer.append(node)
					test.append((pointer,node))
		answer.append(start)
		#answer.reversed()
		
		return answer[::-1],test[::-1]
		
			
	def plot_graph(self,name,answer=None,adj=None):
		self.add_nodes()
		self.add_edge()
		self.plot.save_file(name,answer,adj)
				
	def add_nodes(self):
		self.plot.add_nodes(self.graph.graph)
	
	def add_edge(self):
			for node,adj_nodes in self.graph.graph.items():
				for adj_node in adj_nodes:
					self.plot.add_edge(node,adj_node)
			
				
			
						






# adj list

							


