from Database import Database
from table import Table,Column


class Person_Info(Table):
	name = Column("TEXT")
	age = Column("INTEGER")
	gender = Column("TEXT")


db = Database()
db.create(Person_Info)
