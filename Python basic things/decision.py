
def max(w,v,i,aw,value):
		if aw!= 0:
			if w[i] <= aw:
				aw = aw-w[i]		
				value += v[i]
				i = i-1
				print(w,v,i,aw,value)
				return max(w,v,i,aw,value)
			else:
				if i ==0:
					i=k
					return max(w,v,i,aw,value)
				else:
					return 0
		else:
			return value
					
						
						
				
w = [5,4,3,2]
v =  [7,3,6,6]
aw = 9
i = 3
k=i
print(max(w,v,i,aw,0))