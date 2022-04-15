a="aaaa"
b = "aaaab" 

#print(a[::-1])

def test1(a,b):
	c1 = b.count(a[0])
	return len(b)-len(a) if c1>=len(a) else "Impossible"

i ="IILLovecoding"
j="ILvovecoding"	
			
def test2(i,j):
	poi,poj = 0,0
	

	while poj<len(j) and poi<len(i):
		if j[poj]==i[poi]:
			poi+=1
			poj+=1	
		else:
			poj+=1
	
	return len(j)-poi if poi == len(i) else "IMPOSSIBLE"
	#return len(i) - score if score == len(j) else "Impossible"
	
def deter(i,j):
	if i==i[::-1]:
		return test1(i,j)
	else:
		return test2(i,j)
	
def main():
	cases = int(input())	
	for i in range(cases):
		print(f"Case #{i+1}: {deter(input(),input())}")
main()
