from Maze import Maze	
from node import Node
from collections import deque


class Bfs:
	def __init__(self):
		self.maze = Maze()
		self.frointer=deque()
		
		
bf1 = Bfs()
print(bf1.frointer)