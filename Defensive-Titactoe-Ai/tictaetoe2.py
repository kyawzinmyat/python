import random
import time
class Board:
	def __init__(self):
		self.board=["_" for i in range(9)]
		self.player ="X"
		self.bot ="O"
		
	def print_board(self):
		print("|"+self.board[0]+"|"+self.board[1]+"|"+self.board[2]+"|")

		print("|"+self.board[3]+"|"+	self.board[4]+"|"+self.board[5]+"|")

		print("|"+self.board[6]+"|"+self.board[7]+"|"+self.board[8]+"|")
	
	def terminate(self,mark):
		if self.board[0]==self.board[3]==self.board[6]==mark:
			return True
		elif self.board[0]==self.board[1]==self.board[2]==mark:
			return True
		elif self.board[0]==self.board[4]==self.board[8]==mark:
				return True
		elif self.board[3]==self.board[4]==self.board[5]==mark:
			return True
		elif self.board[1]==self.board[4]==self.board[7]==mark:
			return True
		elif self.board[6]==self.board[7]==self.board[8]==mark:
			return True
		elif self.board[6]==self.board[4]==self.board[2]==mark:
			return True
		elif self.board[8]==self.board[2]==self.board[5]==mark:
			return True
		return False
		
	def minmax(self,isMax):
		if self.terminate("X"):
				return -1
		elif self.terminate("O"):
				return 1
		
		elif "_" not in self.board:
			return 0
		
		if isMax:
			best_score = -1000
			av_sp_index = self.state()
			for index in av_sp_index:
				self.board[index]=self.bot
				value  = self.minmax(False)
				self.board[index]="_"
				best_score = max(value,best_score)
			return best_score
		else:
			best_score=1000
			av_sp_index = self.state()
			for index in av_sp_index:
				self.board[index]=self.player
		#		self.print_board()
			#	print("____")
				value = self.minmax(True)# bot true
				self.board[index]="_"
				best_score = min(value,best_score)
			return best_score
			
			
		
	def move_bot(self):
			best_score = -1000
			best_index=0
			av_sp_index = self.state()
			for index in av_sp_index:
				self.board[index]=self.bot
				value = self.minmax(False)
				self.board[index]="_"
				if value>best_score:
					best_score =value
					best_index=index
			self.insert(self.bot,best_index)

	def is_empty(self,pos):
		return self.board[pos]=="_"	
		
	def test(self):
		self.board[1]="X"
		self.board[2]="O"
		self.board[3]="X"
		self.board[5]="O"	
		self.board[6]="O"
		self.board[8]="X"
								
	def insert(self,mark,pos):
				if self.is_empty(pos):
					self.board[pos]=mark
					
					
				
		
	def state(self):
		space_list=[]
		for index,space in enumerate(self.board):
			if space =="_":				space_list.append(index)
		random.shuffle(space_list)
		
		return space_list
		
	def determine_match(self):
		if self.terminate(self.bot):
			return True
		elif self.terminate(self.player):
			return True
		elif "_" not in self.board:
			return True
		
	def play(self):
		while not self.determine_match():
			user_pos=  int(input("Enter the pos"))
			self.insert(self.player,user_pos)
			time.sleep(2)
			self.move_bot()
			self.print_board()
		#	user_pos=  int(input("Enter the pos"))
#			self.insert(self.player,user_pos)
			
			


b1 = Board()
#b1.test()
#b1.print_board()
#b1.minmax(True)
b1.play()
#5print(min(-1,0))
#print(b1.terminate("X")print(b1.state())