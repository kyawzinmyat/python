problem = [
 	[0,0,7],
 	[1,0,0],
 	[0,2,0]	
]
 
 
def is_possible(x,y,n):
 	for row in problem:
 		
 		if row[y]==n:
 			return False
 	
 	for col in problem[x]:
 		
 		if col==n:
 			return False
 			
 
 	for i in range(3):
 		for y in problem[0+i]:
 		 	if y==n:
 		 		return False
 		 		
 		 		
 	return True
 	
def solve():
 		for i in range(3):
 			for j in range(3):
 				if problem[i][j]==0:
 					for k in range(1,10):
 						if is_possible(i,j,k):
 							
 							problem[i][j]=k
 						
 		return problem
 				
 	
 	
#print(is_possible(2,1,7))	
print(solve())

#print(problem)