li =[]
 
def get_root(li):
	return li[0]

def add_node(li,node):
	li.append(node)

def get_range(li):
	return len(li)

#def get_child(li,node):	
#	try:
#		i = get_index(li,node)
#		left_child= li[2*i+1]
#		try:
#			right_child= li[2*i+2]
#			return left_child,right_child
#		except:		
#			return left_child
#	except:
#		return f'invalid child'


def get_index(li,node):
	i=0
	for item in li:
		if item==node:
			return i
		else:
			i+=1
	return i

		
def get_parent(li,node):
	try:
		i = get_index(li,node)
		if i ==0:
			return 0
		return li[abs(i-1)//2]	
	except:
		return None


def compare(i,j):
	if i<j:
		return True
	return False
	
	

def swap(p,i,li):
	parent_index = get_index(li,p)
	current_index = get_index(li,i)
	li[parent_index],li[current_index]=li[current_index],li[parent_index]
	return li


def max_heap(li):
	res =[]
	for i in li:
		res.append(i)
		parent = get_parent(res,i)
		while compare(parent,i):
			if parent !=0:
				swap(parent,i,res)
				parent = get_parent(res,i)
			else:
				break
	return res
		

		
def min_heap(li):
	res = []	
	for i in li:			
		res.append(i)
		
		parent = get_parent(res,i)
		if  not compare(parent,i):
			swap(parent,i,res)
		continue
	return res

def compare_max(i,j):
	if i == None:
		if j== None:
			return None
		else:
			return j
	else:
		if j==None:
			return i
	if i>j:	
		return i
	else:
		return j		
				
								
def left_child(li,i):
		try:
			left_child = li[2*i+1]
			return left_child
		except:
			return None
			
def right_child(li,i):
		try:
			right_child = li[2*i+2]
			return right_child			
		except:
			return None

			
										
			
def max_heapify(li):
	n = len(li)
	for i in reversed(range(0,n//2)):
		node = li[i]
		lc = left_child(li,get_index(li,node))
		rc = right_child(li,get_index(li,node))
		con = compare_max(lc,rc)
		while con!= None and node<con:
				swap(node,con,li)
				lc = left_child(li,get_index(li,node))
				rc = right_child(li,get_index(li,node))
				node = node
				con = compare_max(lc,rc)		
					
	return li
		

			
						
							
def heap_sort(li):
	i=0
	li=max_heap(li)
	res=[]
	for i in range(len(li)):
		t =li.pop(0)
		res.append(t)
		li=max_heapify(li)
	return res
	
	
			
	
						
																		
add_node(li,1)
add_node(li,8)
add_node(li,5)
add_node(li,2)
add_node(li,12)
add_node(li,4)
add_node(li,7)
add_node(li,9)
add_node(li,3)
add_node(li,6)
#print(li)
#print(get_child(li,1))
#print(get_index(li,3))
#print(get_root(li
#print(get_parent(li,1))
#print(max_heap(li))
#print(min_heap(li))
#print(max_heapify(max_heap(li)))
#print(max_heapify(li))
print(heap_sort(li))
