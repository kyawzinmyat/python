from Stack import Stack
from Maze import Maze	

class Dfs:
	def __init__(self):
		self.frointer=Stack()
		self.maze = Maze()
		self.visited=[]
		

		
	def traverse(self):
		self.frointer = [self.maze.get_start_index()]
		while self.frointer:
			current = self.frointer.pop()
			self.visited.append(current)
			for adj_index in self.maze.get_index(current):
				if adj_index not in self.visited:
					self.frointer.append(adj_index)
					self.maze.maze[adj_index[0]][adj_index[1]]="×"
			#print(self.frointer)
	
		self.maze.print()	
			
		
		

