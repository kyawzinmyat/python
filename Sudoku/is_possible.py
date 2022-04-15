def is_possible(x,y,n,problem):
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
 	