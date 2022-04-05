from Database import Database
from table import Table,Column
import inspect

class Person_Info(Table):
	name = Column("TEXT")
	age = Column("INTEGER")
	gender = Column("TEXT")


class Test(Table):
	name = Column("Text")



db = Database()


t = Test(name="Kyaw")

db.save(t)
#print(db.execute("SELECT * FROM test").fetchall())
#print(t.get_insert_command())


