l =[
	[3,1],
	[4,2,]
]


r =[3,
		2,
]

def test():
	m=[0,0]
	for i in range(2):
		for j in range(2):
			m[i]+=r[j]*l[i][j]
		
	print(m)

		
test()		


