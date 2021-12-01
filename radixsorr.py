class Ini:
	def __init__(self,list,choice):
		self.list = list
		size = len(self.list)
		self._result =[choice for i in range(size+1)]
	@property
	def result(self):
		return self._result

		



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
		self.cal = Digit()
		self.cs = CountingSort()
		
	def sort(self):
		n = len(self.list)
		for num in self.list:
			u =self.cal.calculate(n,num)
			self.temp.append([u])
		self.cs.sort(self.temp,self.result,1)
		self.temp = self.result
		self.result = [[] for i in range(len(list)+1)]
		self.cs.sort(self.temp,self.result,0)	
		
		return self.result
	
class Digit:
		def calculate(self,n,num):
			a = int(num /n)
			b = int(num%n)
			return a,b
	
class Number:
		def calculate(self,n,nums):
			ans = (n*nums[0])+nums[1]
			return ans
					
class Final:
	def calculate(self,list,sort):
		n = len(list)
		cal = Number().calculate
		result =[]
		for items in sort:
			if items:
				for item in items:				
					ans = cal(n,item)
					result.append(ans)
		return result
			
						

list =[26,32,35,21,12,21]				
rs = RadixSort(list)
sort = rs.sort()
final = Final()
final =final.calculate(list,sort)
print(final)
