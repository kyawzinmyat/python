
# its simple is A[i] is the largest or not, the largest is in the A[i-1] to A[0]



def p_max(A,i):
	if i>0:
		j = p_max(A,i-1)	
		if A[j] >A[i]:
			return j
	return i
	
	
def selection_sort(A,i):	
	if i>0:
		j = p_max(A,i)
		if A[i]<=A[j]:
			A[i],A[j]=A[j],A[i]
			selection_sort(A,i-1)
	return A

		
A=[8,3,5,7,9]
i=len(A)-1
print(selection_sort(A,i))