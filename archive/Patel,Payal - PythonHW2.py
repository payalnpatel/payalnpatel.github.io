# -*- coding: utf-8 -*-
"""
@author: Payal Patel
Python Assignment 2: Tic-Tac-Toe 
"""

### Create Functions: ###

#first_board function - used to reset winner variable & board list for new game 
#(also making winner & board global variables)
def first_board():
    global winner, board
    winner = False
    board = [ [' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' '] ]

#draw_board function - used to draw tic-tac-toe board
def draw_board():
    for row in board:
        print('----------' * 3)
        for column in row: 
            print('|', column, end = '       ')
        print('|')
    print('----------' * 3)

#next_move function - 
#used to go through moves between both players as long as a winner has not been determined
#or as long as a tie has not occurred.  
def next_move():
    while winner == False:
        x_move()
        if check_win(board) == True:
            print('X wins!')
            break
        elif board_full() ==9:
            break
        o_move()
        if check_win(board) == True:
            print('O wins!')
            break
        elif board_full() == 0:
            break 

#spaces = ['A1', 'A2', 'A3' ,'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
#x_move function - used to take 'X' player's input for next position and update the tic-tac-toe board accordingly
def x_move():
    position_x = input('X choose a position:')
    position_x = position_x.upper()
    if position_x in ['A1', 'A2', 'A3' ,'B1', 'B2', 'B3', 'C1', 'C2', 'C3']:
        update_board_x(position_x)
        current_board(board)
    else:
        x_redo()
    
#o_move function - used to take 'O' player's input for next position and update the tic-tac-toe board accordingly
def o_move():
    position_o = input('O choose a position:')
    position_o = position_o.upper()
    if position_o in ['A1', 'A2', 'A3' ,'B1', 'B2', 'B3', 'C1', 'C2', 'C3']:
        update_board_o(position_o)
        current_board(board)
    else:
        o_redo()

#update_board_x function - updates board for player x based on response
def update_board_x(position_x):
    if position_x =='A1' and board[0][0] == ' ':
            board[0][0] = 'X'
    elif position_x =='B1' and board[0][1] == ' ':
            board[0][1] = 'X'
    elif position_x =='C1' and board[0][2] == ' ':
            board[0][2] = 'X'
    elif position_x =='A2' and board[1][0] ==' ':
            board[1][0] = 'X'
    elif position_x =='B2' and board[1][1] == ' ':
            board[1][1] = 'X'
    elif position_x =='C2' and board[1][2] == ' ':
            board[1][2] = 'X'
    elif position_x =='A3' and board[2][0] == ' ':
            board[2][0] = 'X'
    elif position_x =='B3' and board[2][1] == ' ':
            board[2][1] = 'X'
    elif position_x =='C3' and board[2][2] == ' ':
            board[2][2] = 'X'
    else:
        x_redo()

#update_board_o function - updates board for player o based on response 
def update_board_o(position_o):
    if position_o =='A1' and board[0][0] == ' ':
        board[0][0] = 'O'
    elif position_o =='B1'and board[0][1] == ' ':
        board[0][1] = 'O'
    elif position_o =='C1' and board[0][2] == ' ':
        board[0][2] = 'O'
    elif position_o =='A2' and board[1][0] == ' ':
        board[1][0] = 'O'
    elif position_o =='B2' and board[1][1] == ' ':
        board[1][1] = 'O'
    elif position_o =='C2' and board[1][2] == ' ':
        board[1][2] = 'O'
    elif position_o =='A3' and board[2][0] == ' ':
        board[2][0] = 'O'
    elif position_o =='B3' and board[2][1] == ' ':
        board[2][1] = 'O'
    elif position_o =='C3' and board[2][2] == ' ':
        board[2][2] = 'O'
    else:
        o_redo()

#update board display after player makes a move
def current_board(board):
    
    for row in board:
        print('----------' * 3)
        for column in row: 
            print('|', column, end = '       ')
        print('|')
    print('----------' * 3)

#check_win function - used to check if X has won the game or if O has won the game 
def check_win(board):
    #checking if X has won based off of various combinations
    if board[0][0] =='X' and board[0][1] =='X' and board[0][2] =='X':
        winner = True
    elif board[1][0] =='X' and board[1][1] =='X' and board[1][2] =='X':
        winner = True
    elif board[2][0] =='X' and board[2][1] =='X' and board[2][2] =='X':
        winner = True   
    elif board[0][0] =='X' and board[1][0] =='X' and board[2][0] =='X':
        winner = True
    elif board[0][1] =='X' and board[1][1] =='X' and board[2][1] =='X':
        winner = True
    elif board[0][2] =='X' and board[1][2] =='X' and board[2][2] =='X':
        winner = True
    elif board[0][0] =='X' and board[1][1] =='X' and board[2][2] =='X':
        winner = True
    elif board[2][0] =='X' and board[1][1] =='X' and board[0][2] =='X':
        winner = True
    #checking if O has won
    elif board[0][0] =='O' and board[0][1] =='O' and board[0][2] =='O':
        winner = True
    elif board[1][0] =='O' and board[1][1] =='O' and board[1][2] =='O':
        winner = True
    elif board[2][0] =='O' and board[2][1] =='O' and board[2][2] =='O':
        winner = True   
    elif board[0][0] =='O' and board[1][0] =='O' and board[2][0] =='O':
        winner = True
    elif board[0][1] =='O' and board[1][1] =='O' and board[2][1] =='O':
        winner = True
    elif board[0][2] =='O' and board[1][2] =='O' and board[2][2] =='O':
        winner = True
    elif board[0][0] =='O' and board[1][1] =='O' and board[2][2] =='O':
        winner = True
    elif board[2][0] =='O' and board[1][1] =='O' and board[0][2] =='O':
        winner = True
    else:
        winner = False
    return winner 

#x_redo function - used to inform 'X' player to reenter their move 
def x_redo():
    print('Sorry you have selected a space that is not empty or is invalid, try again.')
    x_move()

#o_redo function - used to inform 'O' player to reenter their move 
def o_redo():
    print('Sorry you have selected a space that is not empty or is invalid, try again.')
    o_move()
    #next_move()


#board_full function - used to check if all spaces are filled / check if there is a tie
def board_full():
    spaces = 0
    for row in [0,1,2]:
        for column in [0,1,2]:
            if board[row][column] == 'X' or board[row][column] == 'O':
                spaces = spaces + 1
    if spaces == 9:
        print('Game is a tie!')
    return spaces


#restart function - used at end of game function to ask users if they would like to play again
def restart():
    restart_game = input('Do you want to play again?')
    if restart_game.upper() in ['YES', 'Y', 'YEAH', 'SURE']:
        game()
    elif restart_game.upper() in ['NO', 'N', 'NOPE', 'bye']:
        print('Ok thanks for playing')
    else:
        print('Ok thanks for playing')
        
    
#game function - main function to play tic-tac-toe
def game():
    first_board()
    draw_board()
    next_move()
    print('Game over')
    restart()


### Play Tic-Tac-Toe ###
    
#call game function to play tic-tac-toe
game()

