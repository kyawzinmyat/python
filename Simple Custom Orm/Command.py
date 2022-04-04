from  abc  import ABC,abstractmethod


class Command(ABC):
	
	
	@abstractmethod	
	def get_command(self):
		return self.command
		
		
class CreateCommand(Command):
	def __init__(self):
		self.command="CREATE TABLE "
	
	def get_command(self):
		return self.command
		
class DeleteCommand(Command):
	
	def __init__(self):
		sefl.command="DROP TABLE"
	
	def get_command(self):
		return self.command
		
		
		
		
class CommandFactory:		
				
	
		def get_command(self,command_name):
				if command_name =="create":
					return CreateCommand().get_command()
				
		
				
				
c = CommandFactory()
				
				
		
				
		

