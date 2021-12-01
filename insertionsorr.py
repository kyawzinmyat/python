user_list=5,4,3,2
def sort(list):
	for i in range(1,len(list)):
		key = list[i]
		while list[i-1]>key and i >0:
			list[i],list[i-1]=list[i-1],list[i]			
			i = i-1
	return list
#list = list.split(",")
list = [int(x)for x in user_list]
print(sort(list))