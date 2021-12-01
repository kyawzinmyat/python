def pre_max(n,list):
	if n > 0:
		j = pre_max(n-1,list)
		if list[j]>list[n]:
			return j
		else:
			return n
	else:
		return n
		
def sort(list):
	n = len(list)
	for i in reversed(range(n)):
		j = pre_max(i,list)		
		list[i],list[j]=list[j],list[i]
	
	return list


list = [3,2,1]
print(sort(list))