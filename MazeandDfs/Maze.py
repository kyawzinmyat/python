class Maze:
	def __init__(self):
		self.maze =[
			["#"," ","#","#","E","#"],
			["#"," "," ","#"," ","#"],
			["#","#"," "," "," ","#"],
			["#","#"," ","#","#","#"],
			["S"," "," ","#","#","#"]
		]
		self.start ="S"
		self.stop="E"		
		
		
	def print(self,custom_maze=None):
		maze = self.maze
		if custom_maze:
			maze = custom_maze
		
		for i in maze:
			k=""
			for j in i:
				k+="".join(j)
			print(k)
			
	def get_index_of(self,node):
		for i,x in enumerate(self.maze):
			for j,y in enumerate(x):
				if y==node:
					return [i,j]
			
					
	def get_index(self,index):
		list_of_index=[]
		row_range=len(self.maze)
		col_range=len(self.maze[0])
		if index[0]+1<row_range:#down
				if self.maze[index[0]+1][index[1]]==" " or self.maze[index[0]+1][index[1]]=="E":
					list_of_index.append([index[0]+1,index[1]])
					
		
		if index[1]-1>=0:##left
			if self.maze[index[0]][index[1]-1]==" " or self.maze[index[0]][index[1]-1]=="E": 
					list_of_index.append([index[0],index[1]-1])
					
		
		if index[0]-1>=0:#up
			if self.maze[index[0]-1][index[1]]==" " or self.maze[index[0]-1][index[1]]=="E":
					list_of_index.append([index[0]-1,index[1]])
		
		if index[1]+1<col_range:#right
			if self.maze[index[0]][index[1]+1]==" " or self.maze[index[0]][index[1]+1]=="E":
					list_of_index.append([index[0],index[1]+1])
						
	
		
				
		return list_of_index