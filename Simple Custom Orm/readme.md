Orm project hasn't finished yet
this project  inspire gtback orm video

you can create database object and create table by passing table object!


You can now insert values into table!

You can query now 

You can now add foreign key

_____________________________________________

To connect to database,You need to instantiate
Database class (db = Database())
this will create "sqlite.db" in current directory .

To create A table ,You need to inherit Table class and 
add class variable as table column and assign Column class with attribute datatype  (class Info(Table): name=Column("TEXT") work = ForeignKey(AnotherTableClass) 
variable name will be column name and value will be column datatype

once you created table,now can instantiate Info table but that will not save to database
To save to database, you need to call create method(method of database) and pass instance as parameter .That will save to the database 

