#Tic Tac Toe Checker
#http://www.codewars.com/kata/tic-tac-toe-checker/

def isSolved(board):
    #Checking for WINS first
    #Check rows first, easiest to check
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]
          
    #check columns
    for col in range(3):
        if len(set([board[0][col], board[1][col], board[2][col]])) == 1 and board[0][col] != 0:
            return board[0][col]
          
    #check diagonals
    if len(set([board[0][0], board[1][1], board[2][2]])) == 1 and board[0][0] != 0:
        return board[0][0]
      
    if len(set([board[0][2], board[1][1], board[2][0]])) == 1 and board[0][2] != 0:
        return board[0][0]
      
    #Checking for DRAW second
    if 0 not in set(board[0] + board[1] + board[2]):
        return 0
    #If we get this far, game hasn't been completed yet
    else:
        return -1