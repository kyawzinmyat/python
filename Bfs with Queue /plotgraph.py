from pyvis.network import Network
import matplotlib.pyplot as plt
import networkx as nx




class Plot:
	def __init__(self):
		self.graph = nx.DiGraph() 
		self.nt = Network('1000px','1000px')
	
	def add_nodes(self,lists_of_nodes):
		for node in lists_of_nodes:
			self.graph.add_node(node)
		
	def add_edge(self,node,adj_node):
			self.graph.add_edge(node,adj_node)
		
	
	def save_file(self,name="Unknown",answer=None,adj_pair=None):
		node_color=["#1f78b4"]
		edge_color=["#1f78b4"]
		weight=[2]
		if  answer:
			node_color=[]
			edge_color=[]
			
			for node in self.graph:
				if node in answer:
					node_color.append("green")
				else:
					node_color.append("#1f78b4")
			
			for edg in self.graph.edges:
				weight=[]
				if edg in adj_pair:
					edge_color.append('green')
					weight.append(10)
				else:
					edge_color.append("#1f78b4")
					weight.append(3)
				
					
			
		nx.draw_circular(self.graph,font_weight='bold',node_size=900,with_labels=True,node_color=node_color,edge_color=edge_color,width=weight)
		plt.savefig(name+'.png')
	
		

		
		
		