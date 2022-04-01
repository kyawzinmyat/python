def check_cc(card_num):
	pivot=1
	res=list(str(card_num))
	if len(str(card_num))%2==0:
		pivot=0
	while pivot<len(str(card_num)):
			if 2*int(res[pivot])>9:
				res[pivot]=2*int(res[pivot])-9
			else :
				res[pivot]=2*int(res[pivot])			
			pivot+=2
	res=[int(int_num) for int_num in res]

	return sum(res)%10==0
		
	
j=891

print(check_cc(j))

k=[int(i) for i in str(j)]
print(k)		
	