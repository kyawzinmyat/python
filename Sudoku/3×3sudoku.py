
from is_possible import is_possible
 

def solve(problem):
 		for i in range(3):
 			for j in range(3):
 				if problem[i][j]==0:
 					for k in range(1,10):
 						if is_possible(i,j,k,problem):
 							
 							problem[i][j]=k
 						
 		return problem
problem = [
 	[0,0,7],
 	[1,0,0],
 	[0,2,0]	
]
 				
 	
 	
#print(is_possible(2,1,7))	
print(solve(problem))

#print(problem)