


### using adj list

## example graph 
## A-->B
##  |    |
## C-->D

graph={
	'A':["B","C"],
	"B":["D"],
	"C":["D"],
	"D":[],
	"E":["G"],
	"F":["H"],
	"G":["F"],
	"H":[],
	
}




	
	


def dfs(graph,startNode,layer):
	counter[startNode]=layer
	visited.append(startNode)
	for adjNode in graph[startNode]:
		if adjNode not in visited:
			print(adjNode)
			dfs(graph,adjNode,layer)
	 
		
# for connected component


def connected_Component(graph):
	
	global visited
	global counter
	visited=[]
	layer=0
	counter={}
	for node in graph:
		if node not in visited:	
			dfs(graph,node,layer)
			layer+=1
	return counter
			
		



	

#print(dfs(graph))
print(connected_Component(graph))

