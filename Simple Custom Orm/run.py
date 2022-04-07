from Database import Database
from table import Table,Column,ForeignKey
import inspect

class Person_Info(Table):
	name = Column("TEXT")
	age = Column("INTEGER")
	gender = Column("TEXT")


class Test(Table):
	name = Column("Text UNIQUE")
	
class Test2(Table):
	gender = Column("Text")
	test1 = ForeignKey(Test)


db = Database()
#db.create(Test)

#t=Test(name="Myat")

#t2 = Test2(gender="Male")
#t2.test1 = t
#
#db.save(t2)

#print(t2.test1)
#9db.drop(Test)

#for i in Test.all():
#print(Test2.all())


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
