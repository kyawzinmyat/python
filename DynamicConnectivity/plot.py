from pyvis.network import Network
import matplotlib.pyplot as plt
import networkx as nx


class Plot:
	def __init__(self):
		self.graph = nx.Graph() 
		self.nt = Network('2000px','2000px')
	
	def add_nodes(self,lists_of_nodes):
		self.graph.add_nodes_from(lists_of_nodes)
		
	def add_edge(self,node,adj_node):
			self.graph.add_edge(node,adj_node)
		
	
	def save_file(self,name="Unknown"):
		nx.draw_networkx(self.graph, with_labels=True, font_weight='bold',node_size=700)
		#options = { 'node_color': 'blue',  'node_size': 800,  'width': 4}
#		nx.draw_circular(self.graph, **options)
		plt.savefig(name+'.png')
		
		
		