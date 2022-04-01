graph ={
	'A':['B',],
	'B':['E',],
	'C':['D'],
	'D':['E'],
	'E':[]	
}


def bfs_traversal(graph,start):
	frointer=[start]
	visited=[]
	parent={}
	while frointer:
		for u in frointer:
			next=[]
			if u not in visited:
				visited.append(u)
				for v in graph[u]:	
					next.append(v)	
					if u in parent:
						parent[u].extend([v])
					else:
						parent[u]=[v]	
		frointer=next	
	return parent
	
#print(bfs_traversal(graph,'A'))
	
#print(visited)
class BFS:
	def __init__(self,graph,start,end):
			self.start=start
			self.end=end
			self.graph=graph
			
	def bfs_find_path(self):
		frointer=[self.start]
		visited=[]
		parent={}
		while frointer:
			for u in frointer:
				next=[]
				if u != self.end:
					if u not in visited:
						visited.append(u)
						for v in graph[u]:	
							next.append(v)	
							parent[u]=[v]
				else:
					parent[v]=u
					break
				
			frointer=next	
		return parent
		
start="A"
def get_path(graph,start,end,path=[start]):
	for i in graph[start]:
		if i == end:
			path.append(end)
			break
		else:
			path.append(i)
			return get_path(graph,i,end)
	return path

end="E"		
bfs = BFS(graph,start,end)
g = bfs.bfs_find_path()
print(g)
print(get_path(g,start,end))