
from bst import Bst


if __name__ =="__main__":
	bfs = Bst()
	bfs.set_root(8)
	bfs.add(4)
	bfs.add(7)
	bfs.add(6)
	bfs.add(20)

	bfs.inorder(bfs.root)
	print(bfs.find(20))