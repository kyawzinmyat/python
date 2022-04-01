user_input =input("enter the num")
user_input = user_input.split(",")
num = int(input("Enter the num"))
list = [int(x)for x in user_input]
print(list)
index = -1
for x in list:
	index +=1
	if x == num:
		print("The number is Index at",index)
		break
	else:
		continue