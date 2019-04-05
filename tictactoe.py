import random

def display_board(board):
	print(''.join(board))
	
def player_input():
	correct_input = False
	while correct_input == False:
		resp = input("'x' or 'o': ")
		if resp == 'x' or resp == 'o':
			break
	return resp
	
def place_marker(board, marker, position):
	if position==1:
		board[1]=marker
	elif position==2:
		board[5]=marker
	elif position==3:
		board[9]=marker
	elif position==4:
		board[12]=marker
	elif position==5:
		board[16]=marker
	elif position==6:
		board[20]=marker
	elif position==7:
		board[23]=marker
	elif position==8:
		board[27]=marker
	elif position==9:
		board[31]=marker
	return board
	
def win_check(board, mark):
	win=False
	if board[1]==mark and board[5]==mark and board[9]==mark:
		win=True
	elif board[12]==mark and board[16]==mark and board[20]==mark:
		win=True
	elif board[23]==mark and board[27]==mark and board[31]==mark:
		win=True
	elif board[1]==mark and board[12]==mark and board[23]==mark:
		win=True
	elif board[5]==mark and board[16]==mark and board[27]==mark:
		win=True
	elif board[9]==mark and board[20]==mark and board[31]==mark:
		win=True
	elif board[1]==mark and board[16]==mark and board[31]==mark:
		win=True
	elif board[9]==mark and board[16]==mark and board[23]==mark:
		win=True
	
	return win

def choose_first():
	randp=random.randint(1,2)
	if randp==1:
		return True
	elif randp==2:
		return False
	
def space_check(board, position):
	emptyspace=False
	if position==1 and board[1]=='_':
		emptyspace=True
	elif position==2 and board[5]=='_':
		emptyspace=True
	elif position==3 and board[9]=='_':
		emptyspace=True
	elif position==4 and board[12]=='_':
		emptyspace=True
	elif position==5 and board[16]=='_':
		emptyspace=True
	elif position==6 and board[20]=='_':
		emptyspace=True
	elif position==7 and board[23]=='_':
		emptyspace=True
	elif position==8 and board[27]=='_':
		emptyspace=True
	elif position==9 and board[31]=='_':
		emptyspace=True
	return emptyspace

def full_board_check(board):
	if board[1]!='_' and board[5]!='_' and board[9]!='_' and board[12]!='_' and board[16]!='_' and board[20]!='_' and board[23]!='_' and board[27]!='_' and board[31]!='_':
		return True
	else:
		return False
	
def player_choice(board):
	check=False
	while check==False:
		player_pos=int(input('1-9: '))
		if space_check(board,player_pos)==True:
			check=True
	
	return player_pos
			
	
def replay():
	check=False
	while check==False:
		resp = input('Do you want to play again? (Y/N): ')
		if resp.lower() == 'y':
			check=True
			return True
		elif resp.lower() == 'n':
			check=True
			return False
	
	
#MAIN
#1=[1], 2=[5], 3=[9], 4=[12], 5=[16], 6=[20], 7=[23], 8=[27], 9=[31]
def_board = ['_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_']

display_board(def_board)
turn=choose_first()
if turn:
	print('Player 1 goes first.')
	p1=player_input()
	if p1=='x':
		p2='o'
	else:
		p2='x'
else:
	print('Player 2 goes first.')
	p2=player_input()
	if p2=='x':
		p1='o'
	else:
		p1='x'
print(f'Player 1 is {p1} and Player 2 is {p2}')

p1win=False
p2win=False
fullboard=False

while p1win == False or p2win == False or fullboard==False:
	if turn:
		p1pos=player_choice(def_board)
		def_board=place_marker(def_board,p1,p1pos)
		display_board(def_board)
		if full_board_check(def_board)==True:
			print('Full Board')
			break
		if win_check(def_board,p1)==True:
			print('Player 1 wins')
			if replay():
				def_board = ['_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_']
				display_board(def_board)
				if choose_first()==True:
					print('Player 1 goes first.')
					p1=player_input()
					if p1=='x':
						p2='o'
					else:
						p2='x'
				else:
					print('Player 2 goes first.')
					p2=player_input()
					if p2=='x':
						p1='o'
					else:
						p1='x'
				print(f'Player 1 is {p1} and Player 2 is {p2}')
				p1win=False
				p2win=False
			else:
				break
		p2pos=player_choice(def_board)
		def_board=place_marker(def_board,p2,p2pos)
		display_board(def_board)
		if full_board_check(def_board)==True:
			print('Full Board')
			break
		if win_check(def_board,p2)==True:
			print('Player 2 wins')
			if replay():
				def_board = ['_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_']
				display_board(def_board)
				if choose_first()==True:
					print('Player 1 goes first.')
					p1=player_input()
					if p1=='x':
						p2='o'
					else:
						p2='x'
				else:
					print('Player 2 goes first.')
					p2=player_input()
					if p2=='x':
						p1='o'
					else:
						p1='x'
				print(f'Player 1 is {p1} and Player 2 is {p2}')
				p1win=False
				p2win=False
			else:
				break
	else:
		p2pos=player_choice(def_board)
		def_board=place_marker(def_board,p2,p2pos)
		display_board(def_board)
		if full_board_check(def_board)==True:
			print('Full Board')
			break
		if win_check(def_board,p2)==True:
			print('Player 2 wins')
			if replay():
				def_board = ['_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_']
				display_board(def_board)
				if choose_first()==True:
					print('Player 1 goes first.')
					p1=player_input()
					if p1=='x':
						p2='o'
					else:
						p2='x'
				else:
					print('Player 2 goes first.')
					p2=player_input()
					if p2=='x':
						p1='o'
					else:
						p1='x'
				print(f'Player 1 is {p1} and Player 2 is {p2}')
				p1win=False
				p2win=False
			else:
				break
		p1pos=player_choice(def_board)
		def_board=place_marker(def_board,p1,p1pos)
		display_board(def_board)
		if full_board_check(def_board)==True:
			print('Full Board')
			break
		if win_check(def_board,p1)==True:
			print('Player 1 wins')
			if replay():
				def_board = ['_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_\n','_',"_",'_','|','_','_','_','|','_','_','_']
				display_board(def_board)
				if choose_first()==True:
					print('Player 1 goes first.')
					p1=player_input()
					if p1=='x':
						p2='o'
					else:
						p2='x'
				else:
					print('Player 2 goes first.')
					p2=player_input()
					if p2=='x':
						p1='o'
					else:
						p1='x'
				print(f'Player 1 is {p1} and Player 2 is {p2}')
				p1win=False
				p2win=False
			else:
				break