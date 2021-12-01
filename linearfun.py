def linear(list,num):
	global index
	index =-1
	for x in list:
		index +=1
		if x == num:	
			return index
		else:
			continue	
list = input("enter the numbers")
list = list.split(",")
list=[int(y)for y in list]
print(list)

num =int(input("Enter the num"))

linear(list,num)
if index<0:
	print("no index")	
else:
	print("the index is ",index)
