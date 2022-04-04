
import sqlite3
from table import Table

class Database:
	
	
	def __init__(self):
		self.conn = sqlite3.connect("sqlite.db")
		self.cursor = self.conn.cursor()
		
	def execute(self,command):
		try:		
			self.cursor.execute(command)
			self.conn.commit()
			#self.conn.close()
		except:
			print("There is something wrong")
		
		
	def create(self,Table):
		self.execute(Table.get_command())
	
		
		
				
	





		