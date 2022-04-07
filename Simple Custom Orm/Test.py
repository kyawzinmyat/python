import inspect

j =[(1,"Kyaw"),(2,"Zin")]


fields = ["id","name"]
k=[]
for i in j:
	k.append(zip(i,fields))

	
			
for i  in k:
	print(dict(i))
	
	
	
#command = CommandFactory.get_command("all").format(fields=",".join(fields),table_name=cls.get_name())
#			
#			
#			
#command = "SELECT {fields} FROM {table_name}".format(fields=",".join(fields),table_name=cls.get_name())
#			
#			
#			


class test:
	
	name ={"id":1}
	
	
	@classmethod
	def g(cls):
		print(cls)
	
	def k(self):
		self.__class__.g()

		
class t:
				
	j = test()
	
	
j =[1,2,3]
l =["one","two","three"]

print(dict(zip(j,l)))



for i,j in zip(j,l):
	print(j)

