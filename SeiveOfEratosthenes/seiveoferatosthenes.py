from math import sqrt,floor
import time


def find_prime(limit):
	start = time.time()
	mark =[True for x in range(limit)]
	mark[0]=False
	mark[1]=False
	
	if limit>=2:
		for i in range(2,int(sqrt(limit))):
			if mark[i]:
				j=i**2
				while j<limit:
					mark[j]=False
					j+=i
	end = time.time()
	print("running time ",end-start)
	return mark
	
def filter_prime(mark):
	counter=0
	answer =[]
	for index,value in enumerate(mark):
		if value:
			#print(index)
			counter+=1
			answer.append(index)
	print(counter)
#	print(answer)		
		
	
	
## its takes 12 sce to find all prime number in the range of 10 millions
n = 20000000
#
find_prime(n)
#print(filter_prime(find_prime(n)))
	