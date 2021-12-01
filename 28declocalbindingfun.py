num1 = int(input("enter the num1"))
num2 =int(input("enter the num 2"))
division = int(num1/num2)
remainder =num1-(division*num2)

print("the remainder of {} divided by {} is {}".format(num1,num2,remainder))


x = 3  #global
def add(x,y): #local binding doesnt affect x
	x =x +y
	return x
print(add(2,3))
print(x)