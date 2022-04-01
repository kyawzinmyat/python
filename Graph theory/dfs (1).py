graph ={
	'A':['B','C'],
	'B':['C','E',],
	'C':['D'],
	'D':['E'],
	'E':[]	
}


def dfs(graph,start,end):
	global parent
	parent={}
	global visited
	visited=[]
	for i in graph:
		if i not in parent:
			visited.append(i)
			dfs_traverse(graph,i)
	
	return parent
	
	
	
def dfs_traverse(graph,i):
	print(i)
	for j in graph[i]:
		if j not in parent:
			parent[i]=j
			visited.append(j)
		return dfs_traverse(graph,j)

		
						
print(dfs(graph,'A','E'))		