graph ={
	'A':['B','C'],
	'B':['C','E',],
	'C':['D'],
	'D':['E'],
	'E':[]	
}


def dfs(graph,start,end):
	parent={}
	visited=[]
	for i in graph:
		if i not in parent:
			visited.append(i)
			dfs_traverse(graph,i,parent,visited)
	
	return visited
def dfs_traverse(graph,i,parent,visited):
	for j in graph[i]:
		if j not in parent:
			parent[i]=j
			visited.append(j)
		return dfs_traverse(graph,j,parent,visited)
		
print(dfs(graph,'A','E'))		