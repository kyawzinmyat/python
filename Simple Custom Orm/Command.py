
		
class CommandFactory:		
		
				
		create_command="CREATE TABLE {table_name} ({fields})"
		
		insert_command ="INSERT INTO {table_name} ({fields}) VALUES({placeholder})"
		
		table_command ="SELECT name FROM sqlite_master WHERE name ='table' "
		
		all_command="SELECT {fields} FROM {table_name}"
		
		drop_command ="DROP TABLE {table_name}"				
										
		@classmethod
		def get_command(cls,command_name):
				if command_name =="create":
					return cls.create_command
				elif command_name =="table":
					return cls.table_command
				elif command_name=="all":
					return cls.all_command
				elif command_name=="insert":
					return cls.insert_command
				elif command_name=="drop":
					return cls.drop_command
					
					

				

				
				
		
				
		

