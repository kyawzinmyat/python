global vertices
vertices =['A','B','C','D','E']
def ini_graph(vertices):
	global dic
	global graph
	
	dic ={}
	j =0
	for v in vertices:
		dic[v]=j
		j+=1

	graph = [[-1 for i in vertices ]for j in vertices]	
	return graph
		
		
def add_edg(vertix,adj,weight):
	index = dic[vertix]
	graph[index][dic[adj]] =weight

def get_adj(vertix):
	ans =[]
	index = dic[vertix]
	j=0
	for i in graph[index]:
		if i >=0:
			ans.append(vertices[j])
		j+=1

		
	return ans
			
			
	
def bfs(source):
	parent ={source:None}
	frointer = [source]
	j=0
	visited=[]
	level ={}		
	
	while frointer:
		for i in frointer:
			level[i]=j
			visited.append(i)
			adj = get_adj(i)
			next=[]
			for u in adj:
				parent[u]=i
				if u not in level:
					next.append(u)
		j+=1
		frointer = next
		#print(visited)	
	return parent
	
																	
def sp_bfs(start,end):
	frointer = [start]
	j=0
	level ={}		

	while frointer:
		for i in frointer:
			if i != end:
				level[i]=j
				adj = get_adj(i)
				next=[]
				for u in adj:
					if u not in level:
						next.append(u)
			else:
				level[i]=j
				next=[]			
		j+=1
		frointer = next
	return level
	
			
def dfs(vertices):
	parent={}
	for i in vertices:
		visit(i,parent)	
	
def visit(node,parent):
	adj = get_adj(node)
	print(node)
	for i in adj:
		if i not in parent:	
			parent[i]=node
			visit(i,parent)
	return parent
		

def relaxation_ini(vertices):
	global values
	values={}
	for i in vertices:
		values[i]=1000000
	
	return values
	
def relaxation(u):
	values =relaxation_ini(vertices)
	adj = get_adj(u)
	values[u]=0
	for i in adj:
		weight(u,i)
	
	
def weight(u,v):
	if values[v]>=values[u]+graph[dic[u]][dic[v]]:
		values[v]=values[u]+graph[dic[u]][dic[v]]
	adj = get_adj(v)
	for i in adj:
		weight(v,i)
	
	

ini_graph(vertices)
add_edg('A','B',6)
add_edg('B','E',2)
add_edg('D','B',1)
add_edg('C','D',4)
add_edg('A','C',1)
add_edg('D','E',2)
#print(graph)
#print(get_adj('D'))
#print(bfs('A'))
#print(sp_bfs('A','D'))
#print(dfs(vertices))
#print(relaxation('A'))
#print(values)