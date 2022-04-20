
#abcdefb

#fb 

#size =2
#hash(abc)=hash(a)+hash(b)+hash(c)

#hash(bcd)= (hash(abc)-a*base^size)*base + hash(d)


class KarpRabin:
	def __init__(self,text,paragraph):
		self.text=text
		self.paragraph = paragraph
		self._hash=0
		self.prime=23
		self.base =10
		self.hash_of_text=self.hash(int(self.text))
	#	self.magic = 
		
	def hash(self,num):
		return num%self.prime
		
	def rolling_hash(self,old,new):
#		print(self._hash-int(old)*self.base)
		self._hash = self.hash(self._hash-(int(old)*self.base))
		self._hash = self.hash(self._hash*self.base+int(new))	# append
	#	print(self._hash)
	#	temp = self.hash((self._hash-int(old))*self.base+self.base*self.prime)*self.base+int(new)	
		
		#print(temp)		
		#self._hash = self.hash(temp)
		#print(self._hash)
	
	def match(self):
		self._hash = self.hash(int(self.paragraph[:len(self.text)]))
	#	print(self._hash)
		
		if self._hash == self.hash_of_text:
			return 0
		
		for i in range(len(self.text),len(self.paragraph)):		
			self.rolling_hash(self.paragraph[i-2],self.paragraph[i])
		
			if self._hash==self.hash_of_text:
				
				return i if self.paragraph[i-1:i+len(self.text)-1] == self.text else None
		
paragraph ="123456"
text ="56"



kr = KarpRabin(text,paragraph)

print(kr.match())
#print(kr.hash(45))
#kr.rolling_hash()
#print(kr.hash_of_text)