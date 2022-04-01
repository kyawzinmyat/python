num = int(input("enter the num for finding fibbo note this function count from 0 to n"))

def fibbo(num):
	if num <= 1:
		return 1
	else:
		return fibbo(num-1)+fibbo(num-2)

print("the fibbo num of {} is {}".format(num,fibbo(num)))