def stack(max_l):
	stacks=[]
	def push(ele):
		if len(stacks)<=max_l:
			stacks.append(ele)
	def pop():
		if len(stacks)>0:
			stacks.pop()
		
	
	def show():
			print(stacks)
			
	return push,pop,show

push,pop,show = stack(5)
push(100)
push(150)
pop()
pop()
pop()
show()

