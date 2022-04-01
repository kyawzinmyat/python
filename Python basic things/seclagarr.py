array = [6,1,7,2,3,8]

def sec_largest(array):
	temp=[0,0]
	for i in range(0,len(array)):
		if temp[0]>=temp[1]:
			temp[1]=array[i]
		else:
			temp[0]=array[i]
				
	return temp

def get_sec(t):
	if t[0]<t[1]:
		return t[0]
	return t[1]

print(get_sec(sec_largest(array)))
	
		