from Database import Database
from table import Table,Column
import inspect

class Person_Info(Table):
	name = Column("TEXT")
	age = Column("INTEGER")
	gender = Column("TEXT")


class Test(Table):
	name = Column("Text")
	
class Test2(Table):
	gender = Column("Text")



db = Database()


#db.create(Test2)

#db.save(Test2(gender="female"))


#print(db.table())


#j=Test.get_select_all_command()
k= Test2.all()
for j in k:
	print(j.id)
	print(j.gender)


