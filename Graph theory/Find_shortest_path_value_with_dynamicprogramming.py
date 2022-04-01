				
lst =['A','B','C','D','E','F']
# inefficient for space
# solve with dynamic programming 

def ini_graph(lst):
	global graph
	global weight_graph
	global incoming_graph
	global parent
	
	graph =[[0 for x in range(len(lst))]for j in range(len(lst))]
	
	weight_graph = [[0 for x in range(len(lst))]for j in range(len(lst))]
	
	incoming_graph = [[0 for x in range(len(lst))]for j in range(len(lst))]
	
	
	
def add_edge(v1,v2,weight):
	graph[lst.index(v1)][lst.index(v2)]=1
	weight_graph[lst.index(v1)][lst.index(v2)]=weight
	incoming_graph[lst.index(v2)][lst.index(v1)]=1
	
def ini_value(lst):
	global value
	value={}
	for i in lst:
		value[i]=99
		
		
	


def get_adj(v):
	ans=[]
	temp_index = lst.index(v)
	j=0
	for i in graph[temp_index]:
		if i == 1:
			ans.append(lst[j])
		j+=1
	return ans

def get_incoming_edge(v):
	ans =[]
	temp_index = lst.index(v)
	j=0
	for i in incoming_graph[temp_index]:
		if i ==1 :
			ans.append(lst[j])
		j+=1
	return ans
	
def sp(v):## single source shortest path
	value[v] = 0
	return _sp(v)			
			
def _sp(v):
	adj = get_adj(v)	
	for i in adj:
		relaxation(v,i)	
		_sp(i)
	

def relaxation(u,v):
	
	if value[v] > value[u]+weight_graph[lst.index(u)][lst.index(v)]:
		value[v] = value[u]+weight_graph[lst.index(u)][lst.index(v)]



# sp = shortest path
# recurence relation = sp(vertix(n))(min(current_weight,sp(vertix(n-1))+weight(vertix(n-1),vertix(n))))
		
def sp_dp(vertix,):

	if vertix:
		if lst.index(vertix) != 0:
			edge = get_incoming_edge(vertix)
			for j in edge:
				temp = value[vertix]
				value[vertix]=min(value[vertix],weight_graph[lst.index(j)][lst.index(vertix)]+sp_dp(j))
		
			return value[vertix]			
				
		else:
			value[vertix]=0	
	return value[vertix]
	

			


ini_value(lst)
ini_graph(lst)
add_edge('A','B',2)
#add_edge('B','C',1)
add_edge('A','C',2)
add_edge('B','D',2)
add_edge('C','D',1)
#add_edge('D','E',1)
#add_edge('E','F',5)


#sp("A")
sp_dp('D')
print(value)


#print(value)
#print(get_adj('A'))
#print(get_incoming_edge('B'))
#print(get_incoming_edge('A'))




