class point():
	pass


def samepoint():
	return (p1.x == p2.x and p1.y == p2.y)
	
p1 = point()
p2 = point()
p1.x = 1
p2.x = 1
p1.y =2
p2.y = 2

print(p1 is p2)
print(samepoint())