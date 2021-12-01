import random
score = 0
while True:
	test = random.randint(1,10000)
	print(test)
	user = int(input("//€€___"))
	
	if user==int(test):
		score += 1
	else:
		score = score
	print(score)