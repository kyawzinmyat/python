#import pyvis

from pyvis.network import Network
import matplotlib.pyplot as plt
import networkx as nx


nx_graph = nx.Graph() 
nx_graph.add_node(20, title='couple1',label="test") 
nx_graph.add_node(21, title='couple2') 
nx_graph.add_edge(20, 21, weight=5) 

nt = Network('800px','800px')
print(dir(nx))
#

#subax2 = plt.subplot() 
#options = { 'node_color': 'blue',  'node_size': 1000,  'width': 4,' }
#nx.draw(nx_graph, with_labels=True, font_weight='bold')

#nx.draw_circular(nx_graph, **options)
#plt.savefig('test.png')

#nx.('test.png') 


