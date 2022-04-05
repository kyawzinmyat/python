
		
class CommandFactory:		
		
				
		create_command="CREATE TABLE {table_name} ({fields})"
		
		table_command ="SELECT name FROM sqlite_master WHERE name ='table' "				
										
		@classmethod
		def get_command(cls,command_name):
				if command_name =="create":
					return cls.create_command
				elif command_name =="table":
					return cls.table_command
					
					

				

				
				
		
				
		

