import time
from math import sqrt,floor

class SegmentedSeive:
	def __init__(self):
		self.max = 10000000
		self.limit=int(sqrt(self.max))
		self.mark =[True for x in range(floor(self.limit))]
		self.mark[0]=False
		self.mark[1]=False
		self.prime=[]
		self.low = self.limit
		self.high = self.limit*2
		self.temp=[]
		
	
	def find_prime(self):	
		if self.limit>=2:
			for i in range(2,self.limit):
				if self.mark[i]:
					j=i**2
					while j<self.limit:
						self.mark[j]=False
						j+=i
		self.limit +=1 
	
		
	def segmented(self):
		start = time.time()
		self.find_prime()	
		self.print_prime()
		while self.low < self.max:
			#print(self.low)
			self.mark=[True for x in range(self.limit)]
			if self.high >=self.max:
					self.high=self.max
					
											
			for i in self.prime:
				low_l = floor(self.low/i)*i
				if low_l<self.low:
					low_l+=i
				

				for j in range(low_l,self.high+1,i):
					self.mark[j-self.low]=False
					#;print(j)
												
			#for k in range(self.low,self.high+1):
#					if self.mark[k-self.low]:
#					
#						self.temp.append(k)
#						
						
						
			self.low += self.limit
			self.high+= self.limit
		end = time.time()
		print("running time ",end-start)
				
			
			
									
																	
	def print_prime(self):
		for index,value in enumerate(self.mark):
			
			if value:
				#print(index)
				self.prime.append(index)
				
				
#	def 

se = SegmentedSeive()
#se.find_prime()
se.segmented()
#print("numbers of prime ",len(se.prime))
print(len(se.temp)+len(se.prime))
