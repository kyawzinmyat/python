def merge_sort(list):
	if len(list)>1:
		left= merge_sort(list[:int(len(list)/2)])
		right=merge_sort(list[int(len(list)/2):])
		return merge(left,right)			
	return list
		
		
def merge(list1,list2):
	i=0
	j=0
	answer=[]
	while i<len(list1) and j <len(list2):
		if list1[i]>list2[j]:
			answer.append(list2[j])
			j+=1
		elif list1[i]<list2[j]:
			answer.append(list1[i])
			i+=1
	
		
	#case when one list is empty	
					
	if i<len(list1) or j<len(list2):			
		if j>=len(list2) and i<len(list1):
				subRouteforI(list1,i,answer)
		elif i>=len(list1) and j<len(list2):
				subRouteforJ(list2,j,answer)
				
				
		
	return answer
	

#case when list 2 is empty	
		
def subRouteforI(list1,i,answer):
	if i<len(list1):
		answer.append(list1[i])
		subRouteforI(list1,i+1,answer)
		

#case when list1 is empty	
		
				
def subRouteforJ(list2,j,answer):
	if j<len(list2):	
		answer.append(list2[j])
		subRouteforJ(list2,j+1,answer)
			


#case when list1 and list2 are not empth 


def Route(list1,list2,i,j,answer):
		if i<len(list1) and j<len(list2):
			if list1[i]>list2[j]:
				answer.append(list2[j])
				Route(list1,list2,i,j+1,answer)
			elif list1[i]<list2[j]:
				answer.append(list1[i])
				Route(list1,list2,i+1,j,answer)
		
	


	
											
						
				
						
list =[5,4,3,2,1]
print(merge_sort(list))			
	
