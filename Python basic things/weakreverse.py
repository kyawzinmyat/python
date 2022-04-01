list =[9,8,7,6,5,4,3,2,1,0]
def reverse(list):
	length = int(len(list))
	if length%2 ==0:
		loop =length/2
		i = 0 
		n= length-1
		l= 0
		while l <loop:
			list[i],list[n]=list[n],list[i]
			l+=1
			i = i+1
			n=n-1		
	elif length%2 ==1:
		loop = length/2+0.5
		loop =int(loop)
		plus =0
		minus = length-1
		while plus != minus:
			list[plus],list[minus]=list[minus],list[plus]
			minus=minus-1
			plus = plus +1
	return list
	
	
print(reverse(list))
			
	
		
			
		