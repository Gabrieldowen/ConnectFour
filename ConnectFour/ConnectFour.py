# create a connect four game
import subprocess

import random
import time
# Variables
print("\n\nWelcome To Connect Four! Your will play as 'X' \n\n")
Board = [[' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],]

currentPlayer = 'X'
Running = True
winner = None



#1 print board
def printBoard(Board):
  
    print("  1   2   3   4   5   6   7")
    print("----------------------------")
    print("|",Board[5][0],"|", Board[5][1],"|", Board[5][2],"|", Board[5][3],"|", Board[5][4],"|", Board[5][5],"|", Board[5][6],"|")
    print("-----------------------------")
    print("|",Board[4][0],"|", Board[4][1],"|", Board[4][2],"|", Board[4][3],"|", Board[4][4],"|", Board[4][5],"|", Board[4][6],"|")
    print("-----------------------------")
    print("|",Board[3][0],"|", Board[3][1],"|", Board[3][2],"|", Board[3][3],"|", Board[3][4],"|", Board[3][5],"|", Board[3][6],"|")
    print("-----------------------------")
    print("|",Board[2][0],"|", Board[2][1],"|", Board[2][2],"|", Board[2][3],"|", Board[2][4],"|", Board[2][5],"|", Board[2][6],"|")
    print("-----------------------------")
    print("|",Board[1][0],"|", Board[1][1],"|", Board[1][2],"|", Board[1][3],"|", Board[1][4],"|", Board[1][5],"|", Board[1][6],"|")
    print("-----------------------------")
    print("|",Board[0][0],"|", Board[0][1],"|", Board[0][2],"|", Board[0][3],"|", Board[0][4],"|", Board[0][5],"|", Board[0][6],"|")
    print("-----------------------------")




#3 check for game over

#check for verticle win, only need to check pieces under most recent since pieces get placed at the top
def CheckVert(Board, column, row):    
    global winner
    #print("column: " + str(column+1))
    #print("row: " + str(row+1))

    
    if Board[row][column] == Board[row-1][column]==Board[row-2][column] == Board[row-3][column] and row>=3:
        winner = Board[row][column]
        #print("*************WINNER_Vert****************")
        return True

def CheckHorz(Board, column, row):
    global winner

    while column < 6:

        if Board[row][column]== Board[row][column+1]: # finds the farthest matching piece to the right
            column = column + 1                                         # shifts one to the right
        else:
            break

    if Board[row][column] == Board[row][column-1]==Board[row][column-2] == Board[row][column-3] and column>=3:
        #print("*************WINNER_Horz****************")
        winner = Board[row][column]
        return True

def CheckDiag(Board, column, row):
    global winner

    while column < 6 and row < 5:
        if Board[row][column]== Board[row+1][column+1]: # finds the farthest matching piece to the right
            column = column + 1                              # shifts one to the right
            row = row + 1                                      # shifts up
        else:
            break

    if Board[row][column] == Board[row-1][column-1] == Board[row-2][column-2] == Board[row-3][column-3] and column>=3 and row>=3:
        #print("*************WINNER_Diag****************")
        winner = Board[row][column]
        return True


#update 
#find correct row to place new token in and checks for win
def TokenPlacement(token):

    print(f"\nPiece will be placed here: {token+1}")
    for i in range(0, 6):
        if Board[i][token] == ' ':        # puts piece at the top of the column
            Board[i][token] = currentPlayer
            column = token
            row = i
            if CheckVert(Board, column, row) or CheckHorz(Board, column, row) or CheckDiag(Board, column, row):  #CHECKS FOR WINNER
                printBoard(Board)
                if winner == 'X':
                    print("\n*****YOU WIN!!!*****\n")
                    subprocess.call(["afplay", "Victory.mp3"])
                else:
                    print("\n***** You Lose *****")
                    subprocess.call(["afplay", "Loser.mp3"])
                exit()    #quits game after winner is declared

            return      # if slot is found return to switch turns
    
    if currentPlayer == 'X':
        token = input("\nthat column is full enter new space: ")
    if currentPlayer == 'O':
        token = random.randint(1,7)
            


#chooses computers move

def ComputerMove(Board):
    global LastMove
    print("\nHmm...")
    time.sleep(1)
    token = LastMove + random.randint(-1,+1)
    while token < 1 and token > 7:
        if token < 1:
            token = token +1
        elif token > 7:
            token = token + 1

    print(f"\nIll go here: {token+1}" )
    time.sleep(1)
    TokenPlacement(token)
    

#2 take input

def PlayerInput(Board):
    global LastMove


    token = int(input("\n Please Enter a Number to place your piece: "))  #takes player input
  

    # checks if input is valid 
    if token <= 7 and token >= 1:
       LastMove = token = token - 1
    else:
        print("\n **INVALID INPUT**")
        return 0
    
    TokenPlacement(token)
   

#Switch to turns between computer and Player

def SwitchTurn():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    

#4 update and repeat (Updates while games running)

while Running:
    global LastMove
    printBoard(Board)
    if winner != None:
        break
    PlayerInput(Board)

    

    printBoard(Board)

    time.sleep(1)

    SwitchTurn()
    ComputerMove(Board)
    SwitchTurn()


 


    





