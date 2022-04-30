import math,random,pylab
class Location:
	def __init__(self,x,y):
		self.x=float(x)
		self.y=float(y)
	
	def move(self,new_x,new_y):
		return Location(self.x+float(new_x),self.y+float(new_y))
		
	def get_cord(self):
		return self.x,self.y
		
	def get_dist(self,old):
		old_x,old_y= old.get_cord()
		return math.sqrt(old_x**2+old_y**2)
		
class Compass:
	possibles =['N','E','S','W']
	def __init__(self,point):
		if point not in self.possibles:
			raise ValueError("point not in possibles")
		self.point = point
	
	def move(self,dist):
		if self.point =='N':
			return (0,dist)
		elif self.point =='S':
			return (0,-dist)
		elif self.point =='E':
			return (dist,0)
		return (-dist,0)
		
class Field:
	def __init__(self,person,loc):
		self.loc = loc
		self.drunk=person
	
	def move(self,point,dist):
		old = self.loc
		x_c,y_c = point.move(dist)
		self.loc = old.move(x_c,y_c)
	def get_drunk(self):
		return self.drunk
	
	def get_loc(self):
		return self.loc
		
class Drunk:
	def __init__(self,name):
		self.name = name
	
	def move(self,field,time=1):
		if field.get_drunk() != self:
			raise ValueError
		for i in range(time):
			cp = Compass(random.choice(Compass.possibles))
			field.move(cp,1)
			
			
def performTrial(time,field):
	start = field.get_loc()
	distances=[0.0]
	for i in range(time):
		field.get_drunk().move(field)
		newLoc = field.get_loc()
		distance = newLoc.get_dist(start)
		distances.append(distance)
	
	return distances

drunk = Drunk("Kyaw")
f = Field(drunk,Location(0,0))
distances = performTrial(500,f)
pylab.plot(distances)
pylab.xlabel("Time")
pylab.ylabel("Distance from origin")

pylab.savefig("test.png")
	