


# use counting sort as sub 

class CountingSort:
	def sort(self,temp,result,choose):
		for items in temp:
			for item in items:
				result[item[choose]].append(item)
		return result
		
		
		
class RadixSort:
	def __init__(self,list):
		self.list = list
		self.result = [[] for i in range(len(list)+1)]
		self.temp =[] 
		self.ctd = ConvertToDigit()
		self.cs = CountingSort()
		
		
	def sort(self):
		n = len(self.list)
		for num in self.list:
			u =self.ctd.get_tuple_form(n,num)
			self.temp.append([u])
		self.cs.sort(self.temp,self.result,1)
		self.temp = self.result
		self.result = [[] for i in range(len(list))]
		self.cs.sort(self.temp,self.result,0)	
		
		return self.result
	
class ConvertToDigit:
		def get_tuple_form(self,n,num):
			a = int(num /n)
			b = int(num%n)
			return a,b
			
		
	
class ConvertToNumber:
		def get_number_back(self,n,nums):
			ans = (n*nums[0])+nums[1]
			return ans
					
class Final:
	def get_number_back(self,list,sort):
		n = len(list)
		cal = ConvertToNumber().get_number_back
		result =[]
		for items in sort:
			if items:
				for item in items:				
					ans = cal(n,item)
					result.append(ans)
		return result
			

						
												
#it will not work for arbirtary number bcz it's only work for value that is <= len(number of items)^2

# here is example its only work for values less than 9 

																																																				
list =[1,5,8]				
rs = RadixSort(list)
sort = rs.sort()
final = Final()
final =final.get_number_back(list,sort)
print(final)
