
import sqlite3
from table import Table,CommandFactory



class Database:
	
	
	def __init__(self):
		self.conn = sqlite3.connect("sqlite.db")
		self.cursor = self.conn.cursor()
		Table.db = self
		
	def execute(self,command,values=None):
		try:
			if values:		
				return self.cursor.execute(command,values)
			return self.cursor.execute(command)
			
		except:
			print("There is something wrong")
		
		
	def create(self,Table):
		self.execute(Table.get_create_command())
	#	print(Table.get_create_command())
		
	def table(self):
	
		return self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'; ").fetchall()
		
		
	def save(self,instance):
		
		command,values = instance.get_insert_command()
	#	print(command,values)
		
		self.execute(command,values)
		instance._data["id"]= self.cursor.lastrowid
		self.call_commit()
#		
		
		
	def drop(self,table):
		self.execute(CommandFactory.get_command("drop").format(table_name=table.get_name()))
	
	
	
		
	def call_commit(self):
		self.conn.commit()
		
		

		
		
				
	





		