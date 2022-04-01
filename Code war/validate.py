def balance(parans):
	open=['(','{','[']
	close =[')','}',']']	
	stack=[]
	for paran in parans:
		if paran in open:
			 stack.append(paran)
		if len(stack)>0 and  paran == close[open.index(stack[len(stack)-1])]:
			stack.pop()
	
	
				
			
	return len(stack)==0
	
		
print(balance("(){}{{}}"))



def queue(parans):
	open =tuple('([{')
	close = tuple(')]}')
	map = dict(zip(open,close))
	queue=[]
	for paran in parans:
		if paran in open:
			queue.append(map[paran])
		elif paran in close:
			if not queue or paran != queue.pop():
				return False
	return len(queue)==0



l=['(']
j=[')']

j=zip(l,j)
print(dict(j))
print(queue("{[]()}"))
		 


j="(){}[()"

l =["()","[]","{}"]

for br in range(int(len(j)/2)):
	for i in l:
		j = j.replace(i,"")
		
print(j)
			