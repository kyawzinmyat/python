graph ={
	'A':['B','C','D'],
	'B':['C'],
	'C':[],
	'D':['C'],	
}
def bfs(graph,start):
	level ={
		start:0,
		
	}
