from dfs import Dfs
from csvtolist import get_maze_list



if __name__ =="__main__":
	new_maze = get_maze_list()
	df1 = Dfs()	
	### you can create or edit maze through maze.cav or use the default maze
	## if you use default maze you need to change Maze attribute
	df1.set_maze(new_maze)
	#df1.maze.start="A"
#	df1.maze.stop="B"
#	df1.maze.wall="#"
#	df1.maze.blank=" "
	df1.mark="☆"
	df1.solve()
#	df1.maze.print()
	#print(df1.maze.maze)