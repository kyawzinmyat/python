def f1(fun):
	def wrapper():
		print(1)
		fun()
		print(3)
	return wrapper

@f1	
def f2():
	print(2)
	
#f1(f2)()
#f = f1(f2)
#f2()


#name = input("enter ur name")

def check(fun):
	def wrapper(*args,**kwargs):
		print('checking _____')
		if name == 'Kyaw':
			fun(*args,**kwargs)
		else:
			print('invalid')	
		print('done')				
	return wrapper

@check
def greet(name):
	print("hi",name)
	
#greet(name)