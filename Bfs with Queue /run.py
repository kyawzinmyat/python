from graph import Graph

from collections import deque

from BfsQueue import Bfs


if __name__ == "__main__":
	graph = Graph()
	graph.add_vertices(["A","B","C","D"])
	graph.add_adj_nodes("A",["B","C"])
	graph.add_adj_nodes("B",[])
	graph.add_adj_nodes("C",["D"])

	bfs = Bfs(graph)
	bfs.traverse("A","D")

	bfs.plot_graph("bfs")
	vertices,adj_pair = bfs.find_path("A","D")
	bfs.plot_graph("answer",vertices,adj_pair)


