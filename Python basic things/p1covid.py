def merge(left,right):
	result =[ ]
	i,j =0,0
	while i < len(left) and j<len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	while i< len(left):
		result.append(left[i])
		i+=1
	while j<len(right):
		result.append(right[j])
		j+=1
	return result

def mergesort(b):
			if len(b)<2:
				return b
			else:
				middle = int(len(b)/2)
				left = mergesort(b[:middle])
				right= mergesort(b[middle:])
				final = merge(left,right)
				return final
	
#left = [2]
#right=[1]
l = [5,4,3,2,1,6]	
print(mergesort(l))