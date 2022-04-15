from is_possible import is_possible
def is_possible(x,y,n):
 	for row in problem:		
 		if row[y]==n:
 			return False
 	
 	for col in problem[x]:
 		
 		if col==n:
 			return False
 			
 			
 	x0 = (x//3)*3
 	y0 = (y//3)*3
 	for x in range(3):
 		for y in range(3):
 			if problem[x0+x][y0+y]==n:
 				return False
 		
 		 		
 		 		
 	return True
 	


def solve():
 		global problem
 		for i in range(6):
 			for j in range(6):
 				if problem[i][j]==0:
 					for k in range(1,10):
 						if is_possible(i,j,k):							
 							problem[i][j]=k
 							solve()
 							problem[i][j]=0
 					return 	
 							
 							
 	
problem = [
 	[0,0,7,0,2,9],
 	[1,0,0,6,0,8],
 	[0,2,0,7,1,0],
 	[2,3,0,1,0,5],
 	[5,0,0,3,0,2],
 	[0,0,0,6,0,0]
]
 
print(solve())
#print(problem)

for i in problem:
	print(i)
