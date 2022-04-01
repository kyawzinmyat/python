
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
			
print(graph)					
	
print(relaxation('A'))



# it doesnt give  actually shortest path it give you the minimum weight values


# is doesn't work for negative weight edges
# Graph representation is vertix * vertix array


print(values)