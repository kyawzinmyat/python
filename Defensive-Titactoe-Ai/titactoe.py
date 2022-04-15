board =["_" for x in range(9)]

def print_board():
	print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")

	print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")

	print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")


#  
#0  1  2
#3  4  5
#6  7  8

def check(mark):
	if board[0]==board[3]==board[6]==mark:
		return 1
	elif board[0]==board[1]==board[2]==mark:
		return 1
	elif board[0]==board[4]==board[8]==mark:
		return 1
	elif board[3]==board[4]==board[5]==mark:
		return 1
	elif board[1]==board[4]==board[7]==mark:
		return 1
	elif board[6]==board[7]==board[8]==mark:
		return 1
	elif board[6]==board[4]==board[2]==mark:
		return 1
	elif board[8]==board[2]==board[5]==mark:
		return 1
	return 0
	
	
def is_end():
	for i in range(9):
		if board[i]=="_":
			return False
	return True

def get_emp_space():
	if not  is_end():
		for i in range(9):
			if board[i]=="_":
				return i
				
def insert(mark,pos):
				board[pos]=mark
				
#def all_possible(mark):
#	value=-100
#	index =None
#	if not is_end():
#		i=get_emp_space()
#		board[i]=mark
#		all_possible(mark)
#		n_v = check(mark)
#		board[i]="_"
#		if n_v>value:
#			value=n_v		
#			return index
#		return i


		#	insert_board(mark,i)

	
def all():
	av={}			
	for i,j in enumerate(board):
				if j=="_":
					av[i]=j
	return av
	
def minmax(mark,is_max):
	if check("O"):
			return 100
	elif check("X"):
		return -100
	if is_end():
			return 0
	
	if is_max:
			b_value=-200
			av = all()
			for ap in av:
				board[ap]="O"
				value = minmax("X",False)
				board[ap]="_"
				if value > b_value:
					b_value=value
					
			return b_value
	else:
				b_value=200
				av = all()
				for ap in av:
					board[ap]="X"
					value=minmax("O",True)
					board[ap]="_"
					if value < b_value:
						b_value=value
				return b_value
						
def bot():
	av = all()
	bv=-1000
	index = -1
	for j in av:
		board[j]="O"
		value = minmax("X",False)
		board[j]="_"
		if value >bv:
			bv=value
			index = j
		
	
	insert("0",index)
	
	
	

values={}	

x="X"
o="O"		
#board[0]=x
#bot()#
#board[2]=x
#bot()
#board[6]=x;
#bot()
#board[8]=x
#bot()
bot()
board[1]=x
bot()
board[8]=x
bot()
board[7]=x
#board[8]=x
bot()
#board[5]=x
#bot()
#bot()
#board[3]=x
#bot()
#board[6]=x
#bot()
#board[4]=x
#bot()
#bot()

#minmax(x)
print_board()
#print(minmax('X'))
