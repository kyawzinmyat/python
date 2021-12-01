class PlainPizza:
	def __str__(self):
		print('making doe')
		return f'making a plain pizza'
	
	def get_des(self):
		return f'Plain Pizza'
		
	def cost(self):
		return 3000
		
class ChickenTopping(PlainPizza):
	def __init__(self,pizza):
		self.pizza = pizza
	
	def __str__(self):
		super(). __str__()
		return f'adding chicken'
	
	def get_des(self):
		return f'Chicken ,{self.pizza.get_des()}'

	def cost(self):
		return 2000 + self.pizza.cost()
	
plain_pizza = PlainPizza()
chicken_pizza = ChickenTopping(plain_pizza)
double_chicken = ChickenTopping(chicken_pizza)
print(double_chicken)
print(double_chicken.get_des())
print(double_chicken.cost())