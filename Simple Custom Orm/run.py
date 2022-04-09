from Database import Database
from table import Table,Column,ForeignKey
import inspect

class PersonInfo(Table):
	name = Column("TEXT")
	age = Column("INTEGER")
	

class Test(Table):
	name = Column("Text UNIQUE")
	
class Test2(Table):
	gender = Column("Text")
	test1 = ForeignKey(Test)
	info = ForeignKey(PersonInfo)


db = Database()
#db.drop(Test)

#db.execute("UPDATE Test SET name=? WHERE id=1",["Update!"])
#db.create(Test)

#t=Test(name="Myat")

#t2 = Test2(gender="Male")
#t2.test1 = t
#
#db.save(t)

#test = Test2.get(id=1)
#test.gender ="j"
#test.test1.name ="Name"
##print(test.gender)

#print(test.gender)
#print(test.name)
#test2 = Test(name="jake")
#db.save(test)
#test = Test2.get(id=1)
#print(test.test1.id)
#print(test.test1.name)

#print(t2.test1)
#9db.drop(Test)

#for i in Test2.all():
#	print(i.test1.name)


#for f in Test.all():
#	print(f.id)

#print(Test2.get_id_at(id=1))
#print(Test2.all())
#print(t2.id)

#t=Test(name="Kzm")
#db.save(t)
#print(t.id)
#db.save(t)
#t2 = Test2(gender="Lol")
#t2.test1 = t
#db.save(t2)
#print(t2.id)
