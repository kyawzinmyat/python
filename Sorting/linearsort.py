

# counting sort



unsorted =[9,8,7,6,5,4,3,2,1]

def counting_sort(unsorted_list):
		sorted_list = [[]for i in range(10)]

		for i in unsorted:
			sorted_list[i]=i
		return remove_blank(sorted_list)
			
def remove_blank(sorted_list):
	result=[]
	for num in sorted_list:
		if num!=[]:
			result.append(num)
	return result
	
	
print(counting_sort(unsorted))