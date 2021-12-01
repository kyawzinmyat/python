matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

test = [[row[i]for row in matrix]for i in range(3)]


print(test)
print(list(zip(*matrix)))

li =[]
for i in range(3):
	li_row =[]
	for row in matrix:
		li_row.append(row[i])
		
	li.append(li_row)
		
print(li)

li_2 =[]
for i in range(3):
	li_2.append([row[i] for row in matrix])
print(li)

dict ={
	'name':'kyaw',
	'age':17
}
	
for n,a in dict.items():
	print(n,a)	